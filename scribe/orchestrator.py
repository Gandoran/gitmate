from scribe import git_extractor
from scribe import ai_engine
from scribe import istructions
from scribe import folder_extractor

def create_commit_message():
    git_extractor.git_add()
    changes = git_extractor.extract_changes()
    if(not changes):
        return "Nothing added to the commit"
    message = ai_engine.ollama_chat(istructions.REGOLE_COMMIT,changes)
    print(f"\n Messaggio generato:\n\n{message}\n")
    response = input("Vuoi procedere? (Y/N): ")
    return handle_response(response,message)

def create_readme():
    text=folder_extractor.extract_project_text()
    message = ai_engine.ollama_chat(istructions.REGOLE_README,text)
    print(f"\n Messaggio generato:\n\n{message}\n")
    return message


def handle_response(response,message):
    if(response == 'Y' or response == 'y'):
        git_extractor.git_commit(message)
        git_extractor.git_push_commit()
        status = "Commit Published"
    else:
        git_extractor.git_reset()
        status = "Commit Aborted"
    return status