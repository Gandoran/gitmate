import subprocess
import sys

def extract_changes():
    try:
        result = subprocess.run(args=["git", "diff", "--staged"],check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def git_add():
    try:
        subprocess.run(args=['git','add','.'],check=True)
    except subprocess.CalledProcessError:
        return("No File to add")

def git_commit(message):
    try:
        subprocess.run(args=['git','commit','-m',message],check=True)
    except subprocess.CalledProcessError:
        return ("Cannot commit")

def git_retrieve_current_branch():
    try:
        result = subprocess.run(args=["git","rev-parse","--abbrev-ref","HEAD"],check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return("Cannot retrieve a branch")
    
def git_push_commit():
    try:
        subprocess.run(args=['git','push','origin',git_retrieve_current_branch()],check=True)
        return("Commit published correctly")
    except subprocess.CalledProcessError:
        return("Cannot push")
