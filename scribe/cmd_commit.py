from scribe import git_extractor, prompt_builder, istructions
from scribe.ai_runner import execute_with_animation

def execute(lan):
    git_extractor.git_add()
    changes = git_extractor.extract_changes()
    if not changes:
        return "Nothing added to the commit"       
    prompt = prompt_builder.build_prompt(istructions.REGOLE_COMMIT, lan)
    message = execute_with_animation(prompt, changes, "Analysis of changes")
    print(f"\nGenerated Message:\n\n{message}\n")
    response = input("Do you want to proceed? (Y/N): ")
    if response.lower() == 'y':
        git_extractor.git_commit(message)
        git_extractor.git_push_commit()
        return "Commit Published"
    else:
        git_extractor.git_reset()
        return "Commit Aborted"