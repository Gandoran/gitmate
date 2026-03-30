from scribe.extractor import git_extractor
from scribe.ai_package import ai_runner
from scribe.cmd import interaction_handler
from scribe.ai_package import istructions, prompt_builder

def execute(lan):
    git_extractor.git_add()
    changes = git_extractor.extract_changes()
    if not changes:
        return "Nothing added to the commit"       
    prompt = prompt_builder.build_prompt(istructions.REGOLE_COMMIT, lan)
    message = ai_runner.execute_with_animation(prompt, changes, "Analysis of changes",profile="light")
    return interaction_handler.handle_interaction(
        starting_message=message,
        change_prompt_m="Modifica il seguente messaggio di commit rispettando questa richiesta:",
        func_accept=save_commit,
        func_refuse=undo_commit,
        output_title="Generated Message"
    )

def save_commit(msg):
    git_extractor.git_commit(msg)
    git_extractor.git_push_commit()
    return "Commit Published"
def undo_commit():
    git_extractor.git_reset()
    return "Commit Aborted"