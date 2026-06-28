# Responsible for: Console logging, File logging, Log formatting, Debug logs, Error logs

from pathlib import Path
import sys

from loguru import logger

from app.config.settings import settings

# Create the logs directory if it doesn't already exist.
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove Loguru's default logger configuration.
# This allows us to define our own logging format and outputs.
logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
)

# File Logger
logger.add(
    LOG_DIR / "application.log",
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
)

# Export the configured logger
app_logger = logger