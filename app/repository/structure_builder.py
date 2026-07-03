from app.analysis.repository.models import (
    ProjectDirectory,
    ProjectFile,
)


class RepositoryStructureBuilder:
    """
    Builds a human-readable repository tree.

    Responsible only for converting scanned directories and files
    into a tree representation.
    """

    def build(
        self,
        directories: list[ProjectDirectory],
        files: list[ProjectFile],
    ) -> str:
        """
        Build repository tree.

        Example:

        app/
        ├── api/
        │   └── routes.py
        ├── services/
        │   └── github.py
        └── main.py
        """

        tree = {}

        # Add directories
        for directory in directories:
            self._insert(
                tree,
                directory.path,
                is_file=False,
            )

        # Add files
        for file in files:
            self._insert(
                tree,
                file.path,
                is_file=True,
            )

        lines: list[str] = []

        self._render(
            tree=tree,
            lines=lines,
            prefix="",
        )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Insert node
    # ---------------------------------------------------------

    def _insert(
        self,
        tree: dict,
        path: str,
        is_file: bool,
    ) -> None:

        parts = path.split("/")

        current = tree

        for index, part in enumerate(parts):

            last = index == len(parts) - 1

            if last and is_file:

                current.setdefault("__files__", [])

                current["__files__"].append(part)

            else:

                current = current.setdefault(part, {})

    # ---------------------------------------------------------
    # Render tree
    # ---------------------------------------------------------

    def _render(
        self,
        tree: dict,
        lines: list[str],
        prefix: str,
    ) -> None:

        directories = sorted(
            [
                key
                for key in tree.keys()
                if key != "__files__"
            ]
        )

        files = sorted(
            tree.get(
                "__files__",
                [],
            )
        )

        items = directories + files

        for index, item in enumerate(items):

            is_last = index == len(items) - 1

            connector = "└── " if is_last else "├── "

            lines.append(
                prefix + connector + item
            )

            if item in tree:

                extension = (
                    "    "
                    if is_last
                    else "│   "
                )

                self._render(
                    tree[item],
                    lines,
                    prefix + extension,
                )