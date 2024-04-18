import os
import random


def create_and_commit(filename, message, days_ago=0):
  
  # Check if Git is installed
  if not os.path.exists(".git"):
    print("Error: Not a Git repository")
    return

  # Create the directory 'green' if it doesn't exist
  if not os.path.exists("green"):
    os.makedirs("green")

  # Create the file with some content inside 'green' directory
  with open(os.path.join("green", filename), "w") as f:
    f.write("This is a new file.\n")

  # Stage the file for commit
  os.system(f"git add green/{filename}")  # Add with full path

  # Commit the changes with the message
  if days_ago == 0:
    os.system(f"git commit -m \"{message}\"")
  else:
    os.system(
        f"git commit -m \"{message}\" --date=\"{days_ago}days ago\"")

  print(f"Created file 'green/{filename}' and committed with message: {message}")


# Example usage
days = int(input("Days to streak you want : "))
fn = input("Enter filename without extension : ")

for i in range(1, days + 1):
  # Generate random number of commits between 1 and 10
  num_commits = random.randint(1, 10)
  for j in range(num_commits):
    filename = f"{fn}_{i}_{j}.txt"
    message = f"Added a new file on day {i} - commit {j+1}"
    create_and_commit(filename, message, days - i + 1)

print(
  "\n\n----------------------------------------\n[+] use the following command to push")
print("-> git push")
