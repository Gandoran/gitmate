from scribe.git import git_extractor
from scribe.ai_package import ai_runner
from scribe.cmd import interaction_handler
from scribe.ai_package import istructions, prompt_builder

def execute(lan):
    text = git_extractor.git_extract_commits(20) 
    if not text or "error" in text:
        return "No commits found or errors in extraction."
    base_prompt = prompt_builder.build_prompt(istructions.REGOLE_CHANGELOG, lan)
    message = ai_runner.execute_with_animation(base_prompt, text, "Writing the CHANGELOG.md", profile="heavy")
    return interaction_handler.handle_interaction(
        starting_message=message,
        change_prompt_m="Modifica questo changelog rispettando la richiesta:",
        func_accept=save_changelog,
        func_refuse=undo_changelog,
        output_title="CHANGELOG Created"
    )

def save_changelog(msg):
    with open("CHANGELOG.md", "w", encoding="utf-8") as f:
        f.write(msg)
    return "CHANGELOG.md saved!"

def undo_changelog():
    return "Operation aborted."