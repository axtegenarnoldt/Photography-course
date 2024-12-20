# Photography Course - Coursebooker
<img src="" alt="image of website on different screens">

## Introduciton 
- The Photography Course website is a project with a booking application for users how are interested to book different photography courses.

When you visit the website you can look at different courses, read comments and register on the website. If you are a registerd user and are signed in you can book courses, leave comments and like courses.

The Admin user can create new courses, approve comments and manage bookings.

The site is live here: <a href=""></a>


## Contents
**Table of content:**
- [Photography Course](#photography-course)
    - [Introduction](#introduciton)
- [Contents](#contents)
- [User Experience](#user-experience)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
- [Design](#design)
    - [Colors](#colors)
    - [Flowchart](#flowchart)
- [Features](#features)
    - [Welcome Screen](#welcome-screen)
    - [Photography Course](#photography-course)
    - [Register Screen](#register-screen)
    - [Sign in Screen](#sign-in-screen)
-[Features To Add](#features-to-add)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [CI Python Linter](#ci-python-linter)
    - [WAVE](#wave)
    - [Lighthouse](#lighthouse)
- [Bugs](#bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credit](#credit)

## User Experience

### Site Owner Goals


### User Stories
The project used GitHub as an Agile tool and linked Issues to define User Stories with acceptance criteria. Development of code for these stories was managed using a Kanban board. All User Stories were linked to a 'parent' Epic issue to show how they all supported the overarching goal of the project.

User stories and kanaban board here <a href="https://github.com/users/axtegenarnoldt/projects/3/views/1">User Stories</a>


### Colors
I used ..



## Fetures

### Welcome Screen
<img src="docs/homescreen.png">
The welcome screen displays the navbar, an image of a camera with a text that tells you to explore the different courses.

### Photography Courses
<img src="docs/coursees.png">
On the home screen under the "welcome message" you can find the different photography courses we offer. You can click on them to read more about every course.

### Register Screen
<img src="docs/registerscreen.png">
On the register screen you can see a welcome message for the course booker, instructions on how to register and a link too the sign in page if you alredy have registerd.

### Sign in Screen
<img src="docs/loginscreen.png">
The sign in screen shows a welcome message, a link to the register page incase you don't have an account and the option to sign in.

## Features To Add

Things I like to add .. in the future to give a better user experience.
<ul>
<li> - </li>
<li> - </li>
<li> - </li>
</ul>

## Testing

### Manual Testing

| Test | Step | Result |
|------|------|--------|
| Heroku |Open live site | Live site runs as expected |
| press "r" to view rules | pressed "r" | Shows rules page |
| Press any key to go back to start menu | tested with different keys | Shows start menu |
| Press "p" to play game | Pressed "p" | show's next page |
| Enter name | typing my name and Enter | Starts the game |
| Enter name | Pressing Enter without typing my name | Ask's me to enter my name again |
| Arrowkeys | pressing arrowkeys to control the snake | Snake moves as expected |
| Border | Snake collides with border | Game ends and shows game over screen |
| snakes body | Snake collides with itself | Game ends and shows game over screen |
| Live score | Snake eat's food | Live score updates with +1 |
| New food | Snake eats food | New food shows up in the game area |
| Play again | Press "p" on game over screen | Shows start menu so I can play again |

### CI Python Linter
<img src="docs/pythonlinter.png">
Validation of Python code in <a href="https://pep8ci.herokuapp.com/">CI Python Linter</a> - No errors

### WAVE
<img src="">
Accessability testing at <a href="">Webaim</a> - No errors

### Lighthouse
Tested the website in lighthouse for desktop.

<img src="">

## Bugs
 During the development and testings several bugs were discoverd.

 | Bug | Fixed/Unfixed |
 |-----|---------------|
 |  | Fixed |
 |  | Unfixed |
 |  | Fixed |
 |  | Fixed |
 |  | Fixed |

## Deployment

### Heroku

To the deploy this project i followed the deployment guide from love sandwiches.

Before i deployd i to Heroku i used "pip3 freeze > requirements.txt" to add dependencies that's requierd for the game to work in Heroku.
<ol>
<li> Set up a Heroku account. </li>
<li> On the Heroku dashboard, select create new app.</li>
<li> Choose a name for your app.</li>
<li> Select a region.</li>
<li> Click on "Create app"</li>
<li> Go to settings and go to Config Vars.</li>
<li> Enter CREDS in the key box and in value add the content from the creds.json file, then click the Add button.</li>
<li> Enter PORT in the next key box and 8000 in the value box, then click Add.</li>
<li> Scroll down to the Buildpack, select the python pack and click on save.</li>
<li> select node.js and save. </li>
<li> Make sure the Bulidpack is in the correct order, python first and node.js second. </li>
<li> Scroll up to the top of the page and click on the Deploy tab. </li>
<li> select GitHub as deployment method. </li>
<li> Enter the name of your repository and connect to it. </li>
<li> Scroll down and choose Enable automatic deployments or deploy manually. </li>
<li> When the deployment is done click on view to see your application. </li>
</ol>


## Credit

Lucidcart was made at <a href="https://lucid.co/ ">Lucid</a> and ASCII art are from <a href="https://www.asciiart.eu/text-to-ascii-art">ASCII Art Archive</a>.

| Knowledge about | Source |
| ----------------|--------|
| How to make a snake game using curses: Mision     Codigo youtube tutorial | https://www.youtube.com/watch?v=_IKIkRMfZJA |
| how to make a snake game using curses: Partick Loeber youtube tutorial| https://www.youtube.com/watch?v=M_npdRYD4K0 |
| how to use colors: | https://www.youtube.com/watch?v=JBE4OwdqzQ8 |
| ASCII art | https://www.asciiart.eu/text-to-ascii-art |
| Curses functions | https://docs.python.org/3/library/curses.html |
| How to split lines in python | https://betterstack.com/community/questions/python-how-to-define-multiline-string/ |
