# Chatbot 🚀
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This project developed using Flask and integrates with the Hugging Face to handle user questions  
returning responses that are stored in a PostgreSQL database.  
The entire application, including the database, is containerized using Docker, with Docker Compose for easy orchestration.  
A basic test suite using Pytest is included to ensure functionality.  

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Run Project](#run)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Additional Notes](#additional-notes)
- [Contact](#contact)

## Features 🌟 <a name="features"></a>
- **Flask Backend**: RESTful API with an endpoint to handle user questions.
- **OpenAI API Integration**: Sends questions to OpenAI and retrieves responses.
- **PostgreSQL Database**: Stores questions and corresponding answers.
- **Alembic Migrations**: Manages database schema changes.
- **Dockerized Setup**: Both the Flask server and PostgreSQL database are containerized.
- **Docker Compose**: Simplifies container management and networking.
- **Testing with Pytest**: Includes a test suite for the `/ask` endpoint.

## Prerequisites 📋  <a name="prerequisites"></a>
Docker  
OpenAI API Key: To interact with the OpenAI API, store your API key in an .env file.  

## Installation and Setup 🛠️  <a name="installation-and-setup"></a>  
Clone the Repository:  
 ```
git clone https://github.com/Avivdo7/chatbot.git
 cd chatbot
```

Set Up Environment Variables: Create a .env file in the root directory with the following variables:  
```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
API_KEY=your_openai_api_key

```

## Run 🏃   <a name="run"></a>

Build and Run with Docker Compose: Build and start the containers:  
```
docker-compose up --build
```
This will set up the Flask server at http://localhost:5000 and connect to the PostgreSQL database.  

Run Migrations: apply database migrations with Alembic:
```bash
docker-compose exec web alembic upgrade head
```
  

## Usage 📖  <a name="usage"></a>
Endpoint: The main endpoint is /ask.  
Method: POST  
```json
Payload:
{
  "question": "What is the capital of France?"
}
Response:
{
  "question": "What is the capital of France?",
  "answer": "The capital of France is Paris."
}
```

## Running Tests 🧪  <a name="running-tests"></a>

To execute the tests within Docker:

```
docker-compose run test
```

The tests validate the /ask endpoint functionality and ensure correct integration with the mocked OpenAI API.

## Project Structure 📂 <a name="project-structure"></a>
```
your-repository/
│
├── app.py                 # Flask application entry point
├── Dockerfile             # Dockerfile for the Flask app
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── alembic/               # Alembic migrations directory
├── templates/             # Frontend HTML files
└── test_app.py/           # Pytest test file
```

## Additional Notes ℹ️  <a name="additional-notes"></a>
Database Management: Alembic is used for migrations. To create a new migration, run:  

```
docker-compose exec web alembic revision --autogenerate -m "Migration message"
```
Stopping the Containers: To stop all running containers:  
```
docker-compose down
```

## Contact 📫  <a name="contact"></a>
For any questions, please contact avivdm7@gmail.com .  
