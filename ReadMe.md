# Installing dependencies
```pip install -r requirements.txt```

# Setting the repositories
Update the file repositories.json with the following structure:

```
[
    {
        "name": "Create a tag name to the repository",
        "path": "../relativePath",
        "commands": [
            "git status",
            "git command 2",
            "git command 3"
        ]
    },
    {
        "name": "Create a tag name to the repository",
        "path": "../relativePath",
        "commands": [
            "git status",
            "git command 2",
            "git command 3"
        ]
    },
    ...
]
```

# Run
Open the terminal in the current folder and execute this command:
```python main.py```
