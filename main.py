import os


def create_and_commit(filename, message, days_ago=0):
    """
    Creates a file with the given filename and content, adds it to the Git index,
    and commits it with the provided message.

    Args:
      filename: The name of the file to create.
      message: The commit message.
    """
    # Check if Git is installed
    if not os.path.exists(".git"):
        print("Error: Not a Git repository")
        return

    # Create the file with some content
    with open(filename, "w") as f:
        f.write("This is a new file.\n")

    # Stage the file for commit
    os.system(f"git add {filename}")

    # Commit the changes with the message
    if days_ago == 0:
        os.system(f"git commit -m \"{message}\"")
    else:
        os.system(f"git commit -m \"{message}\" --date=\"{days_ago}days ago\"")

    print(f"Created file '{filename}' and committed with message: {message}")


# Example usage
days = int(input("Days to streak you want : "))

for i in range(0, days + 1):
    filename = f"new_file_{i}.txt"
    message = "Added a new file"
    create_and_commit(filename, message, i)

print("[+] use the following commond to push")
print("-> git push")
