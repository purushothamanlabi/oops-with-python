"""
PYTHON BUILT-IN FUNCTIONS & STANDARD LIBRARIES
A quick reference guide for essential Python modules.
"""

import os
import sys
import json
import csv
import re
import random
import subprocess
import logging
import argparse
from pathlib import Path
from datetime import datetime, date, timedelta

# =================================================================
# MODULE OVERVIEW
# =================================================================
# os         -> Operating system tasks (files, directories)
# sys        -> Python system-specific parameters and functions
# pathlib    -> Object-oriented file system paths
# datetime   -> Date and time manipulation
# json       -> JSON data encoding and decoding
# csv        -> CSV file reading and writing
# re         -> Regular expressions
# random     -> Generate pseudo-random numbers
# subprocess -> Run system commands
# logging    -> Event logging for applications
# argparse   -> Command-line option and argument parsing

# =================================================================
# 1. JSON MODULE EXAMPLE
# =================================================================
# Working with JSON data (Dictionaries to Strings/Files and vice-versa)

data = {"name": "Aakash", "age": 20}

# Writing to a file
with open("data.json", "w") as f:
    json.dump(data, f)

# Reading from a file
with open("data.json", "r") as f:
    loaded_data = json.load(f)
    print(f"File Object: {f}")
    print(f"Loaded JSON: {loaded_data}")

# =================================================================
# 2. PATHLIB EXAMPLE (Preview)
# =================================================================
current_path = Path.cwd()
print(f"Current Directory: {current_path}")

# =================================================================
# END OF NOTES
# =================================================================
