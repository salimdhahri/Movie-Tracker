#################### this file is used to test our embedded sql code ####################

import pymysql
import os


# defining cursor to use in other functions
def cursor():
    # connected to env file with your workbench info
    conn = pymysql.connect(
        host="localhost", user="root", password="Rapgodeminem8*", database="project"
    )
    conn.autocommit(True)
    crsr = conn.cursor()
    return crsr


def login():
    ## first screen for users, either existing user or new
    # future implementation: allow users to enter user ID or name

    crsr = cursor()
    userID = input(
        "For returning users, please enter your user ID. If you're a new user, please enter 0: "
    )
    sql = "select ID "
    sql = sql + "from project.users "
    sql = sql + f"where ID = {userID}"
    output = crsr.execute(sql)
    print(output)

    if crsr.rowcount == 1:  # meaning the user is not new
        print("Welcome back!")
        getWatched(userID)
    else:
        print("No user found. Let's make an account for you!")
        fName = input("Input your first name: ")
        lName = input("Input your last name: ")
        uEmail = input("Input your email address: ")
        sql = "insert into project.users (`First Name`, `Last Name`, `Email`) "
        sql = sql + f"values ('{fName}', '{lName}', '{uEmail}')"
        crsr.execute(sql)
        # userMovie() # some other function that takes them directly to adding to watched list


# function to get the movies that a user have watched and rated
# future implementation: allow the users to change their rating, add a rewatch date, or notes
def getWatched(userID):
    print("Here are the movies you've watched before!")
    crsr = cursor()

    ## concat makes the "first name" & "last name" attributes of Director table as one
    sql = "select m.`Title`, concat(d.`first name`, ' ', d.`last name`), w.`Date Watched`, w.`User Rating` "
    sql = (
        sql
        + "from project.Watched w, project.Users u, project.Movies m, project.director d, project.directed dm "
    )
    sql = (
        sql
        + f"where w.`user ID` = u.ID and w.`movie ID` = m.ID and u.ID = {userID} and dm.`director ID` = d.ID and dm.`movie ID` = m.ID"
    )
    # print(sql)
    crsr.execute(sql)
    # output = crsr.fetchall()
    # print(output)
    rows = crsr.fetchall()
    print(rows)
    # watched = []
    # for r in rows: # formatting output
    #   watched.append({'Title': r[0], 'Date Watched': r[1], 'User Rating': r[2]})
    # print(watched)


## function to add a movie to their "watched" list
## then users will put what date they watched it and their rating
def addMovie():
    crsr = cursor()  # call cursor function

    ## when we make this in react, it will be some kind of interactive list that users click on -> tied to movie ID
    movie = input("Enter the movie you'd like to add to your watched list: ")
    print("Adding the movie: ")
    sql = "SELECT m.Title, concat(d.`first name`, ' ', d.`last name`) as `Directed By`, m.Genre, m.Length, m.`Release Date` "
    sql = sql + "FROM project.movies m, project.director d, project.directed dm "
    sql = (
        sql
        + f"WHERE dm.`director ID` = d.ID and dm.`movie ID` = m.ID and m.ID = {movie}"
    )
    crsr.execute(sql)
    output = crsr.fetchall()
    print(output)


##get the averge rating for a movie
def getRating():
    crsr = cursor()
    movie = input("Enter the movie's rating you want: ")
    sql = "SELECT AVG(`User Rating`)"
    sql += "FROM project.Watched"
    sql += "WHERE ID = {movie}"
    output = crsr.fetchall()

    average_rating = (
        crsr.fetchone()
    )  # source: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchone.html
    if average_rating is None:
        print("No ratings found for the movie (ID: {movieID}).")
    else:
        print("The average rating for the movie (ID: {movieID}) is: {average_rating}")

    print(output)


# def getSuggestions():
## give the user top movies from same genre/director
def getSuggestionsGenre():
    crsr = cursor()

    # Based on genre
    genre = input("Enter your favorite genre to get movie suggestions: ")

    # Use parameterized queries to prevent SQL injection
    sql = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
    sql += "FROM project.movies m "
    sql += "WHERE m.genre = %s"  # Use %s as a placeholder for the genre

    try:
        crsr.execute(sql, (genre))
        output = crsr.fetchall()
        for movie in output:
            title, genre, release_date = movie
            print(f"Title: {title} | Genre: {genre} | Release Date: {release_date}")
    except pymysql.Error as e:
        print(f"Error: {e}")


##################################
# 3 most recent movies (based on release date)
def getSuggestionsRecent():
    crsr = cursor()

    recent = input(
        "Type Recent if you'd like to see recently released movies: "
    )  # Prompt user for input
    if (
        recent.lower() == "recent"
    ):  # Check if the user input matches the expected string
        sql = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
        sql += "FROM project.movies m, project.directed dm, project.director d "
        sql += "WHERE m.`Release Date` >= '2023-11-01' "
        sql += "LIMIT 3"

        try:
            crsr.execute(sql)
            output = crsr.fetchall()
            for movie in output:
                title, genre, release_date = movie
                print(f"Title: {title} | Genre: {genre} | Release Date: {release_date}")
        except pymysql.Error as e:
            print(f"Error: {e}")
    else:
        print(
            "Invalid input. Please type 'Recent' if you'd like to see recently released movies."
        )


## # 3 top movies by the same director (of a user's most recently rated movie?) (will require avg rating calculation)
def getSuggestionsDirector():
    crsr = cursor()
    director = input(
        "Enter director's last name to find similar movies recommendations: "
    )

    sql = "SELECT m.`Title`, m.`Genre`, m.`Release Date` "
    sql += "FROM project.movies m, project.directed dm, project.director d "
    sql += (
        "WHERE dm.`director ID` = d.ID AND dm.`movie ID` = m.ID AND d.`Last Name` = %s"
    )

    try:
        crsr.execute(sql, (director,))
        output = crsr.fetchall()
        for movie in output:
            title, genre, release_date = movie
            print(f"Title: {title} | Genre: {genre} | Release Date: {release_date}")
    except pymysql.Error as e:
        print(f"Error: {e}")


getSuggestionsGenre()
getSuggestionsRecent()
getSuggestionsDirector()
