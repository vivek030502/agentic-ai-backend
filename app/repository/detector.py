from pathlib import Path

from app.analysis.repository.models import ProjectFile


class RepositoryDetector:
    """
    Detects repository metadata from scanned files.

    Responsible for detecting:
    - Programming language
    - Framework
    - Package manager
    - Build system
    - Entry point
    """

    def detect(
        self,
        repository_path: str,
        files: list[ProjectFile],
    ) -> dict:
        """
        Detect repository metadata.

        Returns:
            {
                "language": "...",
                "framework": "...",
                "package_manager": "...",
                "build_system": "...",
                "entry_point": "..."
            }
        """

        root = Path(repository_path)

        return {
            "language": self._detect_language(files),
            "framework": self._detect_framework(root),
            "package_manager": self._detect_package_manager(root),
            "build_system": self._detect_build_system(root),
            "entry_point": self._detect_entry_point(root),
        }

    # ------------------------------------------------------------------
    # Language Detection
    # ------------------------------------------------------------------

    def _detect_language(
        self,
        files: list[ProjectFile],
    ) -> str | None:

        extensions = {
            file.extension.lower()
            for file in files
        }

        if ".py" in extensions:
            return "Python"

        if ".java" in extensions:
            return "Java"

        if ".ts" in extensions:
            return "TypeScript"

        if ".js" in extensions:
            return "JavaScript"

        if ".go" in extensions:
            return "Go"

        if ".cs" in extensions:
            return "C#"

        if ".php" in extensions:
            return "PHP"

        if ".rb" in extensions:
            return "Ruby"

        if ".rs" in extensions:
            return "Rust"

        return None

    # ------------------------------------------------------------------
    # Framework Detection
    # ------------------------------------------------------------------

    def _detect_framework(
        self,
        root: Path,
    ) -> str | None:

        # Python
        if (root / "requirements.txt").exists():

            text = (root / "requirements.txt").read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "fastapi" in text:
                return "FastAPI"

            if "django" in text:
                return "Django"

            if "flask" in text:
                return "Flask"

        if (root / "pyproject.toml").exists():

            text = (root / "pyproject.toml").read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "fastapi" in text:
                return "FastAPI"

            if "django" in text:
                return "Django"

            if "flask" in text:
                return "Flask"

        # Java

        if (root / "pom.xml").exists():

            text = (root / "pom.xml").read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "spring-boot" in text:
                return "Spring Boot"

            if "jersey" in text:
                return "Jersey"

        if (root / "build.gradle").exists():
            return "Spring Boot"

        # Node

        if (root / "package.json").exists():

            text = (root / "package.json").read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "next" in text:
                return "Next.js"

            if "react" in text:
                return "React"

            if "vue" in text:
                return "Vue"

            if "express" in text:
                return "Express"

            if "nestjs" in text:
                return "NestJS"

        return None

    # ------------------------------------------------------------------
    # Package Manager
    # ------------------------------------------------------------------

    def _detect_package_manager(
        self,
        root: Path,
    ) -> str | None:

        if (root / "requirements.txt").exists():
            return "pip"

        if (root / "pyproject.toml").exists():
            return "poetry"

        if (root / "package-lock.json").exists():
            return "npm"

        if (root / "yarn.lock").exists():
            return "yarn"

        if (root / "pnpm-lock.yaml").exists():
            return "pnpm"

        if (root / "pom.xml").exists():
            return "maven"

        if (root / "build.gradle").exists():
            return "gradle"

        return None

    # ------------------------------------------------------------------
    # Build System
    # ------------------------------------------------------------------

    def _detect_build_system(
        self,
        root: Path,
    ) -> str | None:

        if (root / "pom.xml").exists():
            return "Maven"

        if (root / "build.gradle").exists():
            return "Gradle"

        if (root / "Makefile").exists():
            return "Make"

        return None

    # ------------------------------------------------------------------
    # Entry Point
    # ------------------------------------------------------------------

    def _detect_entry_point(
        self,
        root: Path,
    ) -> str | None:

        candidates = [
            "app/main.py",
            "main.py",
            "manage.py",
            "app.py",
            "server.py",
            "src/main.py",
            "src/main/java",
            "src/main/kotlin",
            "index.js",
            "server.js",
            "main.js",
            "index.ts",
            "main.ts",
        ]

        for candidate in candidates:

            if (root / candidate).exists():
                return candidate.replace("\\", "/")

        return None