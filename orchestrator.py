import git_extractor
import ia_chat
import istructions

def create_commit_message():
    git_extractor.git_add()
    changes = git_extractor.extract_changes()
    if(not changes):
        return "Nothing added to the commit"
    message = ia_chat.ollama_chat(istructions.REGOLE_COMMIT,changes)
    print(f"\n Messaggio generato:\n\n{message}\n")
    response = input("Vuoi procedere? (Y/N): ")
    if(response == 'Y' or response == 'y'):
        git_extractor.git_commit(message)
        git_extractor.git_push_commit()
    return message