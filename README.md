# Photography Course
<img src="" alt="image of website on different screens">

## Introduciton 
-

The site is live here: <a href=""></a>


## Contents
**Table of content:**
- [Snake Game](#snake-game)
    - [Introduction](#introduciton)
- [Contents](#contents)
- [User Experience](#user-experience)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
- [Design](#design)
    - [ASCII Art](#ascii-art)
    - [Colors](#colors)
    - [Flowchart](#flowchart)
- [Features](#features)
    - [Welcome Screen](#welcome-screen)
    - [Rules Screen](#rules-screen)
    - [User Name](#user-name)
    - [Main Game](#main-game)
    - [Live Score](#live-score)
    - [Game Over Screen](#game-over-screen)
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
The goal..


### ASCII Art
Both the start screen and game over screen displays ASCII art to make it stand out from the rest of the text in the game.

### Colors
I used ..



## Fetures

### Welcome Screen
<img src="">

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
