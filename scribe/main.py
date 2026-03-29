import sys
from scribe import cmd_commit, cmd_readme

def main():
    command = sys.argv
    if len(command) < 2:
        print("Try use: gitmate -<comando>. with the commands: commit, readme")
        sys.exit(1)
    azione = command[1]
    lan = command[2] if len(command) > 2 else "-it"
    if azione == "-commit":
        message = cmd_commit.execute(lan)
    elif azione == "-readme":
        message = cmd_readme.execute(lan)
    else:
        message = "Command not recognized, Try use: gitmate -<comando>. with the commands: commit, readm"
        
    print(message)

if __name__ == "__main__":
    main()