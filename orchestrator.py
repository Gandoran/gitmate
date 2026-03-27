import git_extractor
import ia_chat
import istructions

def create_commit_message():
    changes = git_extractor.extract_changes()
    if(not changes):
        return "Nothing added to the commit"
    message = ia_chat.ollama_chat(istructions.REGOLE_COMMIT,changes)
    return message