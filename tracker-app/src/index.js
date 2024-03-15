// APP FILE
// Includes the react functions
// Referenced Pete's Software Certification Modules for implementation of Flask and React, in particular Modules 4 and 6

/////////////////// IMPORTING LIBRARIES ///////////////////

import React from 'react'; // react library from javascript
import ReactDOM from 'react-dom/client'; // to manage DOM elements
import './index.css'; // to format what the site looks like, and tables for result displays
import axios from 'axios'; // axios library from javascript to interact with node.js

// Main component
class Main extends React.Component {
    // construction functions
    constructor() {
        super()
        // Setting the initial states: no user, user not located in table, etc.
        this.state = {userID: '', userName: '', newUser: '', found: false, fName: '', lName: '', email: '', added: false, rows:[], isUser: false, movies:[], title: '', date: '', rating: '', addedMovie: false, recentMovies: [], genre: '', isGenre: false, director: '', isDir: false, dirMovies: []}
        this.urlbase = 'http://127.0.0.1:5000'
        //this.urlbase = 'https://flask-service.h11219crb8qqc.us-west-2.cs.amazonlightsail.com/'
    }

    /////////////////// FUNCTIONS FOR THE INPUT TEXTS/BUTTONS ///////////////////
    onLoginChange(e) {
        //Keep track of the login value
        this.setState({...this.state, userID: e.target.value}) // holds e as the changed object (userID)
    }

    onfNameChange(e) {
        //Keep track of the login value
        this.setState({...this.state, fName: e.target.value}) // holds e as the changed object (user first name)
    }

    onlNameChange(e) {
        //Keep track of the login value
        this.setState({...this.state, lName: e.target.value}) // holds e as the changed object (user last name)
    }

    onemailChange(e) {
        //Keep track of the login value
        this.setState({...this.state, email: e.target.value}) // holds e as the changed object (user email)
    }

    onTitleChange(e) {
        //Keep track of the login value
        this.setState({...this.state, title: e.target.value}) // holds e as the changed object (title)
    }

    onDateChange(e) {
        //Keep track of the login value
        this.setState({...this.state, date: e.target.value}) // holds e as the changed object (date)
    }

    onRatingChange(e) {
        //Keep track of the login value
        this.setState({...this.state, rating: e.target.value}) // holds e as the changed object (rating)
    }

    onGenreChange(e) {
        //Keep track of the login value
        this.setState({...this.state, genre: e.target.value}) // holds e as the changed object (genre)
    }

    onDirChange(e) {
        //Keep track of the login value
        this.setState({...this.state, director: e.target.value}) // holds e as the changed object (director)
    }
    
    /////////////////// OTHER FUNCTIONS ///////////////////
    // login function
    login() {
        const {userID, userName, found, isUser} = this.state // set as initial states
        var url = '/login' // also in server.py
        // Store the user's name in a JSON object and boolean values that trigger different welcome messages
        const body = {'userID' : userID, 'userName': userName, 'found': found, isUser: isUser}
        // We're sending JSON data to our server
        const headers = { "Content-Type": "application/json" }
        // Configuration information for the server
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        // Make the request
        axios(config).then((resp) => {
            //When this completes, the response from the server has data
            this.setState({...this.state, 
                userID: resp.data['userID'], // response data from the server
                userName: resp.data['userName'],
                found: resp.data['found'],
                isUser: resp.data['isUser']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // addUser function using their first name, last name, and email
    addUser(){
        const {newUser, fName, lName, email, added, userID} = this.state
        var url = '/adduser'
        const body = {'fName': fName, 'lName': lName, 'email': email, 'newUser': newUser, 'added': added, 'userID': userID}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            // what we get back from the server:
            this.setState({...this.state, 
                newUser: resp.data['newUser'],
                added: resp.data['added'],
                userID: resp.data['userID']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // watchedList, connected with getWatched()
    watchedList(){
        const {userID, watched} = this.state
        var url = '/watched'
        const body = {userID: userID, watched: watched}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state, 
                rows: resp.data['Watched'],
                //user: resp.data['users']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // addMovie
    // UNFINISHED
    addMovie(){
        const {userID, title, date, rating, addedMovie} = this.state
        var url = '/addmovie'
        const body = {userID: userID, title: title, date: date, rating: rating, addedMovie: addedMovie}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            //debugger
            this.setState({...this.state, 
                addedMovie: resp.data['addedMovie'],
                title: resp.data['title']
            })
        }).catch(error => {
            console.log(error)
        })

    }
    // resetInput: clears textboxes for adding a movie
    resetInput(){
        //const {} = this.state
        var url = '/resetInput'
        const body = {}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state,
                title: resp.data['title'],
                date: resp.data['date'],
                rating: resp.data['rating'],
                addedMovie: resp.data['addedMovie']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // recentMovies
    getRecentMovies(){
        //const {} = this.state
        var url = '/recentmovies'
        const body = {}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            //debugger
            //When this completes, the response from the server has the count data
            this.setState({...this.state, 
                recentMovies: resp.data['recentMovies']
            })
        }).catch(error => {
            console.log(error)
        })

    }

    // getGenre: get movies from the genre user wants
    getGenre(){
        const {genre} = this.state
        var url = '/getGenre'
        const body = {genre: genre}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state,
                movies: resp.data['movies'],
                isGenre: resp.data['isGenre']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // resetGenre: clears textboxes searching a genre
    resetGenre(){
        //const {} = this.state
        var url = '/resetInput'
        const body = {}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state,
                genre: resp.data['genre'],
                isGenre: resp.data['isGenre']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // getDirector: get movies from the director last name that user wants
    getDirector(){
        const {director} = this.state
        var url = '/getDirector'
        const body = {director: director}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state,
                dirMovies: resp.data['dirMovies'],
                isDir: resp.data['isDir']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    // resetDir: clears textboxes searching a director
    resetDir(){
        //const {} = this.state
        var url = '/resetDir'
        const body = {}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state,
                director: resp.data['director'],
                isDir: resp.data['isDir']
            })
        }).catch(error => {
            console.log(error)
        })
    }

    /////////////////// RENDER FUNCTION ///////////////////
    render() {
        const {userName, userID, found, fName, lName, email, added, newUser, rows, isUser, movies, title, date, rating, addedMovie, recentMovies, genre, isGenre, director, isDir, dirMovies} = this.state // initial states
        return (
            <div className='Main'> {/* main  div tag*/}
                {/* Welcome page */}
                <p>Welcome!</p> 
                <p>For returning users, please enter your user ID below:</p>
                <p>
                    {/* have user put in their userID for login */}
                    <span>User ID: </span><input value={userID} onChange={this.onLoginChange.bind(this)}/>
                    <button onClick={this.login.bind(this)}> Login</button>
                </p>

                {/* User with existing account*/}
                {(found === true) && (userName.length > 0) && // makes sure that there is a user in the json object
                <div>
                    {/* Welcome back message */}
                    <p><b><span>Welcome back {userName}!</span></b></p>

                    {/* Show watched list*/}
                    <p><button onClick={this.watchedList.bind(this)}>See my watched list</button></p>

                    {/* Add movie */}
                    <p><b><span>Add movies to my Watched List</span></b></p>
                    {/* User input title */}
                    <span>Movie Title: </span><input value={title} onChange={this.onTitleChange.bind(this)}/>
                    {/* User input date */}
                    <span>Date Watched (YYYY-MM-DD): </span><input value={date} onChange={this.onDateChange.bind(this)}/>
                    {/* User input rating */}
                    <span>Rating (1-5): </span><input value={rating} onChange={this.onRatingChange.bind(this)}/>
                    <button onClick={this.addMovie.bind(this)}>Confirm</button>

                    {/* Add movie confirmation message */}
                    {(addedMovie === true) &&
                    <div>
                        <span>Added {title} to your Watched List!</span>
                        <button onClick={this.resetInput.bind(this)}>Add another movie</button>
                    </div>
                    } {/* closes addedMovie... */}

                    {/* Get suggestions*/}
                    <p><b><span>Get movie suggestions</span></b></p>
                    <span>More movies in this genre: </span><input value={genre} onChange={this.onGenreChange.bind(this)}/>
                    <button onClick={this.getGenre.bind(this)}>Enter</button>

                    {/* Output movies in the genre users wanted */}
                    { movies.length > 0 && (isGenre === true) && (
                        <div>
                        <p><span>Here are some other {genre} movies!</span></p>
                        <table className="genre-table">
                        <thead>
                            <tr>
                            <th>Title</th>
                            <th>Genre</th>
                            <th>Release Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {movies.map((r, index) => (
                            <tr key={index} className={(index % 2 === 0) ? 'even-row' : 'odd-row'}>
                                <td>{r.Title}</td>
                                <td>{r.Genre}</td>
                                <td>{new Date(r['Release Date']).toLocaleDateString()}</td>
                            </tr>
                            ))}
                        </tbody>
                        </table>
                        <button onClick={this.resetGenre.bind(this)}>Search another genre</button>
                    </div>
                    )
                    }
                    <p></p>
                    {/* movies by a specific director */}
                   <span>See movies by this director (enter last name): </span><input value={director} onChange={this.onDirChange.bind(this)}/>
                    <button onClick={this.getDirector.bind(this)}>Enter</button>
                    {/* Output movies by the director users wanted */}
                    { dirMovies.length > 0 && (isDir === true) && (
                        <div>
                        <p><span>Here are some other movies directed by {director}!</span></p>
                        <table className="dir-table">
                        <thead>
                            <tr>
                            <th>Title</th>
                            <th>Genre</th>
                            <th>Release Date</th>
                            </tr>
                        </thead>
                        <tbody>
                            {dirMovies.map((r, index) => (
                            <tr key={index} className={(index % 2 === 0) ? 'even-row' : 'odd-row'}>
                                <td>{r.Title}</td>
                                <td>{r.Genre}</td>
                                <td>{new Date(r['Release Date']).toLocaleDateString()}</td>
                            </tr>
                            ))}
                        </tbody>
                        </table>
                        <button onClick={this.resetDir.bind(this)}>Search another director</button>
                    </div>
                    )
                    }
                    
                    
                    {/* output 3 recent movies */}
                    <p><button onClick={this.getRecentMovies.bind(this)}>See recent movies</button></p>


                </div>
                }{/* closes found... */}

                {/* User needs to make an account */}
                {(isUser === false) &&
                <div>
                    <p>For new users, please enter your information below to make an account:</p>
                        <p><span>First name: </span><input value={fName} onChange={this.onfNameChange.bind(this)}/></p>
                        <p><span>Last name: </span><input value={lName} onChange={this.onlNameChange.bind(this)}/></p>
                        <span>Email: </span><input value={email} onChange={this.onemailChange.bind(this)}/>
                        <p><button onClick={this.addUser.bind(this)}> Confirm</button></p>
                </div>
                } {/* closes isUser... */}
                
                {/* Welcome message to new user */}
                {(added === true) && (newUser.length > 0) && // makes sure that user was added successfully
                    <div>
                        <p><span>Welcome {newUser}!</span></p> {/* Welcome message if added successfully*/}
                        <p><span>Your user ID is: {userID}</span></p>
                        <p><span>Please sign in above to start adding movies to your list!</span></p>
                    </div>
                } {/* closes added... */}

                {/* Output movies in a user's watched list, formatted in a table */}
                {rows.length > 0 && (
                    <div>
                    <table className="movie-table">
                      <thead>
                        <tr>
                          <th>Title</th>
                          <th>Date</th>
                          <th>Rating</th>
                        </tr>
                      </thead>
                      <tbody>
                        {rows.map((r, index) => (
                          <tr key={index} className={(index % 2 === 0) ? 'even-row' : 'odd-row'}>
                            <td>{r.Title}</td>
                            <td>{new Date(r['Date Watched']).toLocaleDateString()}</td>
                            <td>{r['User Rating']}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                    )
                } {/* closes watched list */}

                {/* Output 3 recent movies */}
                { recentMovies.length > 0 && (
                    <div>
                    <p><span>Here are three of the most recently released movies!</span></p>
                    <table className="recent-table">
                      <thead>
                        <tr>
                          <th>Title</th>
                          <th>Genre</th>
                          <th>Release Date</th>
                        </tr>
                      </thead>
                      <tbody>
                        {recentMovies.map((r, index) => (
                          <tr key={index} className={(index % 2 === 0) ? 'even-row' : 'odd-row'}>
                            <td>{r.Title}</td>
                            <td>{r.Genre}</td>
                            <td>{new Date(r['Release Date']).toLocaleDateString()}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )
                } {/* closes recent movies list */}
            
            </div> // closes main div

        ) // closes return function
        
    } // closes render function

} // closes main component

// interacting with the root
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);