import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from app.analysis.repository.models import Dependency


class DependencyParser:
    """
    Parses project dependencies from different package managers.

    Supported:
    - requirements.txt
    - pyproject.toml
    - package.json
    - pom.xml
    - build.gradle
    """

    def parse(
        self,
        repository_path: str,
    ) -> list[Dependency]:
        """
        Parse dependencies from the repository.

        Args:
            repository_path: Local repository path.

        Returns:
            List of Dependency objects.
        """

        root = Path(repository_path)

        dependencies: list[Dependency] = []

        parsers = [
            self._parse_requirements,
            self._parse_pyproject,
            self._parse_package_json,
            self._parse_maven,
            self._parse_gradle,
        ]

        for parser in parsers:
            dependencies.extend(parser(root))

        return self._remove_duplicates(dependencies)

    # ------------------------------------------------------------
    # requirements.txt
    # ------------------------------------------------------------

    def _parse_requirements(
        self,
        root: Path,
    ) -> list[Dependency]:

        file = root / "requirements.txt"

        if not file.exists():
            return []

        dependencies = []

        for line in file.read_text(
            encoding="utf-8",
            errors="ignore",
        ).splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            if "==" in line:

                name, version = line.split(
                    "==",
                    1,
                )

                dependencies.append(
                    Dependency(
                        name=name.strip(),
                        version=version.strip(),
                    )
                )

            else:

                dependencies.append(
                    Dependency(
                        name=line,
                        version=None,
                    )
                )

        return dependencies

    # ------------------------------------------------------------
    # pyproject.toml
    # ------------------------------------------------------------

    def _parse_pyproject(
        self,
        root: Path,
    ) -> list[Dependency]:

        file = root / "pyproject.toml"

        if not file.exists():
            return []

        text = file.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        dependencies = []

        pattern = r'([A-Za-z0-9_\-]+)\s*=\s*"([^"]+)"'

        for match in re.finditer(pattern, text):

            dependencies.append(
                Dependency(
                    name=match.group(1),
                    version=match.group(2),
                )
            )

        return dependencies

    # ------------------------------------------------------------
    # package.json
    # ------------------------------------------------------------

    def _parse_package_json(
        self,
        root: Path,
    ) -> list[Dependency]:

        file = root / "package.json"

        if not file.exists():
            return []

        data = json.loads(
            file.read_text(
                encoding="utf-8",
            )
        )

        dependencies = []

        for section in [
            "dependencies",
            "devDependencies",
        ]:

            for name, version in data.get(
                section,
                {},
            ).items():

                dependencies.append(
                    Dependency(
                        name=name,
                        version=version,
                    )
                )

        return dependencies

    # ------------------------------------------------------------
    # Maven
    # ------------------------------------------------------------

    def _parse_maven(
        self,
        root: Path,
    ) -> list[Dependency]:

        file = root / "pom.xml"

        if not file.exists():
            return []

        tree = ET.parse(file)

        root_element = tree.getroot()

        namespace = {
            "m": "http://maven.apache.org/POM/4.0.0"
        }

        dependencies = []

        for dependency in root_element.findall(
            ".//m:dependency",
            namespace,
        ):

            group = dependency.find(
                "m:groupId",
                namespace,
            )

            artifact = dependency.find(
                "m:artifactId",
                namespace,
            )

            version = dependency.find(
                "m:version",
                namespace,
            )

            if artifact is None:
                continue

            dependencies.append(
                Dependency(
                    name=f"{group.text}:{artifact.text}"
                    if group is not None
                    else artifact.text,
                    version=version.text
                    if version is not None
                    else None,
                )
            )

        return dependencies

    # ------------------------------------------------------------
    # Gradle
    # ------------------------------------------------------------

    def _parse_gradle(
        self,
        root: Path,
    ) -> list[Dependency]:

        build_file = None

        if (root / "build.gradle").exists():
            build_file = root / "build.gradle"

        elif (root / "build.gradle.kts").exists():
            build_file = root / "build.gradle.kts"

        if build_file is None:
            return []

        text = build_file.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        dependencies = []

        pattern = r'["\']([\w\-.]+):([\w\-.]+):([\w\-.]+)["\']'

        for match in re.finditer(
            pattern,
            text,
        ):

            dependencies.append(
                Dependency(
                    name=f"{match.group(1)}:{match.group(2)}",
                    version=match.group(3),
                )
            )

        return dependencies

    # ------------------------------------------------------------
    # Remove duplicate dependencies
    # ------------------------------------------------------------

    def _remove_duplicates(
        self,
        dependencies: list[Dependency],
    ) -> list[Dependency]:

        unique = {}

        for dependency in dependencies:

            unique[dependency.name] = dependency

        return sorted(
            unique.values(),
            key=lambda item: item.name.lower(),
        )