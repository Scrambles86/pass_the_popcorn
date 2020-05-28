<h1>Pass The Popcorn</h1>

<p>Pass The Popcorn is my third major project. The original idea behind PTP was that it would be a user to user movie review site. The site would have allowed users to upload an image from the film - preferably the poster - and asks them to fill out a few key details of the film to make reviews as readable as possible for other users.</p>

<p>Whilst this was the original goal, it pivoted slightly through development. The site now operates more as a personal film collection, where users can track their the films that they have seen and log them to a Mongo Database. I still appreciate the idea of having a peer to peer movie review site, but due to the seperate users and databases required, it made more sense to first create a personal collection, and add reviewing and social media elements afterwards.</p>

<p>My hope is that the target audience for this site will end up being extremely broad. The film industry is one of the highest earning indstries in the world, with an almost global appeal - but different genres and eras of films appeal to different people, meaning that the possibility for the addition of new content is almost endless.</p>

<h2>UX</h2>

<h3>User Stories</h3>
<ul>
<li>I am an avid cinema goer, and would like to keep an account of all of the films that I have seen.</li>
<li>I am a Film Studies teacher, and would like to log a database of all the films that I have seen for my students to peruse.</li>
<li>I am a parent looking for recommendations on a good film to watch with my kids</li>
<li>I am a Film Studies student, and would like to make a log of films that I haven't yet seen in order to expand my knowledge</li>
</ul>

<h3>Wireframes</h3>
<ul>
<li><a href="https://imgur.com/JlYk0kQ">Front Page - Desktop</a></li>
<li><a href="https://imgur.com/TouLGr9">Add Review - Desktop</a></li>
<li><a href="https://imgur.com/3FQsaPN">My Page - Desktop</a></li>
<li><a href="https://imgur.com/xWLqmGN">Archive - Desktop</a></li>
<li><a href="https://imgur.com/8khKGsy">Front Page - Tablet</a></li>
<li><a href="https://imgur.com/7KH3QVg">Add Review - Tablet</a></li>
<li><a href="https://imgur.com/ZwqINCv">My Page - Tablet</a></li>
<li><a href="https://imgur.com/qC3KDgP">Archive - Tablet</a></li>
<li><a href="https://imgur.com/It2nwsf">Front Page - Mobile</a></li>
<li><a href="https://imgur.com/PFt2HDz">Add Review - Mobile</a></li>
<li><a href="https://imgur.com/ZwqINCv">My Page - Mobile</a></li>
<li><a href="https://imgur.com/WhhITB8">Archive - Mobile</a></li>
</ul>

<h2>Features</h2>

<h3>Existing Features</h3>

<p>The landing page of PTP contains a navbar and footer that contains links enabling the user to add film reviews on their own page, visit their own page to allow them to post reviews, and visit the archive, which will allow users to browse through film reviews chronologically. The navbar also contains a button to allow users to log in to their account or register for a new account.</p>

<p>On the Add Film page, the user will find a form wherein they can search for a movie using OMDB API - this search will return the poster for every film containing the words sued in the search bar, and posts that data to the users database when chosen. The original plan for this site called for the user to add this information themselves, but this felt like bad UI - it was forcing the user to go to other sites to find this information, which would have made the overall user experience very clunky and laboured.</p>

<p>Clicking 'Add To Collection' opens a modal containing a search bar. When a user searches in this bar, it returns the film posters associated with their search. The user can then click on the poster that they want to add to their database. Once this has been done, the user can fill in the textbox at the bottom of the form with their thoughts on the film and click the add button. This will then return the user to their page, and present them with a card containing all of the information for that film, including the poster.</p>


<h3>Features Left To Implement</h3>

<p>Ideally, I would like to code a version of this site that has full user profile pages, allowing users to read selected information about others and look at their stored collections. I would also like to implement a commenting system, allowing user to comment on each others reviews to create more of a social media type experience.</p>

<p>I would also like to eventually implement full user reviews on each film. It was in the original plan, but was left out for the sake of streamlining and making sure the base elements were working. In future, I would like for users to be able to make each film in their collection into a full blog post containing a review score, and potentially a hyperlink to the film trailer.</p>

<h3>Javascript Functions</h3>

<p>Pass The Popcorn works in conjunction with Bootstrap to allow for cleaner site usage on smaller screens. The pairing of JQuery with Bootstrap allows for the navbar selections to shrink into a burger menu on smaller devices.</p>

<p>Core Javascript has been used to create open and close buttons for the add film modal. In order to break the close button down to be included as a Jinja element, the id of each form has been targeted to display:none if the button is clicked.</p>

<p>Core JS has also been used in the API function, which allows the user to search for films through a database. The JS has been modified so that the results returned to the user are the movie posters, but still posts relevant data to the database. The reason only posters are returned on the search is that this is a much cleaner browsing experience for the user.</p>

<h3>Python & Flask Functions</h3>

<p>Render Template, Redirect, Request, url_for, Session, and Flash are all imported from Flask for use in Python
and Flask functionality. Render template and redirect and used to render the pages on the site, and redirect is used to send the user to certain pages based on certain actions on the page. Url_for is used in a similar way to redirect, but redirects functions to pages that have already been rendered.</p>

<p>Session is used to ensure that users can be logged in and out based on their credentials in the database, and also allows for certain functionalities based on this. Flash has been used to flash messages to the user informing that that objects have been added to their database, or that they have logged in or out.</p>

<p>Python functionality has been used to create a login function, as well as the registering of new users. This function requires fields be filled out in the register form, including a password - which is then checked against itself for authorisation purposes. If the two passwords don't match, the user gets a flash message to say there has been an error. Once the user has registered, their data is stored in the database, but the passwords are hashed by Werkzeug security, so that they remain unknown to anyone aside from the user.</p>

<p>Functionality also exists within Python to allow the users chosen films to be posted to the Mongo database. The function takes the poster, directore, title, year, genre and actor fields from the result provided by the API/JS function and returns the user a card with the poster as the header and all of the information beneath. There is also a delete function should a user decide to remove anything from their database - this function has been attached to the bottom of each film card.</p>

<p>Jinja templates are also heavily deployed throughout the project, particularly for the navbar. These templates have also been used in the cards on the users film collection page to ensure that the correct content is laoded into the correct places.</p>

<h3>Technologies Used</h3>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a></li>
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html">CSS</a></li>
<li><a href="https://getbootstrap.com/">Bootstrap</a></li>
<li><a href="https://jquery.com/">JQuery</a></li>
<li><a href="https://www.javascript.com/">Javascript</a></li>
<li><a href="https://fonts.google.com/">Google Fonts</a></li>
<li><a href="https://www.python.org/">Python</a></li>
<li><a href="https://www.mongodb.com/">MongoDB</a></li>
<li><a href="https://www.omdbapi.com/">OMDB API</a></li>
<li><a href="https://pypi.org/project/Flask/">Flask</a></li>
<li><a href="https://dashboard.heroku.com/login">Heroku</a></li>


</ul>

<h3>Testing</h3>

<p>Pass The Popcorn has been tested on Mozilla Firefox and Google Chrome internet browsers, on both a Macbook Pro and a desktop PC. There are no differences between the two, with the Bootstrap providing compatability between a variety of devices. Pass The Popcorn has also been tested on a Kindle Fire tablet and and iPhone8, with no functionality issues. The code for Pass The Popcorn was written in Virtual Studio Code.</p>

<p>Testing has been done on all the navbar links from each seperate page, and all links are fully functional. All of the app routes redirect to the desired pages upon completion of their desired functions.</p>

<p>All of the Python functions have been tested to ensure that everything correctly posts to the database, and also hashes the passwords when users register. There were a lot of inital problems in having the API/JS function and Python function talk to each other and post film data to the DB. A huge help in solving this was in having the movie data post to a form when chosen, which made it much easier for the Python function to identify the required data.</p>

<h2>Deployment</h2>

<p>Pass The Popcorn was deployed through <a href="https://dashboard.heroku.com/apps/pass-the-popcorn">Heroku</a> from the Github master. There is no difference between the development and deployment version of the site. All of the user and film information is stored on MongoDB and is sent through the Heroku app.</p>

<p>In order to deploy Pass the Popcorn, make sure the following are installed on your IDE (I recommend VSCode or Github) :</p>
<ul>
<li>git</li>
<li>PIP</li>
<li>Python 3</li>
<li>Flask</li>
<li>MongoDB Atlas</li>
</ul>

<p>From the terminal, run the following commands</p>
<ul>
<li>$ git clone https://github.com/Scrambles86/pass_the_popcorn.git</li>
<li>$ pip install --upgrade pip</li>
<li>$ pip install -r requirements.txt</li>
<li>$ python -m flask run</li>
</ul>

<h2>Heroku Deployment</h2>

<p>In order to deply to heroku, you will first need a Heroku account. Once you have one, use the command heroku login in the terminal. Clone the repository and change the directory in your terminal :</p>

<ul>
<li>$ heroku git:clone -a pass_the_popcorn</li> 
<li>$ cd pass_the_popcorn</li>
</ul>

<p>from here you will need to create a requirements.txt file and Procfile in order to ensure that the app runs on Heroku using all the technologies used in Pass The Popcorn. You can do this by running the following commands in your terminal :</p>

<ul>
<li>$ pip freeze --local > requirements.txt</li>
<li>$ echo web: python app.py > Procfile</li>
</ul>

<p>From here, perform and add and a commit and push to heroku master. Once you arrive at the app, you will need to amend the config vars. You can do this in the settings tab. You'll need to change the IP and PORT.</p>

<ul>
<li>IP - 0.0.0.0</li>
<li>PORT - 5000</li>
</ul>

<h2>Acknowledgments</h2>

<p>A huge thank you as always to my mentor, Simen Daehlin, who was instrumental in pushing me through this project, and continues to be a huge source of knowledge</p>

<p>Huge thanks as well to everyone on the Code Institute tutorial team, all of whom I have recieved help from throughout this project. In particular, thanks to <a href="https://github.com/TravelTimN">Tim Nelson</a>, who was a tremendous help in showing me how to correctly wire up the code to the DB.</p>

<p>An additional thanks to Dave Lovejoy, who continues to hold my hand through Javascript and JQuery when I start to get confused - which happens often.</p>

<p><strong>All content in this app is intended for educational purposes only.</strong></p>

<h2>Credits</h2>

<p>The user login and register functions, as well as the register template, are amended versions of a function written by fellow Code Institute student <a href="https://github.com/MiroslavSvec">Miro_alumni</a>, as recommended to me by the tutorial team.</p>

<p>The background image used in this project is a free image from <a href="https://www.pexels.com/">Pexels</a></p>



