import time
import threading

from scribe import git_extractor
from scribe import ai_engine
from scribe import istructions
from scribe import folder_extractor
from scribe import loading_bar

def create_commit_message():
    git_extractor.git_add()
    changes = git_extractor.extract_changes()
    if not changes:
        return "Nothing added to the commit"
    message = esegui_con_animazione(istructions.REGOLE_COMMIT, changes, "Reading the changes")
    print(f"\nMessaggio generato:\n\n{message}\n")
    response = input("Do you want to procede? (Y/N): ")
    return handle_response(response, message)

def create_readme():
    text = folder_extractor.extract_project_text()    
    message = esegui_con_animazione(istructions.REGOLE_README, text, "Writing the README.md")
    print(f"\nREADME created:\n\n{message}\n")
    response = input("Do you want to save it as README.md? (Y/N): ")
    if response.lower() == 'y':
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(message)
        return "README.md saved!"
    else:
        return "Saving the README aborted."


def handle_response(response,message):
    if(response == 'Y' or response == 'y'):
        git_extractor.git_commit(message)
        git_extractor.git_push_commit()
        status = "Commit Published"
    else:
        git_extractor.git_reset()
        status = "Commit Aborted"
    return status

def esegui_con_animazione(istruzioni, dati, testo_barra="Im reasoning"):
    stop_event = threading.Event()
    thread = threading.Thread(target=loading_bar.print_bar, args=(stop_event, testo_barra))
    thread.start()
    message = ai_engine.ollama_chat(istruzioni, dati)
    stop_event.set()
    thread.join()
    return message