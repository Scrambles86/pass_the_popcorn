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


<h3>Features Left To Implement</h3>

<p>Ideally, I would like to code a version of this site that has full user profile pages, allowing users to read selected information about others and look at their stored collections. I would also like to implement a commenting system, allowing user to comment on each others reviews to create more of a social media type experience.</p>

<p>I would also like to eventually implement full user reviews on each film. It was in the original plan, but was left out for the sake of streamlining and making sure the base elements were working. In future, I would like for users to be able to make each film in their collection into a full blog post.</p>

<h3>Javascript Features</h3>

<p>Pass The Popcorn works in conjunction with Bootstrap to allow for cleaner site usage on smaller screens. The pairing of JQuery with Bootstrap allows for the navbar selections to shrink into a burger menu on smaller devices.</p>

<p>Core Javascript has been used to create open and close buttons for the add film modal. In order to break the close button down to be included as a Jinja element, the id of each form has been targeted to display:none if the button is clicked.</p>

<p>Core JS has also been used in the API function, which allows the user to search for films through a database. The JS has been modified so that the results returned to the user are the movie posters, but still posts relevant data to the database. The reason only posters are returned on the search is that this is a much cleaner browsing experience for the user.</p>

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

<p></p>
