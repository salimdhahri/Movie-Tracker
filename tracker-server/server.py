# SERVER FILE
# Includes the embedded sql, api routes, flask functions
# Referenced Pete's Software Certification Modules for implementation of Flask and React, in particular Modules 4 and 6

###################### IMPORTING LIBRARIES ######################
# source: CS100D_Module4 README.md
import sys
sys.path.append('/usr/local/lib/python3.11/site-packages')

import pymysql # library to run the embedded sql with MySQLWorkbench

from flask import Flask, jsonify, request # flask framework
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Test API
@app.route('/')
def index():
    return 'Hello World'

###################### CURSOR DEFINITION ######################
# source: CS100D_Module4 README.md
# defining it once so other functions can call it instead of connecting it every time
def cursor():

    # connected to env file with personal workbench info -> hides the password, user, etc.
    server = os.environ['DATAHOST']
    user = os.environ['DATAUSER']
    pwd = os.environ['DATAPWD']
    db = os.environ['DATADATABASE']

    # connect the login info to the mySQL database
    conn = pymysql.connect(host=server, user=user, password=pwd, database=db)
    conn.autocommit(True)
    crsr = conn.cursor() # set as the cursor
    return crsr

###################### OUR FUNCTIONS HERE #######################
######## login function must be last

##### GET WATCHED MOVIES: get the movies that a user have watched and rated #####
@app.route('/watched', methods=['POST'])
def getWatched():

    crsr = cursor() # call cursor function

    json = request.get_json() 
    userID = json['userID'] # get json object as userID
    
    ## embedded sql: retrieve all the movies this user has watched
    sql = "select m.`Title`, w.`Date Watched`, w.`User Rating` "
    sql = sql + "from project.Watched w, project.Users u, project.Movies m "
    sql = sql + "where w.`user ID` = u.ID and w.`movie ID` = m.ID and u.ID = %s" # using the input from user
    
    crsr.execute(sql, [userID]) # execute the embedded sql using the userID
    rows = crsr.fetchall() # we want all the result lines
    watched = [] # creating a list to put results into

    # formatting the output by looping through all the rows
    for r in rows: 
        watched.append({'Title': r[0], 'Date Watched': r[1], 'User Rating': r[2]})
    
    return jsonify({'User ID': 'user', 'User Name': 'userName', 'Watched': watched }) # returning the results as specific json objects for react to use


##### ADD USER FUNCTION: first name, last name, and email of new users #####
## then insert into the Users table
@app.route('/adduser', methods=['POST'])
def addUser():

    crsr = cursor() # call cursor function

    # json object requests:
    json = request.get_json()
    fName = json['fName'] # new user's first name
    lName = json['lName'] # new user's last name
    email = json['email'] # new user's email

    # embedded sql: add this user into the User table with their first name, last name, and email
    sql = "insert into project.users (`First Name`, `Last Name`, `Email`) "
    sql = sql + f"values ('{fName}', '{lName}', '{email}')"
    crsr.execute(sql)

    # get the user ID, used for other functions
    sql2 = "select ID "
    sql2 = sql2 + "from project.users "
    sql2 = sql2 + f"where `First Name` = {fName} and `Last Name` = {lName} and `Email` = {email}"
    ID = crsr.execute(sql2)

    # return the name and ID to use in other functions, added is a boolean value -> will trigger the welcome message to show
    return jsonify({'newUser': fName, 'added': True, 'userID': ID})


## ADD MOVIE FUNCTION: users can select a movie out of the list to add to their watched list
## then users will put in the date and their rating
@app.route('/addmovie', methods=['POST'])
def addMovie():

    crsr = cursor() # call cursor functions

    # json object requests
    json = request.get_json()
    userID = json['userID']
    date = json['date']
    rating = json['rating']
    addedMovie = json['addedMovie']
    title = json['title']

    # embedded sql: get the ID of this movie
    sql = "select ID "
    sql = sql + "from project.movies "
    sql = sql + f"where title = '{title}'"
    crsr.execute(sql)
    movieID = crsr.fetchone()[0] # only should have 1 number

    # embedded sql: insert that movie into a specific user's watched list, with the date they watched it and their rating
    sql2 = "insert into project.watched "
    sql2 = sql2 + f"values({userID}, {movieID}, '{date}', {rating})"
    crsr.execute(sql2)
     
    # addedMovie is a boolean that triggers a confirmation message 
    return jsonify({'addedMovie': True, 'title': title})


## FUNCTION TO CLEAR INPUT BOXES: after a user added one movie
@app.route('/resetInput', methods=['POST'])
def resetInput():
    title = '' # reset to empty so users can add another movie
    date = ''
    rating = ''
    addedMovie = False # takes away the confirmation message

    # returns empty/false to reuse
    return jsonify({'title': title, 'date': date, 'rating': rating, 'addedMovie': addedMovie})


## SHOW RECENT MOVIES: show the user 3 recent movies
@app.route('/recentmovies', methods=['POST'])
def recentMovies():

    crsr = cursor() # call cursor function

    # embedded sql: retrieve 3 movies released after November 1
    sql = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
    sql += "FROM project.movies m, project.directed dm, project.director d "
    sql += "WHERE m.`Release Date` >= '2023-11-01' "
    sql += "LIMIT 3"

    crsr.execute(sql)
    rows = crsr.fetchall() # want all the outputs
    recentMovies = [] # empty list to put the results into

    # formatting output
    for r in rows: # loop through all the rows of the result to add descriptions
        recentMovies.append({'Title': r[0], 'Genre': r[1], 'Release Date': r[2]})

    return jsonify({'recentMovies': recentMovies}) # return list of movies


## SUGGEST GENRE: user inputs a genre and gets other movies in that genre
@app.route('/getGenre', methods=['POST'])
def getGenre():

    crsr = cursor() # call cursor function

    json = request.get_json()
    genre = json['genre'] # user inputs the genre they want

    # embedded sql: retrieve 3 movies in a specific genre
    # Use parameterized queries to prevent SQL injection
    sql = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
    sql += "FROM project.movies m "
    sql += f"WHERE m.genre = '{genre}' "  # Use %s as a placeholder for the genre
    sql += "LIMIT 3"

    crsr.execute(sql)
    rows = crsr.fetchall() # want all results
    movies = [] # empty list for results

    # formatting output
    for r in rows: # loop through all the rows of the result to add descriptions
        movies.append({'Title': r[0], 'Genre': r[1], 'Release Date': r[2]})

    # returns list of movies, isGenre is a boolean value to trigger a display message
    return jsonify({'movies': movies, 'isGenre': True}) 


## FUNCTION TO CLEAR INPUT BOXES: for genre search
@app.route('/resetInput', methods=['POST'])
def resetGenre():
    genre = '' # reset to empty
    isGenre = False # takes away the display message

    return jsonify({'genre': genre, 'isGenre': isGenre}) # returns empty genre and false value


## SUGGEST DIRECTOR: user inputs a director's last name and gets other movies by the director
@app.route('/getDirector', methods=['POST'])
def getDirector():

    crsr = cursor() # calls cursor function

    json = request.get_json()
    director = json['director'] # user input

    # embedded sql: retrieve the ID of this director
    sql = "select ID "
    sql += "from project.director "
    sql += f"where `last name` = '{director}'"
    crsr.execute(sql)
    dID = crsr.fetchone()[0] # only should have 1 ID

    # embedded SQL: retrieve movies by this director
    sql2 = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
    sql2 += "FROM project.movies m, project.directed dm, project.director d "
    sql2 += f"WHERE dm.`director ID` = d.ID AND dm.`movie ID` = m.ID and d.ID = {dID}"
    crsr.execute(sql2)
    rows = crsr.fetchall() # want all the results
    dirMovies = [] # empty list for the results

    # formatting output
    for r in rows: # loops through all the rows of the result to trigger a display message
        dirMovies.append({'Title': r[0], 'Genre': r[1], 'Release Date': r[2]})

    # returns the movies, isDir is a boolean value to trigger display message
    return jsonify({'dirMovies': dirMovies, 'isDir': True}) 


## FUNCTION TO CLEAR INPUT BOXES: for director search
@app.route('/resetDir', methods=['POST'])
def resetDir():
    director = '' # reset to empty
    isDir = False # takes away the display message

    return jsonify({'director': director, 'isDir': isDir}) # return empty director name and false


########## LOGIN FUNCTION: check if users are new or for them to sign up
@app.route('/login', methods=['POST'])
def login():
## first screen for users, either existing user or new
    crsr = cursor() # call cursor function  

    json = request.get_json()
    userID = json['userID'] # from the user input

    # embedded sql code: get the user information for this user ID
    sql = "select ID, `first name`, `last name` "
    sql = sql + "from project.users "
    sql = sql + "where ID = %s"

    output = crsr.execute(sql, [userID])

    # if user exists, react will take them to -> getWatched function
    # if user doesn't exist, react will have them enter their info -> addUser function
    if crsr.rowcount == 1: # user exists
        rows = crsr.fetchall()

        # returns userID to use in other functions, found is boolean value that will trigger welcome message
        return jsonify({'userID': userID, 'found': True, 'userName': rows[0][1]}) # returns the first name
    else: # user is new, so make account and put that into the Users table
        return jsonify({'user':'no user', 'found':False, 'isUser': True})

# runs locally
if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=5000) 