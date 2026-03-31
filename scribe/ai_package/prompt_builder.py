from scribe.ai_package.istructions import REGOLE_ENG, REGOLE_IT,REGOLE_COMMIT

def build_prompt(base_rule, lan):
    lan_rule = REGOLE_IT if lan == "-it" else REGOLE_ENG
    return f"{lan_rule}\n\n{base_rule}"

def build_user_payload(codice_diff, lan, tipo_promemoria=None):
    if not tipo_promemoria:
        return codice_diff
    lingua_target = "ITALIANO" if lan == "-it" else "INGLESE"
    promemoria_formattato = tipo_promemoria.format(lingua=lingua_target)
    return f"{codice_diff}\n\n{promemoria_formattato}"