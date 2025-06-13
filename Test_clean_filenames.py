import os
from clean_filenames import clean_filenames  # Match the exact filename and function name

def test_clean_filenames(tmp_path):
    # Create fake messy files inside temporary folder
    messy_filenames = [
        "My  FILE .jpeg",
        "Report   (1).TXT",
        "notes .CSV"
    ]

    for name in messy_filenames:
        file_path = tmp_path / name
        file_path.write_text("dummy content")

    # Run the cleaning function
    clean_filenames(str(tmp_path))

    # Expected cleaned filenames
    expected_filenames = [
        "my__file.jpg",       # .jpeg → .jpg
        "report___(1).txt",    # .TXT → .txt
        "notes.csv"           # .CSV → .csv
    ]

    # Check that each cleaned file now exists
    for expected in expected_filenames:
        expected_path = tmp_path / expected
        assert expected_path.exists(), f"{expected} not found after cleaning"
