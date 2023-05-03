
# Task Manager API

This is a simple Flask-based API for managing tasks. It provides endpoints for creating, updating, and deleting tasks, as well as retrieving tasks by status or priority.

## Getting Started

### Prerequisites

* Python 3.x
* Flask
* sqlite3

### Installing

1. Clone this repository:
   ````
   git clone https://github.com/your-username/task-manager-api.git
   ```
2. Create a virtual environment:
   ````
   python3 -m venv env
   ```
3. Activate the virtual environment:
   ````
   source env/bin/activate
   ```
4. Install the required packages:
   ````
   pip install -r requirements.txt
   ```
5. Run the Flask app:
   ````
   flask run
   ```
   The app will be available at http://localhost:5000.

## Usage

### Endpoints

The following endpoints are available:

* `GET /tasks` - Get all tasks
* `GET /tasks/<int:task_id>` - Get a specific task by ID
* `POST /tasks` - Create a new task
* `PUT /tasks/<int:task_id>` - Update an existing task
* `DELETE /tasks/<int:task_id>` - Delete a task
* `GET /tasks?status=<status>` - Get tasks by status
* `GET /tasks?priority=<priority>` - Get tasks by priority

### Request and Response Formats

The API accepts and returns JSON data. Here are the formats for the request and response bodies:

#### Creating a task

Request:
```
{
    "title": "Task title",
    "description": "Task description",
    "status": "Not started",
    "priority": "Low",
    "due_date": "2023-05-10"
}
```

Response:
```
{
    "task": {
        "id": 1,
        "title": "Task title",
        "description": "Task description",
        "status": "Not started",
        "priority": "Low",
        "due_date": "2023-05-10"
    }
}
```

#### Updating a task

Request:
```
{
    "title": "Updated task title",
    "description": "Updated task description",
    "status": "In progress",
    "priority": "High",
    "due_date": "2023-05-15"
}
```

Response:
```
{
    "id": 1,
    "title": "Updated task title",
    "description": "Updated task description",
    "status": "In progress",
    "priority": "High",
    "due_date": "2023-05-15"
}
```

#### Getting tasks by status or priority

Response:
```
{
    "tasks": [
        {
            "id": 1,
            "title": "Task title",
            "description": "Task description",
            "status": "Not started",
            "priority": "Low",
            "due_date": "2023-05-10"
        },
        {
            "id": 2,
            "title": "Another task",
            "description": "Another task description",
            "status": "In progress",
            "priority": "Medium",
            "due_date": "2023-05-12"
        }
    ]
}
```

### Error Handling

The API returns the following HTTP error codes:

* 400 Bad Request - if the request is malformed or missing required parameters
* 404 Not Found - if the requested task does not exist
* 500 Internal Server Error - for any other error

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
