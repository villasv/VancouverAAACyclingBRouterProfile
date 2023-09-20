import sys
import logging
from rich.console import Console
from rich.logging import RichHandler

stderr_console = Console(file=sys.stderr)

logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=stderr_console)],
)

log = logging.getLogger()
