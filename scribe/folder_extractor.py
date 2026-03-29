import os
from scribe.token_reducer import file_clean

FOLDER_IGNORE = ['.venv', '__pycache__', '.git', 'node_modules', 'target', 'dist', 'build', '.next']
FILE_IGNORE = ['package-lock.json', 'yarn.lock', 'Cargo.lock']
EXTENSION_IGNORE = ('.exe', '.png', '.jpg', '.pdf', '.pyc','.md')

def extract_project_text():
    complete_text = ""
    for root, dirs, files in os.walk('.'):
        if ".gitignore" in files:
            gitignore_rule=extract_git_ignore_files(root)
        dirs[:] = [d for d in dirs if d not in FOLDER_IGNORE and d not in gitignore_rule]
        for file in files:
            if file.endswith(EXTENSION_IGNORE) or file in FILE_IGNORE or file in gitignore_rule or file == ".gitignore":
                continue
            route = os.path.join(root, file)
            complete_text += file_clean(route)
    return complete_text

def extract_git_ignore_files(root):
    gitignore_rule = set()
    gitignore_route = os.path.join(root, ".gitignore")
    try:
        with open(gitignore_route, "r", encoding="utf-8") as file_git:
            for line in file_git:
                riga_pulita = line.strip()
                if riga_pulita and not riga_pulita.startswith('#'):
                    gitignore_rule.add(riga_pulita.rstrip('/'))
    except Exception:
        pass
    return gitignore_rule