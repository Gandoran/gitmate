import os

FOLDER_IGNORE = {'.venv', '__pycache__', '.git', 'node_modules', 'target', 'dist', 'build', '.next'}
FILE_IGNORE = {'package-lock.json', 'yarn.lock', 'Cargo.lock'}
EXTENSION_IGNORE = ('.exe', '.png', '.jpg', '.pdf', '.pyc', '.md')

def load_gitignore_rules(root_path="."):
    rules = set()
    gitignore_path = os.path.join(root_path, ".gitignore")    
    if not os.path.exists(gitignore_path):
        return rules
    try:
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and not line.strip().startswith('#'):
                    rules.add(line.strip().rstrip('/'))
    except Exception:
        pass
    return rules

def is_ignored(name, is_dir, rules):
    if is_dir:
        return name in FOLDER_IGNORE or name in rules
    else:
        return name.endswith(EXTENSION_IGNORE) or name in FILE_IGNORE or name in rules or name == ".gitignore"