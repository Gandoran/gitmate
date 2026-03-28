import os
import ollama

MODELLO = os.getenv("GITMATE_MODEL", "qwen2.5-coder:7b")
TOKEN_INPUT = int(os.getenv("TOKEN_INPUT", "8192"))
TOKEN_OUTPUT = int(os.getenv("TOKEN_OUTPUT", "2048"))

def ollama_chat(system_istruction,git_changes):
    response = ollama.chat(
        model=MODELLO, 
        messages=[
        {
            'role': 'system',
            'content': system_istruction
        },
        {
            'role': 'user',
            'content': git_changes
        }],
        options={
            'num_ctx': TOKEN_INPUT,
            'num_predict': TOKEN_OUTPUT
        }
    )
    return response['message']['content']
