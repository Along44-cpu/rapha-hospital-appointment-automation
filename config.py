"""
Global configuration for automation project output paths.
All scripts should use this module to ensure consistent output handling.
"""

from pathlib import Path
import os

# Central output directory - all scripts save here by default
# Uses environment variable if set, otherwise defaults to relative 'outputs' directory
OUTPUT_DIR = Path(os.getenv('AUTOMATION_OUTPUT_DIR', './outputs')).resolve()

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def get_output_path(filename):
    """
    Get the full path for an output file in the central output directory.

    Args:
        filename (str): Name of the output file (e.g., 'report.txt')

    Returns:
        Path: Full path to the output file
    """
    return OUTPUT_DIR / filename

def ensure_output_dir():
    """Ensure the output directory exists."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR
