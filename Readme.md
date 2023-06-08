# Pokemon CRUD operation

This project implements a simple CRUD operation for managing Pokemon data. It fetching the data from an JSON url to Database. It provides APIs for creating, reading, updating, and deleting Pokemon records.

### Access the APIs using the provided endpoints ( http://localhost:5000/pokemon/api ).

### Direction
- For starting app, run the start.py file.
- The basic config is in app/config.py
- Table and Marshallow schema is in app/models.py
- APIs is in app/views.py

### Installation Process
1)   "python3 -m venv venv"
- run the command to create a new venv
2) "source myenv/bin/activate"
- to activate virtual environment
3) "export FLASK_APP=start.py" 
    "flask run"
- execute the above command to run the app
- it will run in debug: OFF mode

## Features

- create a model and insert the data from url
- Create a new Pokemon record
- Read Pokemon records
- Update existing Pokemon records
- Delete Pokemon records

## API Endpoints
- GET /pokemon: Get a list of all Pokemon records. Search by name, type 1 and legendary
- GET /pokemon/{id}: Get the details of a specific/all Pokemon by ID.
- POST /pokemon: Create a new Pokemon record.
- PUT /pokemon/{id}: Update the details of a specific Pokemon by ID and update by using UPSERT command.
- DELETE /pokemon/{id}: Delete a specific Pokemon by ID.