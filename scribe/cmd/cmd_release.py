from scribe.git import git_extractor
from scribe.ai_package import ai_runner, istructions, prompt_builder
from scribe.cmd import interaction_handler
import subprocess

def execute(lan):
    ultimo_tag = git_extractor.get_last_tag()
    commits = git_extractor.extract_commits_since_tag(ultimo_tag)
    if not commits: return "No commit from the last tag."
    prompt = prompt_builder.build_prompt(istructions.REGOLE_RELEASE, lan)
    message = ai_runner.execute_with_animation(prompt, commits, "Writing Release Notes...", profile="heavy")
    return interaction_handler.handle_interaction(
        starting_message=message,
        change_prompt_m="Modifica le note di rilascio seguendo questa istruzione:",
        func_accept=save_release,
        func_refuse=undo_release,
        output_title="Release Notes created"
    )

def undo_release():
    return "Release aborted"

def save_release(msg):
    version = input("\nEnter the version number (es. v1.2.0):\n> ").strip()
    git_extractor.create_tag(version)
    git_extractor.push_tag(version)
    git_extractor.github_cli_push(version,msg)