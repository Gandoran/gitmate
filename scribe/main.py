import sys
from scribe import orchestrator

def main():
    command = sys.argv
    if len(command) < 2:
        message = "Uso corretto: gitmate -<comando>. Comandi disponibili: commit, readme"
    elif command[1] == "-commit":
        message = orchestrator.create_commit_message()
    elif command[1] == "-readme":
        message = orchestrator.create_readme()
    else:
        message = "Command not recognized"
    print(message)

if __name__ == "__main__":
    main()
