from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)

# Define a function to create the tasks table
def create_tasks_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  status TEXT NOT NULL,
                  priority TEXT NOT NULL,
                  due_date TEXT)''')
    conn.commit()
    conn.close()

# Create the tasks table
create_tasks_table()

# Define endpoints for CRUD operations

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'status': row[3], 'priority': row[4], 'due_date': row[5]} for row in c.fetchall()]
    conn.close()
    return jsonify({'tasks': tasks})

# Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = c.fetchone()
    conn.close()
    if task is None:
        abort(404)
    return jsonify({'id': task[0], 'title': task[1], 'description': task[2], 'status': task[3], 'priority': task[4], 'due_date': task[5]})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'status': request.json.get('status', 'Not started'),
        'priority': request.json.get('priority', 'Low'),
        'due_date': request.json.get('due_date', None)
    }
    if not isinstance(task['title'], str) or not isinstance(task['description'], str) or not isinstance(task['status'], str) or not isinstance(task['priority'], str) or (task['due_date'] is not None and not isinstance(task['due_date'], str)):
        abort(400)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (title, description, status, priority, due_date) VALUES (?, ?, ?, ?, ?)',
              (task['title'], task['description'], task['status'], task['priority'], task['due_date']))
    conn.commit()
    task_id = c.lastrowid
    conn.close()
    task['id'] = task_id
    return jsonify({'task': task}), 201

# Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = c.fetchone()
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    task_title = request.json.get('title', task[1])
    task_description = request.json.get('description', task[2])
    task_status = request.json.get('status', task[3])
    task_priority = request.json.get('priority', task[4])
    task_due_date = request.json.get('due_date', task[5])
    if not isinstance(task_title, str) or not isinstance(task_description, str) or not isinstance(task_status, str) or not isinstance(task_priority, str) or (task_due_date is not None and not isinstance(task_due_date, str)):
        abort(400)
    c.execute('UPDATE tasks SET title = ?, description = ?, status = ?, priority = ?, due_date = ? WHERE id = ?',
              (task_title, task_description, task_status, task_priority, task_due_date, task_id))
    conn.commit()
    conn.close()
    return jsonify({'id': task_id, 'title': task_title, 'description': task_description, 'status': task_status, 'priority': task_priority, 'due_date': task_due_date})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = c.fetchone()
    if task is None:
        abort(404)
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'result': True})

# Get tasks by status
@app.route('/tasks', methods=['GET'])
def get_tasks_by_status():
    status = request.args.get('status', None)
    if status is None:
        abort(400)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE status = ?', (status,))
    tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'status': row[3], 'priority': row[4], 'due_date': row[5]} for row in c.fetchall()]
    conn.close()
    return jsonify({'tasks': tasks})

# Get tasks by priority
@app.route('/tasks', methods=['GET'])
def get_tasks_by_priority():
    priority = request.args.get('priority', None)
    if priority is None:
        abort(400)
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE priority = ?', (priority,))
    tasks = [{'id': row[0], 'title': row[1], 'description': row[2], 'status': row[3], 'priority': row[4], 'due_date': row[5]} for row in c.fetchall()]
    conn.close()
    return jsonify({'tasks': tasks})

# Handle errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)