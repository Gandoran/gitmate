import os
import sys
import ollama
import yaml
from pathlib import Path

from scribe.create_global_configuration import create_default_global

def load_config():
    local_config = "gitmate_config.yaml"
    global_config = os.path.join(Path.home(), ".gitmate", "gitmate_config.yaml")
    try:
        if os.path.exists(local_config):
            with open(local_config, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        if os.path.exists(global_config):
            with open(global_config, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        print(f"First start, creating the configuration file in: {global_config}")
        create_default_global(global_config)
        with open(global_config, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        sys.exit(1)

CONFIG = load_config()

def ollama_chat(system_istruction,git_changes,profile="light"):
    selected_profile = CONFIG['profiles'].get(profile,CONFIG['profiles']['light'])
    response = ollama.chat(
        model= selected_profile['model'], 
        messages=[
        {'role': 'system','content': system_istruction},
        {'role': 'user','content': git_changes}],
        options=selected_profile['options'],
        keep_alive=0
    )
    return response['message']['content']
