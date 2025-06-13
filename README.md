# File Cleaner Bot

This is a simple Python script that automatically cleans up filenames in a selected folder. It's useful for organizing files by applying consistent naming rules.

## What It Does

- Removes extra spaces at the beginning or end of filenames
- Converts filenames to lowercase
- Replaces spaces within filenames with underscores
- Fixes common file extension formats:
  - `.jpeg` is changed to `.jpg`
  - `.htm` is changed to `.html`
- Skips renaming if the cleaned filename already exists

## Files

- `clean_filenames.py`: The main script that performs the cleaning
- `test_clean_filenames.py`: A test script used to check that the main script works correctly

## How to Use

1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python clean_filenames.py


