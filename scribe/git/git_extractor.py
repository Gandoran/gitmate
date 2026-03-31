import subprocess

def extract_changes():
    try:
        result = subprocess.run(args=["git", "diff", "--staged"],check=True, capture_output=True, text=True, encoding="utf-8")
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

def git_reset():
    try:
        subprocess.run(args=['git','reset'],check=True)
        return("Commit Reverted")
    except subprocess.CalledProcessError:
        return("Error durring reversion")

def get_last_tag():
    try:
        result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def git_extract_commits(n_commit=20):
    try:
        result = subprocess.run(args=['git', 'log', '--pretty=format:%h - %s', '-n', str(n_commit)],
                                check=True,capture_output=True,text=True,encoding="utf-8")
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return("Error durring reversion")
    
def extract_commits_since_tag(last_tag):
    try:
        if last_tag:
            args = ['git', 'log', f'{last_tag}..HEAD', '--pretty=format:%h - %s']
        else:
            args = ['git', 'log', '--pretty=format:%h - %s'] 
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return("Error during retrieve the commits")
    
def github_cli_push(version,msg):
    try:
        subprocess.run(['gh', 'release', 'create', version, '--title', f'Release {version}', '--notes', msg], 
                            check=True, capture_output=True)
        return f"Release {version} created and pubblished on GitHub!"
    except FileNotFoundError:
            return f"Tag: {version} pushed! (Download GitHub CLI 'gh' to create the web release in automatic)"
    except subprocess.CalledProcessError:
        return "Error during github release"
    
def create_tag(version):
    try:
        subprocess.run(['git', 'tag', '-a', version, '-m', f'Release {version}'], check=True)
    except subprocess.CalledProcessError:
        return "Error during release creation"

def push_tag(version):
    try:
        subprocess.run(['git', 'push', 'origin', version], check=True)
    except subprocess.CalledProcessError:
        return "Error during release commit"

 