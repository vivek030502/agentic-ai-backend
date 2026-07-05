from pathlib import Path

from app.repository.models import (
    RepositoryDirectory,
    RepositoryFile,
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
    ) -> tuple[list[RepositoryDirectory], list[RepositoryFile]]:

        root = Path(repository_path)

        if not root.exists():
            raise FileNotFoundError(
                f"Repository does not exist: {repository_path}"
            )

        if not root.is_dir():
            raise ValueError(
                f"Repository path is not a directory: {repository_path}"
            )

        directories: list[RepositoryDirectory] = []
        files: list[RepositoryFile] = []

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
        directories: list[RepositoryDirectory],
        files: list[RepositoryFile],
    ) -> None:

        for item in current.iterdir():

            if item.name in self.IGNORED_DIRECTORIES:
                continue

            if item.name in self.IGNORED_FILES:
                continue

            if item.is_dir():

                directories.append(
                    RepositoryDirectory(
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
                RepositoryFile(
                    path=self._relative_path(root, item),
                    name=item.name,
                    extension=item.suffix.lower(),
                    language=self._detect_language(item.suffix),
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

    @staticmethod
    def _detect_language(extension: str) -> str:

        mapping = {
            ".py": "python",
            ".java": "java",
            ".kt": "kotlin",
            ".js": "javascript",
            ".ts": "typescript",
            ".tsx": "typescript",
            ".jsx": "javascript",
            ".vue": "vue",
            ".html": "html",
            ".css": "css",
            ".scss": "scss",
            ".json": "json",
            ".xml": "xml",
            ".yaml": "yaml",
            ".yml": "yaml",
            ".sql": "sql",
            ".md": "markdown",
            ".txt": "text",
            ".go": "go",
            ".cs": "csharp",
            ".php": "php",
            ".rb": "ruby",
            ".rs": "rust",
            ".cpp": "cpp",
            ".c": "c",
            ".h": "c",
        }

        return mapping.get(extension.lower(), "text")