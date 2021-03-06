<h1>Pass The Popcorn</h1>

<img src="wireframes/mockup.png"></img>

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
<li>As a user, I expect all of the relevant information to be found for me when I use a search function.</li>
<li>As a user, I expect to be able to edit posts I have made when I have made an error or changed my mind about posting.</li>
<li>As a user, I expect to be prompted on how to proceed with an app when I have logged in.</li>
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

<h4>Languages</h4>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a></li>
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html">CSS</a></li>
<li><a href="https://jquery.com/">JQuery</a></li>
<li><a href="https://www.javascript.com/">Javascript</a></li>
<li><a href="https://www.json.org/json-en.html">JSON</a></li>
<li><a href="https://www.python.org/">Python</a></li>
</ul>

<h4>Libraries</h4>
<ul>
<li><a href="https://getbootstrap.com/">Bootstrap</a></li>
<li><a href="https://fonts.google.com/">Google Fonts</a></li>
<li><a href="https://www.mongodb.com/">MongoDB</a></li>
<li><a href="https://www.omdbapi.com/">OMDB API</a></li>
<li><a href="https://pypi.org/project/Flask/">Flask</a></li>
<li><a href="https://dashboard.heroku.com/login">Heroku</a></li>
</ul>

<h3>MongoDB Data</h3>

MongoDb stores the following types of data for this app :
<ul>
<li>ObjectId</li>
<li>String</li>
<li>Array</li>
<li>Object</li>
<li>Binary</li>
</ul>

<h4>Movie Data Collection</h4>

| Title 	| Key In Collection 	| Data Type 	|
|-	|-	|-	|
| _id 	| _id 	| ObjectId 	|
| Movie Poster 	| movie-poster 	| String 	|
| Movie Title 	| movie-title 	| String 	|
| Movie Director 	| movie-director 	| String 	|
| Movie Year 	| movie-year 	| String 	|
| Movie Actor 	| movie-actor 	| String 	|
| Movie Genre 	| movie-genre 	| String 	|
| Reviewed By 	| reviewed-by 	| String 	|


<h4>User Collection</h4>

| Title 	| Key In Collection 	| Data Type 	|
|-	|-	|-	|
| _id 	| _id 	| ObjectId 	|
| Username 	| username 	| String 	|
| Email 	| email 	| String 	|
| Password 	| password 	| Binary 	|

<p>Examples of these schemas as they are used in the database can be found <a href="https://github.com/Scrambles86/pass_the_popcorn/tree/master/data/schemas">here.</a></p>

<h3>Testing</h3>

<p>Pass The Popcorn has been tested on Mozilla Firefox and Google Chrome internet browsers, on both a Macbook Pro and a desktop PC. There are no differences between the two, with the Bootstrap providing compatability between a variety of devices. Pass The Popcorn has also been tested on a Kindle Fire tablet and and iPhone8, with no functionality issues. The code for Pass The Popcorn was written in Virtual Studio Code.</p>

<p>Testing has been done on all the navbar links from each seperate page, and all links are fully functional. All of the app routes redirect to the desired pages upon completion of their desired functions.</p>

<p>All of the Python functions have been tested to ensure that everything correctly posts to the database, and also hashes the passwords when users register. There were a lot of inital problems in having the API/JS function and Python function talk to each other and post film data to the DB. A huge help in solving this was in having the movie data post to a form when chosen, which made it much easier for the Python function to identify the required data.</p>

<h3>Specific Function Testing</h3>

<ul>
<li><h3>Add User Function</h3></li>

<h4>Planning Stage</h4>
<p>The first function created for this app in relation to the database was the add user and register function. The reason this was the inital creation is because I was keen for this app to be a personal diary, so being able to log in and out was essential.</p>

<h4>Implementation</h4>
<p>As this was the first function that I created in Python, I ran into numerous blocks. The tutor team proved vital here, and point me in the direction of a function created by <a href="https://github.com/MiroslavSvec">Miro_alumni</a>, which proved an invaluable learning tool. From checking through this function, I was able to ascertain numerous areas wherein I was making errors - perhaps most importantly was that I was unaware of the session function the can be imported from Flask. I was comfortable with creating functions that return users to the correct templates, but was unable to figure out how to define a specific user, so learning about session helped immeasurably.</p>

<h4>Testing</h4>
<p>In addition, Miro_alumni's function pointed out several things I hadn't even considered - how the site should behave if a user is logged in, what it should do if the user isn't registered, and how to check that passwords matched. I had initially attempted to log hashed passwords with bcrypt, but founc werkzeug security to be a much easier tool to import and work with. From looking at the function sent to me, I was able to discern how to properly apply the checking of hashed passwords.</p>
</ul>

<ul>
<li><h3>Add Film Function</h3></li>

<h4>Planning Stage</h4>
<p>Setting up the add user function was vital in showing me how to talk to the database from my code. As a result, the add film function was comparatively easy to set up, but still presented issues - namely that I could post to the database, but I wasn't getting any information back.</p> 

<h4>Implementation</h4>
<p>Tim Nelson on the tutor team was an immense help here, and noted that most of my problem were being caused by syntactical issues - my parameters all contained hyphens instead of underscores, and hyphens do not work with PyMongo. Once he noted this and all of the issues were corrected, he also helped me with how to incorporate the user into this function so that it only rendered the information that they themselves have posted on their page, as opposed to returning everything that is logged to the database.</p>

<h4>Testing</h4>
<p>Once testing began on this function, there were no issues thanks to the removal of the syntactical errors.</p>
</ul>

<ul>
<li><h3>Delete Function</h3></li>

<h4>Planning Stage</h4>
<p>I needed a function that simply removed the film from the user's database. This was the simplest of the functions to implement, as it was able to act purely as a function without a need for a page rendering, so the function was simply attached to an icon on the user's film cards.</p>

<h4>Implementation</h4>
<p>Comparatively, there were few issues with the delete function beyond syntax problems. I had made the inital assumption that adding the delete button to the card would be enough for PyMongo to know to remove the film. It was pointed out to me that whilst everything to get the function working was technically in place, it wasn't being passed an object id, and therefore wasn't firing off correctly.</p>
</ul>

<ul>
<li><h3>Edit Function</h3></li>

<h4>Planning Stage</h4>
<p>I wanted the edit function to present as a simple popup modal - there is only one field that the user is able to edit, so I felt it was important to keep this clean and easy. Additionally, I wanted to make sure that the user's original information appeared within this modal, eliminating the need for a total re-write if all they are doing is editing spelling errors.</p>

<h4>Implementation</h4>
<p>The edit function was built after the add and delete functions, as it was important for me to check that the data was arriving in and exiting from the database correctly before I started to play around with it. In it's initial stage, I was unable to get this function working as I was approaching it in a similar manner to the previous two functions, and trying to get all of the information crammed into the same function.</p> 

<h4>Testing</h4>
<p>Upon speaking to the tutors, I was advised that I needed to split this function and create two instances - one where the information for updating it indentified, and one where that information is then updated. After testing this, I found that the function was posting to the database, but in doing so was deleting the original database entry. Instead of an updated review form, I was instead getting a databse entry containing only the updated review, and the card itself was disappearing from the user's page. After checking this with the tutors once more, I found that I was missing the $set operator from the function - once this was added in the edit function began behaving correctly.</p>
</ul>

<h2>Deployment</h2>

<p>Pass The Popcorn was deployed through <a href="https://dashboard.heroku.com/apps/pass-the-popcorn">Heroku</a> from the Github master. There is no difference between the development and deployment version of the site. All of the user and film information is stored on MongoDB and is sent through the Heroku app.</p>

<h3>Cloning PTP From Github</h3>

<p>You will need the following languages and toolkits installed :</p>
<ul>
<li>git</li>
<li>PIP</li>
<li>Python 3</li>
<li>Flask</li>
<p>You will also need an account with <strong>MongoDB Atlas</strong></p>
</ul>


<p> 1 - From the terminal, run the following command :</p>

```
git clone https://github.com/Scrambles86/pass_the_popcorn
```

<p>2 - From your terminal, navigate to this folder.</p>
<p>3 - In your terminal, run the following command : </p>

```
python3 -m .venv venv
```

<p>4 - Use the following command in order to initilise the environment : </p>

```
.venv\bin\activate 
```

<p>5 - Run the following command in order to install the libraries relevant to this app : </p>

```
pip3 -r requirements.txt
```

<p>6 - You should then make sure to create an <strong>env.py</strong> file, where you can set a <strong>SECRET_KEY</strong>, as well as link to your <strong>MONGO_URI</strong></p>

<p>7 - Run the following command in your terminal in order to run the app : </p>

```
Python3 app.py
```

<h2>Heroku Deployment</h2>

<p>1 - In order to deply to Heroku, you will first need a Heroku account. Once you have one, use the command heroku login in the terminal.</p>

<p>2 - From here, create your <strong>requirements.txt</strong> file by entering the following into the terminal :</p>

```
pip3 freeze > requirements.txt
```

<p>3 - Then create your <strong>Procfile</strong> by entering the following into the terminal : </p>

```
echo web: python app.py > Procfile
```

<p>4 - Push these files to your repository</p>

<p>5 - From your Heroku dashboard, create a new app.</p>

<p>6 - Make sure you set your delpoyment method - you can do this by clicking on the button marked Deployment Method. In this instance, you will set this to Github</p>

<p>7 - Go to the settings tab and click the button marked Config Vars. From here you will need to set the following :</p>

```
IP - 0.0.0.0
```

```
PORT - 5000
```

```
SECRET_KEY - 'my_secret_key'
```

```
MONGO_URI - mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
```

<p>8 - Back on the dashboard, click the <strong>deploy</strong> button.</p>

<h2>Acknowledgments</h2>

<p>A huge thank you as always to my mentor, <a href="https://github.com/Eventyret">Simen Daehlin</a>, who was instrumental in pushing me through this project, and continues to be a huge source of knowledge</p>

<p>Huge thanks as well to everyone on the Code Institute tutorial team, all of whom I have recieved help from throughout this project. In particular, thanks to <a href="https://github.com/TravelTimN">Tim Nelson</a>, who was a tremendous help in showing me how to correctly wire up the code to the DB.</p>

<p>An additional thanks to Dave Lovejoy, who continues to hold my hand through Javascript and JQuery when I start to get confused - which happens often.</p>

<p><strong>All content in this app is intended for educational purposes only.</strong></p>

<h2>Credits</h2>

<p>The user login and register functions, as well as the register template, are amended versions of a function written by fellow Code Institute student <a href="https://github.com/MiroslavSvec">Miro_alumni</a>, as recommended to me by the tutorial team.</p>

<p>The background image used in this project is a free image from <a href="https://www.pexels.com/">Pexels</a></p>



