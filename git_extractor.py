import subprocess
import sys

def extract_changes():
    try:
        result = subprocess.run(args=["git", "diff", "--staged"],check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        print("Not in a git folder: ")