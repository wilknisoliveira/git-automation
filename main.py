import logging
import os
import git
from git import Repo


def repo_commands(name, relative_path, commands):
    local_repo_path = os.path.dirname(os.path.realpath(__file__))
    local_repo_path = os.path.join(local_repo_path, relative_path)

    print(f'## Repository: {name} ##')  # Press Ctrl+F8 to toggle the breakpoint.

    try:
        repo = Repo(local_repo_path)
    except git.exc.NoSuchPathError as e:
        print(f"Error while trying to set the repository from:\n{e}")
        return

    for command in commands:
        if "push" in command:
            print(f"\nThe following command will be executed: {command}")
            confirm = input("Are you sure you want to execute this operation? (y/n): ")
            if confirm == 'y':
                execute_git_command(command, repo)
            else:
                print("Command not executed!")
        else:
            execute_git_command(command, repo)


def execute_git_command(git_command, repository):
    print("\n#Command: " + git_command)
    try:
        response = repository.git.execute(git_command)
        logging.info(response)
        print(response)
    except git.exc.GitCommandError as e:
        print(f"Error:\n {e}")
        return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # Set here your repositories and commands
    repositories = [
        {
            "name": "new-feature",
            "path": "../rebase-upstream-test-new-feature",
            "commands": [
                "git checkout main",
                "git pull",
                # "git fetch upstream",
                # "git rebase upstream/main",
                # "git push --force",
                # "git checkout dev",
                # "git rebase main",
                "git push --force"
            ]
        },
        {
            "name": "original",
            "path": "../rebase-upstream-test-original",
            "commands": [

            ]
        }
    ]

    while True:
        print("--- Git Automation ---")
        print("Repositories:")
        for index, repository in enumerate(repositories):
            print(f"{index} - {repository["name"]}")

        repo_name = input("To be safe, insert the repository name: ")
        print("\n")

        find_repo = False
        for repository in repositories:
            if repo_name == repository["name"]:
                find_repo = True
                repo_commands(repository["name"], repository["path"], repository["commands"])
                input("\nInsert anything to continue: ")

        if not find_repo:
            print(f"Check the repository name! You entered: {repo_name}")
            input("Insert anything to continue: ")

        print("\n\n\n")
