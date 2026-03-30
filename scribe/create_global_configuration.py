import os

def create_default_global(filepath):
    default_yaml = """# GitMate Global Config
profiles:
  light:
    model: "qwen2.5-coder:7b"
    options:
      num_ctx: 8192           
      num_predict: 2048            

  heavy:
    model: "qwen2.5-coder:7b"       #you can change it with a more powerful Model
    options:
      num_ctx:
      num_ctx: 8192
      num_predict: 4096           

git:
  default_language: "-it"      
  max_commit_history: 20
"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(default_yaml)