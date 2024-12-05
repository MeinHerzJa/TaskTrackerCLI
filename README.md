# TaskTrackerCLI

Task tracker is a project used to track and manage your tasks. This is a solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/)


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

# How to Run

Clone the repository

```bash
git clone https://github.com/MeinHerzJa/TaskTrackerCLI.git
```

```bash
# Adding a new task
% add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
% update 1 "Buy groceries and cook dinner"
% delete 1

# Marking a task as in progress or done
% mark-in-progress 1
% mark-done 1

# Listing all tasks
% list

# Listing tasks by status
% list done
% list todo
% list in-progress`
```