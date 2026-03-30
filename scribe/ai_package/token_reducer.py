import os

MAINTAIN_RULES = {
    '.rs': ('fn ', 'struct ', 'enum ', 'impl ', 'pub trait ', 'mod '),
    '.ts': ('interface ', 'type ', 'class ', 'function ', 'export '),
    '.tsx': ('interface ', 'type ', 'class ', 'function ', 'export '),
    '.py': ('def ', 'class ', '@'),
    '.java': ('class ', 'interface ', 'enum ', 'public ', 'protected ', 'private ', '@')
}

def file_clean(file_path):
    _, ext = os.path.splitext(file_path)
    rule = MAINTAIN_RULES.get(ext)
    lines = [f"\n--- FILE: {file_path} ---\n"]
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            if rule is None:
                lines.append(f.read())
            else:
                for line in f:
                    if line.strip().startswith(rule):
                        lines.append(line)
    except Exception:
        return ""
    return "".join(lines) + "\n"