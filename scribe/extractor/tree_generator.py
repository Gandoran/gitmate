import os
from scribe.extractor import gitignore_parser

def generate_tree(startpath=".", prefix="", rules=None):
    if rules is None:
        rules = gitignore_parser.load_gitignore_rules(startpath)
    tree_str = ""
    try:
        items = os.listdir(startpath)
    except PermissionError:
        return ""
    dirs = sorted([d for d in items if os.path.isdir(os.path.join(startpath, d)) and not gitignore_parser.is_ignored(d, True, rules)])
    files = sorted([f for f in items if os.path.isfile(os.path.join(startpath, f)) and not gitignore_parser.is_ignored(f, False, rules)])
    entries = dirs + files
    for i, entry in enumerate(entries):
        path = os.path.join(startpath, entry)
        is_last = (i == len(entries) - 1)
        pointer = "└── " if is_last else "├── "
        tree_str += f"{prefix}{pointer}{entry}\n"
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix=prefix + extension, rules=rules)
    return tree_str

def get_project_structure(root_path="."):
    project_name = os.path.basename(os.path.abspath(root_path))
    tree = generate_tree(root_path)
    struttura = (
        f"```text\n"
        f"{project_name}/\n"
        f"{tree}"
        f"```\n"
    )
    return struttura