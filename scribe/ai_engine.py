import ollama

def ollama_chat(system_istruction,git_changes):
    response = ollama.chat(model='qwen2.5-coder:7b', messages=[
    {
        'role': 'system',
        'content': system_istruction
    },
    {
        'role': 'user',
        'content': git_changes
    }])
    return response['message']['content']
