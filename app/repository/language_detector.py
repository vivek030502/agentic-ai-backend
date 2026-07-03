LANGUAGE_MAP = {

    ".java": "java",

    ".py": "python",

    ".js": "javascript",

    ".ts": "typescript",

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

    ".txt": "text"
}


def detect_language(extension: str) -> str:
    return LANGUAGE_MAP.get(
        extension.lower(),
        "text"
    )