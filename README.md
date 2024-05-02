<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
  </a>

  <h3 align="center">SVG Backend Service</h3>

  <p align="center">
    This project implements a Backend Game Service for Simple Viral Games using Django RestFramework and Postgresql as the database. It has Django's built-in caching that caches the data for a range of time. Additionally filtering and Pagination are implemented as well. The Service follows best practices of RESTFul principles.
  </p></div>
<!-- ABOUT THE PROJECT -->

## Overview

The project consists of several components:

- Django: Provides the REST API endpoints for interacting with the Game Backend Service and its CRUD Operations.
- Postgresql: Used as the database.



## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.9 or higher



<!-- GETTING STARTED -->
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your username>/SVG-Backend-Service.git
   cd svg_backend

2. Create and activate a virtual environment:

   ```bash
    python3 -m venv venv
    venv/Scripts/activate

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

   
## Running Locally

1. Create a .env file and add your variables, SECRET_KEY for Django and NAME, USER, PASSWORD, HOST and PORT for setting up PostgreSQL Database. You can use pgadmin locally as well as Cloud alternative which is easily available on Render.

2. Run DB Migrations
    ```sh
   py manage.py makemigrations
   py manage.py migrate
   ```
    
3. Start the DRF application:
   ```sh
   py manage.py runserver
   ```

   ```
The Backend Service should now be accessible at http://localhost:8000. To go directly to main page => http://localhost:8000/v1/games

You can also test the APIS using swagger UI. Just go to http://localhost:8000/v1/swagger/




## Running via hosted service

The Backend Service is hosted on Render and available to tinker on https://svg-backend-service-1.onrender.com


## Usage
Once the Service is running, you can interact with it using HTTP requests. Here are some example requests:

Data Schema:
```json
{
 "name" : "<game_name>",
 "url" : "<game_url>",
 "author" : "<game_author>",
 "published_date" : "<game_published_date>"
}
```

Create Single Game:

```bash
http://localhost:8000/v1/games/new-game       (along with data)
```
or
```bash
https://svg-backend-service-1.onrender.com/v1/games/new-game     (along with data)
```


Read Single Game:

```bash
http://localhost:8000/v1/games/<int:pk>
```
or
```bash
https://svg-backend-service-1.onrender.com/v1/games/<int:pk>
```


Get All Games:

```bash
http://localhost:8000/v1/games
```
or
```bash
https://svg-backend-service-1.onrender.com/v1/games
```


Update Single Game:

```bash
http://localhost:8000/v1/games/<int:pk>     (along with Body)
```
or
```bash
https://svg-backend-service-1.onrender.com/v1/games/<int:pk>     (along with body)
```


Delete Single Game:

```bash
http://localhost:8000/v1/games/<int:pk>/
```
or
```bash
https://svg-backend-service-1.onrender.com/v1/games/<int:pk>/
```
<div align="center">
  <h3 align="center">Thank You !!!</h3>
</div>
