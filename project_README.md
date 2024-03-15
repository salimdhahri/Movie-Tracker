# Welcome to our Movie Database! 
CS374 Database Management  
Fall 2023  
Final Project  
Team Members: Salim Dhari, Michelle Lie, and Esther Ng

<b>This file includes: purpose, program requirements, how to run the program, queries written out in words, future implementations.</b>

## Purpose
Our program aims to allow users to make an account where they can store the movies they've watched, including the date they watched it and their rating. The program also gives user suggestions for movies.

This is achieved through using MySQLWorkbench to manage the data. Primary modifications and implementation of the code is done through `server.py`, which uses the Flask framework of Python, to manage queries using embedded SQL. The `index.js` file uses the React library of Javascript and communicates with the server. `index.css` is then used for designing the webpage and tables.

For more detailed information on the structure, UML diagrams, and code challenges, please see our [program presentation](https://www.canva.com/design/DAF25lqq22s/yH5K-V4IXKwB0fjsGcwAtg/edit?utm_content=DAF25lqq22s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## Requirements
The Movie Database is connected with a database on MySQLWorkbench. The .sql files must be imported to a schema named "Project" locally, in order to run the queries successfully.

A `.env` file must be made in the `tracker-server` of this project, with your MySQLWorkbench password.

Installation of the libraries in the `requirements.txt` file must be downloaded, which can be done using the following terminal command:
```
pip install -r requirements.txt 
```

Flask framework must also be installed using:
```
pip install flask
pip install flask-cors
```

Lastly, the axios library of React must be installed:
```
npm install axios
```

## How to Run the Program
The `server.py` file must be run in `tracker-server`:
```
cd tracker-server
python3 server.py
```
The `index.js` file must be run in `tracker-app`:
```
cd tracker-app
npm start
```

## Queries Included

* Get all the movies a specific user has watched (getWatched)
* Retrieve 3 movies released recently (recentMovies)
* Retrieve 3 movies in a specific genre (getGenre)
* Retrieve other movies a specific director made (getDirector)

Other interactions with the database include getting a user's first name from their ID to display a welcome message, getting the user ID that is auto-generated for a new user, and getting the movie ID to insert movies into a specific user's watched list.

## Future Implementation and Work
There are many aspects that can be further developed for better use of this program:

* Better functionality of the code, especially using components in React to display specific sections of the site rather than using boolean values
* The web interface can also be improved upon, to make it more engaging and easy to navigate
* Implement more advanced SQL queries, such as ones requiring calculations of average ratings
* Allow users to change their ratings, add a rewatch date, add notes for a movie
* Include more precise recommendations, such as a specific genre of movies released in a specific year
* Also, add more movies. For now, the database only has 50 movies since the focus was more on the queries and the user interface. However, it would be great having a bigger database with more movies.
