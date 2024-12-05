# TaskTrackerCLI

Task tracker is a project used to track and manage your tasks 

# Actions
- Add, Update and Delete Tasks
- MArk a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are in progress

# Task Properties

- **id**: A unique identifier for the task
- **description**: A short description of the task
- **status**: The status of the task (todo, in-progress, done)
- **createdAt**: The date and time when the task was created
- **updatedAt**: The date and time when the task was last updated

# Usage

`# Adding a new task`
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress`

https://roadmap.sh/projects/task-tracker
