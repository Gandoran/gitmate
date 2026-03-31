import sys
from scribe.cmd import cmd_changelog, cmd_commit, cmd_readme, cmd_release

def execute_commands():
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
    elif azione == "-changelog":
        message = cmd_changelog.execute(lan)
    elif message == "-release":
        message = cmd_release.execute(lan)
    else:
        message = "Command not recognized, Try use: gitmate -<comando>. with the commands: commit, readm"
    print(message)

def main():
    try:
        execute_commands()
    except KeyboardInterrupt:
        print("Operation aborted by the user")
        sys.exit(0)


if __name__ == "__main__":
    main()