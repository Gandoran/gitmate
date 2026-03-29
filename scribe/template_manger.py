import os

def add_template(testo_codice, prompt_base):
    n_token = os.getenv("TOKEN_OUTPUT",4096)
    used_token = token_calc(testo_codice) + token_calc(prompt_base)
    token_left = n_token - used_token - 1000 
    try:
        template = choose_template(token_left)
    except FileNotFoundError:
        return prompt_base
    if template:
        prompt_esteso = f"{prompt_base}\n\nECCO UN TEMPLATE DI ESEMPIO DA SEGUIRE COME STILE:\n{template}"
        return prompt_esteso
    else:
        return prompt_base

def token_calc(text):
    return len(text) // 4

def choose_template(token_left):
    template = ""
    if token_left >= 2000:
        with open("templates/readme_large.md", "r", encoding="utf-8") as f:
            template = f.read()
    elif token_left >= 800:
        with open("templates/readme_medium.md", "r", encoding="utf-8") as f:
            template = f.read()
    elif token_left >= 200:
        with open("templates/readme_small.md", "r", encoding="utf-8") as f:
            template = f.read()
    return template