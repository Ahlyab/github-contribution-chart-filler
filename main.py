import os
import random


def create_and_commit(filename, message, days_ago=0):
  """
  Creates a file with the given filename and content, adds it to the Git index,
  and commits it with the provided message.

  Args:
    filename: The name of the file to create.
    message: The commit message.
    days_ago: The number of days ago for the commit date (optional).
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
    os.system(
        f"git commit -m \"{message}\" --date=\"{days_ago} days ago\"")

  print(f"Created file '{filename}' and committed with message: {message}")


# Example usage
days = int(input("Days to streak you want : "))

for i in range(1, days + 1):
  # Generate random number of commits between 1 and 10
  num_commits = random.randint(1, 13)
  for j in range(num_commits):
    filename = f"new_file_{i}_{j}.txt"
    message = f"Added a new file on day {i} - commit {j+1}"
    create_and_commit(filename, message, days - i + 1)

print("[+] use the following command to push")
print("-> git push")
