"""
Create a zip file out of all files that end in .tox in a directory
"""

__author__ = "SudoMagic"
__copyright__ = "Copyright 2026, SudoMagic"
__credits__ = ["Matthew Ragan", "Gemini"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Matthew Ragan"

from pathlib import Path
import os
import zipfile

def zip_contents():
    """
    """
    release_path = Path(Path.cwd(), os.getenv("SM_RELEASE_DIR"))
    zip_files_by_extension(release_path, 'tox', f'{release_path.as_posix()}/package.zip')

def zip_files_by_extension(dir: Path, ext: str, outputFile:str) -> Path:
    """
    """
    with zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in dir.rglob(f'*.{ext}'):
            print(f"Adding {file.name} to zip")
            zipf.write(file, os.path.relpath(file, dir))


if __name__ == "__main__":
    zip_contents()
