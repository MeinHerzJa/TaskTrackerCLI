import re
import json
import os
from datetime import datetime

current_path = os.getcwd()
task_path = os.path.join(current_path, "tasks", "task_data.json")


def cli_interface():
    return input("Ingress the action to do: ").lower()


def extract_action(text):
    action = text.split(" ")
    return action[0]


def extract_text(text):
    select_text = re.findall("(\".*?\")", text)[0].replace("\"", "")
    return select_text


def extract_id(text):
    split_text = text.split(" ")
    if len(split_text) <= 2:
        return print("Missing argument")
    elif len(split_text) > 3:
        return print(f"Argument len exceeded. Expected 3 received {len(split_text)}")
    else:
        return split_text[1]


def file_exists():
    if os.path.exists(task_path):
        with open(os.path.join(task_path, task_path)) as file:
            data = json.load(file)
    else:
        data = []
    return data


def update_task(id_to_find, description):
    data = file_exists()
    for task in data:
        if task["id"] == id_to_find:
            print(f"Change description from {task['description']} to {description}")
            now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            task["description"] = description
            task["updateAt"] = now
            return

    print(f"The task with the id: {id_to_find} no exists")


def add_new_task(task_description):
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    data = file_exists()
    if len(data) == 0:
        new_id = 1
    else:
        old_id = data[-1]["id"]
        new_id = old_id + 1
    print(new_id)

    task_data = {
        "id": new_id,
        "description": task_description,
        "status": "todo",
        "createdAt": now,
        "updateAt": now
    }
    data.append(task_data)

    with open(os.path.join(task_path, task_path), 'w') as new_file:
        json.dump(data, new_file)

    return new_id


def delete_task(id_to_find):
    position = 0
    data = file_exists()
    for task in data:
        if task["id"] == id_to_find:
            break
        position += 1
    data.pop(position)


def mark_in_progress(id_to_find):
    data = file_exists()
    for task in data:
        if task["id"] == id_to_find:
            print("Mark task to in-progress")
            task["status"] = "in-progress"
            return
    print(f"The task with the id: {id_to_find} no exists")


def mark_done(id_to_find):
    data = file_exists()
    for task in data:
        if task["id"] == id_to_find:
            print("Mark task to done")
            task["status"] = "done"
            return 
    print(f"The task with the id: {id_to_find} no exists")


if __name__ == "__main__":
    while True:
        input_text = cli_interface()
        print(input_text)
        action_to_do = extract_action(input_text)

        match action_to_do:
            case "add":
                new_task = extract_text(input_text)
                print("Adding a new task")
                last_id = add_new_task(new_task)
                print(f"Output: Task added successfully (ID: {last_id})")
                continue
            case "update":
                task_id = extract_id(input_text)
                if not task_id.isnumeric():
                    print("Invalid Id: is not numeric")
                    continue
                else:
                    print("Updating existing task")
                    new_description = extract_text(input_text)
                    update_task(task_id, new_description)
                continue
            case "delete":
                task_id = extract_id(input_text)
                delete_task(task_id)
                print("delete action")
                continue
            case "mark-in-progress":
                task_id = extract_id(input_text)
                if not task_id.isnumeric():
                    print("Invalid Id: is not numeric")
                    continue
                else:
                    mark_in_progress(task_id)
                    print("Updating existing task")
                continue
            case "mark-done":
                task_id = extract_id(input_text)
                if not task_id.isnumeric():
                    print("Invalid Id: is not numeric")
                    continue
                else:
                    mark_done(task_id)
                    print("Updating existing task")
                continue
            case "list":
                text_split = input_text.split(" ")
                data = file_exists()
                if len(text_split) == 1:
                    print("List all task")
                    if len(data) != 0:
                        for task in data:
                            print(task)
                        continue
                    else:
                        print("No exists any task saved")
                elif len(text_split) == 2 and text_split[1] == "done":
                    print("List done task")
                    if len(data) != 0:
                        for task in data:
                            if task["status"] == "done":
                                print(task)
                        continue
                    else:
                        print("No exists any task saved")
                elif len(text_split) == 2 and text_split[1] == "todo":
                    print("List todo task")
                    if len(data) != 0:
                        for task in data:
                            if task["status"] == "todo":
                                print(task)
                        continue
                    else:
                        print("No exists any task saved")
                elif len(text_split) == 2 and text_split[1] == "in-progress":
                    print("List in-progress task")
                    if len(data) != 0:
                        for task in data:
                            if task["status"] == "in-progress":
                                print(task)
                        continue
                    else:
                        print("No exists any task saved")
                else:
                    print("Invalid or missing argument")
                continue
            case "exit":
                print("Good bye")
                break
            case _:
                print("No valid action")
                continue


