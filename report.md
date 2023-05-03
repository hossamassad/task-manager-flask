Design Choices

The Task Manager API is designed to provide endpoints for managing tasks. The API is built using Flask, a lightweight web framework, and SQLite, a relational database management system. Flask is chosen due to its simplicity, flexibility and ease of use, whereas SQLite is chosen for its small size, portability and the fact that it is a built-in module in Python.

The API provides endpoints for creating, updating, and deleting tasks, as well as retrieving tasks by status or priority. Each task has a title, description, status, priority, and due date. The status and priority of a task are predefined values, which helps to ensure consistency and ease of searching.

The API is designed to be RESTful, meaning that each endpoint is associated with a specific HTTP method and URL. For example, the GET /tasks endpoint returns all tasks, while the POST /tasks endpoint creates a new task.
Challenges

The main challenge in developing this API was designing the schema for the tasks table. The schema needed to be flexible enough to accommodate different types of tasks, while also being simple enough to allow for easy querying. In addition, the schema needed to allow for easy updates and deletions of tasks.

Another challenge was ensuring that the API followed best practices for error handling and input validation. The API needed to handle errors gracefully and provide informative error messages to the client.
Improvements

There are several improvements that can be made to the Task Manager API, such as:

    Adding authentication and authorization: Currently, the API does not require any authentication or authorization, which could lead to security vulnerabilities. Adding authentication and authorization mechanisms would make the API more secure and prevent unauthorized access.

    Adding pagination: If the number of tasks grows large, it may become difficult to retrieve all tasks at once. Adding pagination would allow for retrieving tasks in smaller chunks, which would improve performance.

    Adding filtering and sorting: Currently, the API only allows for retrieving tasks by status or priority. Adding filtering and sorting capabilities would allow for more advanced querying, which would make the API more flexible and useful.


Conclusion

Overall, the Task Manager API is a simple and effective API for managing tasks. It is designed to be easy to use and to follow best practices for RESTful APIs. The use of Flask and SQLite makes the API lightweight and portable, while providing the necessary functionality for managing tasks. The API is well-documented and follows best practices for error handling and input validation. However, there is always room for improvement, and the above suggestions could be implemented to make the API more secure, flexible, and reliable.
