# Angus Friel

## Project-Name: Damn The Torpedos

![Responsive](./assets/images/battleship.png)

[View Deployed Site Here](https://damn-the-torpedos.herokuapp.com/)

## Features
The game starts by displayig the rules for the player and then asks the players name. The game then displays a welcome message for the player.
![Game Start](./assets/images/features1.png)

After this, the game askes the player to guess and row and column of the computers ship in order to fire a torpedo at that location. Once the tordepdo has been fired the board is updated to display if the torpedo was a miss or a hit.

![Game Start](./assets/images/features2.png)

![Game Start](./assets/images/features3.png)

Once all attempts have been taken or if the player or tjhe computer hits all the oponants ships the game is then over
![Game Start](./assets/images/features4.png)

### Game Rules
The rules of the game are displayed at the start of the game. THey are the following: 

Damn The Torpedos!!!
Game rules are as follows:

    i) Destroy your enemies ships.
    ii) Each row uses a coordinate system of (0,9) there are ten rows.
    iii) Inputs must use numbers between(0,7) for both the row and the column. Beginning at (0, 0).
    iv) Water is represented by ~. Misses are represented by X. Hits are represented by # and your ship is represented by S.
    v) You ten attempts to destroy the enemy target.
    vi) Enjoy yourself.

## Testing
During testing I ran into some problems with entering a letter or blanck space. This took some time to over come. By using isdigit to check to see if the user has entered a digit along with checking to see if the user has entered the correct coordinantes within the boards range, this was the goal of this error handling. I also incorparated a print statement to tell the user that they have entered the wrong details. Wether it was not a digit or if a ship was of course of the board, or if there was already a ship in that location. Then once they have entered the correct details a success message was displayed with the number of tuirns they have to enter all 8 ships. 

Below is a copy of the code I used for this error handling:

![Errors](./assets/images/errors_handling.png)

![Errors](./assets/images/errors_handling1.png)

## Bugs
 There was a lot of bugs in this program that took me a while to over come. But once I had them sorted by elminating them one by one in terminal window in GitPod, I had zero issues in Pep8 online checker. 
 Below is a list of some of the issues I was encountering. The main problem I had was name convention for global variables and varibles within a function. Trying to pass this information from one to the other to update the computers and players board. But I overcame this by creating a function that once its completed it then later passes this information back to the global variable. 

![Errors](./assets/images/errors1.png)

![Fixed](./assets/images/compo_board.png)

![Pep8](./assets/images/Pep.png)

Sadly, there is one bug I can not get rid of. But it does not show up in Pep8 only in the terminal of GitPod.

![One more bug](./assets/images/bug.png)

![Where its coming from](./assets/images/bug1.png)

## Technologies used
The technologies used for the contruction of this site are as follows: 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - The game itself is written in python and held in the run.py file
* [Heroku](https://dashboard.heroku.com/apps) - Heroku was used to delopy the website as python is a backend language and the game needed a terminal to dsiplay the game
* [GitPod](gitpod.io) - This was used as an IDE, or the Intergrated Development Area, where the HTML, CSS and JavaScritp where all written in the required file types in oder to display the website. 
* [GitHub](https://github.com/) - this was used to host the website, so it is viewable to the public.

## Deployment

This website was contructed in GitPod and deplopyed using Github and Heroku. The steps taken to deploy this website from its [GitHub Repository](https://github.com/Ajfriel86/DamnTheTorpedoes) are as follows: 

* Log into GitHub
* Go to the list of repositories on the left-hand side of the screen.
* Click on the repository - Ajfriel86/DamnTheTorpedoes
* Choose the settings tab froim the menu items across the top of the page; it is the ninth choice and last option on the menu items.
* Once the settings page has loaded scroll down to GitHub Pages.
* In the source section, choose the master branch.
* On selecting this the page is automatically refreshed and the website is deployed.
* A link to the website is then diplayed, this is the deployed websites website address.   

The steps taken to delpoy this via heroku are as follows:
* Create an account on heroku or login to your perviously made account.
* Add a new app.
* Add the python buildpack firstly, then add the NodesJs buildpack.
* I decided to used an automatic update with my application and proceeded with manuel to create the enviorment it displays on.
* After this the application is Tested to see if it works

## Credits
### Content
The content of this website were written by Angus Friel. 

### Code
 The code in this project was constructed by myself. It is a combuination of what I have learned here at The Code Institute, from perevious course, studying for my MTA: Introduction to programing using Python, and from my job at SAP. The inspriation for the game was taken from project example idea 2 - build a battle shipgame. 

### Acknowledgements

A trutorial that guided me through of build for this game:
[Python Battleships](https://coderspacket.com/battleship-game-in-python)

After this tutorial I incorparated my own way of constructing the finished product. I also had help from my mentor, Brian Macharia. As well as tutor support via the code institute. Everyone involved help me over come obstacles throughout this prject and I am very greatful for their time and help. 

#### Disclaimer
The content of this Website is for educational purposes only.