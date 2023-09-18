import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="DEBUG", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger()
