from typing import List
from pathlib import Path

import logging
import brouter

profile = Path("vancycling.brf").read_text()

if __name__ == "__main__":
    brouter.set_profile(profile)
