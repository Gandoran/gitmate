from scribe.istructions import REGOLE_ENG, REGOLE_IT

def build_prompt(base_rule, lan):
    lan_rule = REGOLE_IT if lan == "-it" else REGOLE_ENG
    return f"{lan_rule}\n\n{base_rule}"