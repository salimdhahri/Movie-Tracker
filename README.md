<table>
<tr><th>Tracker App</th></tr>
<tr><td>

## Overview

The Tracker App is a web-based movie recommendation system that helps users discover new movies based on their preferences. It utilizes a backend server built with Flask and a frontend interface developed using React.js. The system manages user data, movie information, and recommendations through interactions with CSV and SQL databases.

## Features

- **User Authentication:** Users can log in using their unique user ID or create a new account if they're new to the system.
- **Watched List:** Users can maintain a list of watched movies, including details such as title, date watched, and user rating.
- **Adding Movies:** Users can add new movies to their watched list, providing details like title, date watched, and rating.
- **Genre and Director Search:** Users can explore movies by searching for specific genres or directors, receiving recommendations based on their preferences.
- **Recent Releases:** The system displays information about recent movie releases, allowing users to stay updated on new releases.

## Technologies Used

- React.js: Frontend library for building dynamic user interfaces.
- Flask: Backend framework for building the server-side application.
- Axios: JavaScript library for making HTTP requests to the server.
- CSS: Used for styling the frontend components and providing a visually appealing user interface.
- CSV and SQL Databases: Used for storing and managing data related to users, movies, genres, and directors.

## Installation

To run the Tracker App locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using npm install.
4. Start the development server using npm start.

Make sure you have Node.js and npm installed on your machine before proceeding with the installation.

## Usage

Once the development server is running, you can access the Tracker App in your web browser. The app provides various features for users to interact with, including logging in, adding movies to their watched list, searching for movies by genre or director, and exploring recent releases.

## Project Structure

- **src/:** Contains the source code for the React frontend.
- **components/:** Contains React components used to build the user interface.
- **data/:** Contains CSV and SQL files used as databases to store movie and user information.
- **App.js:** Main component that renders the application.
- **public/:** Contains public assets such as images and static files.
- **server.py:** Backend server implemented using Flask for handling user requests and database interactions.
- **README.md:** This file providing an overview of the project.

## Credits

The implementation of the Tracker App was inspired by Pete's Software Certification Modules, particularly Modules 4 and 6, which provided guidance on building Flask and React applications.

</td></tr>
<tr><th>Tracker Server</th></tr>
<tr><td>

## Overview

The Tracker Server is a Flask-based web application designed to manage users' watched movies and provide recommendations based on various criteria such as genre and director. It utilizes embedded SQL queries to interact with a MySQL database containing information about movies, users, and directors.

## Installation

To run the Tracker Server locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using pip install -r requirements.txt.
4. Set up the MySQL database with the appropriate schema and tables. Ensure that the necessary environment variables for database connection (e.g., DATAHOST, DATAUSER, DATAPWD, DATADATABASE) are configured.
5. Run the Flask application using python tracker_server.py.

## Features

1. **User Management**
   - **Login:** Users can log in using their user ID. New users can create an account by providing their first name, last name, and email address.
   - **Get Watched Movies:** Retrieve a list of movies that a user has watched along with the watch date and user rating.
   - **Add User:** Add a new user to the system by providing their personal information.

2. **Movie Management**
   - **Add Movie:** Users can add movies to their watched list by selecting from a list of available movies and providing the watch date and rating.
   - **Recent Movies:** Display three recent movies released after a specified date.
   - **Get Genre:** Get recommendations of movies in a specific genre.
   - **Get Director:** Get recommendations of movies directed by a specific director.

3. **Recommendations**
   - **Genre Suggestions:** Provide movie recommendations based on a user's favorite genre.
   - **Recent Movies Suggestions:** Recommend recently released movies to users.
   - **Director Suggestions:** Recommend movies directed by a specific director.

## Usage

Once the server is running, users can interact with the API endpoints using HTTP requests. The API endpoints include:

- /login: Login or create a new user account.
- /watched: Get watched movies for a user.
- /adduser: Add a new user.
- /addmovie: Add a movie to the watched list.
- /recentmovies: Get recent movie recommendations.
- /getGenre: Get movie recommendations based on genre.
- /getDirector: Get movie recommendations based on director.

</td></tr>
</table>
