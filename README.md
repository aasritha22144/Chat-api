Chat History REST API – Assignment

### Description
This assignment focuses on building a simple backend REST API that manages chat history. The API allows users to create chat messages, retrieve all messages, filter messages by user, and clear the entire chat history. The application is developed using FastAPI, stores data in a SQLite database, includes automated test cases using pytest, and is containerized using Docker.

## Objective
The main objective of this assignment is to understand and implement core backend development concepts such as RESTful API design, database integration, data validation, automated testing, and containerized application deployment.



## Technologies Used
FastAPI– for building RESTful APIs  
SQLite – lightweight database for persistent storage  
SQLAlchemy – ORM for database operations  
Pydantic – request and response validation  
Pytest – automated testing framework  
Docker – containerization for consistent execution  


## API Functionality

### 1. Create a Message  
POST /messages

Creates and stores a new chat message in the database.

Request body:

{
  "user": "string",
  "message": "string"
}

### 2. Retrieve All Messages

GET /messages

Retrieves all stored chat messages from the database in chronological order based on the timestamp.

Example response:

[
  {
    "id": 1,
    "user": "Priya",
    "message": "Hello",
    "timestamp": "2025-12-13T06:17:11"
  },
  {
    "id": 2,
    "user": "Aasritha",
    "message": "Hi",
    "timestamp": "2025-12-13T06:18:05"
  }
]

### 3. Retrieve Messages by User

GET /messages/{user}

Retrieves all chat messages sent by a specific user.

If the specified user exists, their messages are returned.

If the user does not exist, an empty list is returned.

Example:

GET /messages/Priya

### 4. Clear Chat History

DELETE /messages

Deletes all chat messages stored in the database.

Response:

{
  "status": "cleared"
}
