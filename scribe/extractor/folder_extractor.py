import os
from scribe.ai_package import token_reducer
from scribe.extractor import gitignore_parser

def extract_project_text(root_path="."):
    extracted_lines = []
    rules = gitignore_parser.load_gitignore_rules(root_path)
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if not gitignore_parser.is_ignored(d, True, rules)]
        for file in files:
            if gitignore_parser.is_ignored(file, False, rules):
                continue
            route = os.path.join(root, file)
            extracted_lines.append(token_reducer.file_clean(route))
    return "".join(extracted_lines)