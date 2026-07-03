from pathlib import Path

from app.analysis.repository.models import (
    ProjectDirectory,
    ProjectFile,
)


class RepositoryScanner:
    """
    Scans a repository and returns all directories and files.
    """

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

    IGNORED_FILES = {
        ".DS_Store",
    }

    IGNORED_EXTENSIONS = {
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
        ".mp3",
    }

    def scan(
        self,
        repository_path: str,
    ) -> tuple[list[ProjectDirectory], list[ProjectFile]]:

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

        directories.sort(key=lambda x: x.path)
        files.sort(key=lambda x: x.path)

        return directories, files

    def _scan_directory(
        self,
        root: Path,
        current: Path,
        directories: list[ProjectDirectory],
        files: list[ProjectFile],
    ) -> None:

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

                continue

            if item.suffix.lower() in self.IGNORED_EXTENSIONS:
                continue

            try:
                content = item.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )
            except Exception:
                content = ""

            files.append(
                ProjectFile(
                    path=self._relative_path(
                        root,
                        item,
                    ),
                    extension=item.suffix.lower(),
                    size=item.stat().st_size,
                    content=content,
                )
            )

    @staticmethod
    def _relative_path(
        root: Path,
        path: Path,
    ) -> str:

        return str(
            path.relative_to(root)
        ).replace("\\", "/")