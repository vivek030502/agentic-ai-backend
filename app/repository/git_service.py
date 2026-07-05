from pathlib import Path
import subprocess

from app.config.logger import app_logger


class GitService:
    """
    Performs git operations on
    the local cloned repository.
    """

    def commit_and_push(
        self,
        repository_path: str,
        branch: str,
        message: str,
    ):

        root = Path(repository_path)

        commands = [

            ["git", "add", "."],

            ["git", "commit", "-m", message],

            ["git", "push", "origin", branch],

        ]

        for command in commands:

            app_logger.info(
                "Running: %s",
                " ".join(command),
            )

            result = subprocess.run(
                command,
                cwd=root,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:

                # git commit exits with code 1 if nothing changed
                if (
                    command[1] == "commit"
                    and "nothing to commit" in result.stdout.lower()
                ):
                    continue

                raise Exception(
                    result.stderr or result.stdout
                )

        app_logger.info("Push completed.")