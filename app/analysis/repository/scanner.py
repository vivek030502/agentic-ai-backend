from pathlib import Path

from app.analysis.repository.models import (
    ProjectDirectory,
    ProjectFile,
)


class RepositoryScanner:
    """
    Scans a repository and returns all directories and files.

    Responsible only for filesystem scanning.
    No framework detection or dependency parsing.
    """

    # Directories to ignore
    IGNORED_DIRECTORIES = {
        ".git",
        ".idea",
        ".vscode",
        "__pycache__",
        "node_modules",
        "venv",
        ".venv",
        "target",
        "build",
        "dist",
        ".mypy_cache",
        ".pytest_cache",
        ".tox",
        ".gradle",
        "out",
    }

    IGNORE_EXTENSIONS = {
        ".class",
        ".jar",
        ".war",
        ".exe",
        ".dll",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".ico",
        ".pdf",
        ".zip",
        ".7z",
        ".tar",
        ".gz",
        ".mp4",
        ".mp3"
    }

    # Files to ignore
    IGNORED_FILES = {
        ".DS_Store",
    }

    def scan(
        self,
        repository_path: str,
    ) -> tuple[list[ProjectDirectory], list[ProjectFile]]:
        """
        Scan the repository recursively.

        Args:
            repository_path:
                Absolute or relative repository path.

        Returns:
            Tuple of:
                - List[ProjectDirectory]
                - List[ProjectFile]
        """

        root = Path(repository_path)

        if not root.exists():
            raise FileNotFoundError(
                f"Repository does not exist: {repository_path}"
            )

        if not root.is_dir():
            raise ValueError(
                f"Repository path is not a directory: {repository_path}"
            )

        directories: list[ProjectDirectory] = []
        files: list[ProjectFile] = []

        self._scan_directory(
            root=root,
            current=root,
            directories=directories,
            files=files,
        )

        directories.sort(key=lambda d: d.path)
        files.sort(key=lambda f: f.path)

        return directories, files

    def _scan_directory(
        self,
        root: Path,
        current: Path,
        directories: list[ProjectDirectory],
        files: list[ProjectFile],
    ) -> None:
        """
        Recursively scan a directory.
        """

        for item in current.iterdir():

            if item.name in self.IGNORED_DIRECTORIES:
                continue

            if item.name in self.IGNORED_FILES:
                continue

            if item.is_dir():

                directories.append(
                    ProjectDirectory(
                        path=self._relative_path(
                            root,
                            item,
                        )
                    )
                )

                self._scan_directory(
                    root=root,
                    current=item,
                    directories=directories,
                    files=files,
                )

            elif item.is_file():

                files.append(
                    ProjectFile(
                        path=self._relative_path(
                            root,
                            item,
                        ),
                        extension=item.suffix.lower(),
                        size=item.stat().st_size,
                    )
                )

    @staticmethod
    def _relative_path(
        root: Path,
        path: Path,
    ) -> str:
        """
        Convert absolute path to repository-relative path.
        """

        return str(
            path.relative_to(root)
        ).replace("\\", "/")