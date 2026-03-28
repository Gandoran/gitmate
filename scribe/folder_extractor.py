import os

FOLDER_IGNORE = ['.venv', '__pycache__', '.git', 'node_modules']
EXTENSION_IGNORE = ('.exe', '.png', '.jpg', '.pdf', '.pyc')

def extract_project_text():
    complete_text = ""
    gitignore_rule = []

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in FOLDER_IGNORE and d not in gitignore_rule]
        if ".gitignore" in files:
            gitignore_route = os.path.join(root, ".gitignore")
            try:
                with open(gitignore_route, "r", encoding="utf-8") as file_git:
                    for line in file_git:
                        if line.strip() and not line.strip().startswith('#'):
                            gitignore_rule.append(line.strip().rstrip('/'))
            except Exception:
                pass
        for file in files:
            if file.endswith(EXTENSION_IGNORE) or file in gitignore_rule or file == ".gitignore":
                continue
            route = os.path.join(root, file)
            try:
                with open(route, "r", encoding="utf-8") as f:
                    content = f.read()
                    complete_text += f"\n--- FILE: {file} ---\n{content}\n"
            except Exception:
                pass
    return complete_text