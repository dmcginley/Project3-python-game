# Project 3 - Battleship game
***A terminal base Battleship game written in Python.***

&nbsp;

Site URL:

Repository for the project: https://github.com/dmcginley/Project3-python-game

Live website: https://project3-python-game.herokuapp.com/

## About the Project



![Battleship game image](readme_img/game.png "the battleship game in the terminal")

The Battleship game was developed as a one player game, (one player vs the computer).

It is a version of the classic board game Battleship from Milton Bradley.

The game is deployed on Heroku and is terminal-based for user interaction.

## Table of contents

&nbsp;

## Wireframe

- landscape not portrait

## Who is this website for

- For casual gamers




## User Stories

&nbsp;

*"As a user, I want to be able to play a Battleship game in the terminal like the old style game where I can call out
the coordinates link 'B1' to try and hit a ship."*

Acceptance criteria:

- Chart terminal based game.

- Use a coordinates method from 1 to 10, and a to j .

&nbsp;

*"As a user, I would like a clear message to tell me whether a ship has been hit or missed, so I can see what action has
occurred.*

Acceptance criteria:

- Print a message to give clear feedback to user.

&nbsp;

*"As a user, I want color on the board so I can quickly see what has happened so that the game feels more interactive."*

Acceptance criteria: 

- Add color to different events on the grid.

- Have 'Hit' show as red, and 'Miss' show as white in color.

&nbsp;

*"As a user, I want different character to distinguish between hitting a boat and hitting water, so I can see where I hit on the board."* 

Acceptance criteria:

- Use 'X' character for hit, and '!' character for miss.

&nbsp;

*"As a user, I want an error message if I enter the wrong coordinates, such as: A4B or B22, so that I can see I if I mistyped the coordinates."*

Acceptance criteria: 

- Give an error message back if the user inputs coordinates outside the given parameter. 

- Also prompted correct coordinates by giving an example e.g. D 4.

&nbsp;


*"As a user, I want....
so that I can....."*

Acceptance criteria:

-
-

&nbsp;

*"As a user, I want....
so that I can....."*

Acceptance criteria:

-
-

&nbsp;

- *"As a user, error message if I miss the board
- *"As a user, error message if I enter the wrong coordinates

<p>&nbsp;</p>


## Technologies Used

- **PyCharm** - IDE for Python
- **GitHub**
- **Heroku**

### The Code

- **Python3**

### Libraries used

- [colored 1.4.3](https://pypi.org/project/colored/) ~ Simple library for color and formatting to the terminal.


## Features

- Ability to place ships randomly for player and computer.
	- Collision detection so neither I nor the computer can place a ship on top of another.
	- Edge detection so that you cant place a ship over the edge of the boundary.
- Can set board size from 5 x 5 up to 10 x 10 - smaller board leads to a quicker game.
- Try to hit a ship by giving coordinates like: A 3.
- Shows whether you hit a ship or not by displaying a X or exclamation mark (!) on the grid.
- Print out the result of the player's move or of the computer's move, e.g. "D 3 - Miss!", or "D 4 - Hit! You sunk my Battleship"
- Correctly detect game over.


## Files & classes

There are 7 files:

- **ship.py** ~ *the ships properties*
	- class Ship

- **place_ship.py** ~ *object to tell if ships could be placed*
	- class PlacementResult
	- class NoOverlap
	- class Overlap

- **ocean_grid.py** ~ *my grid space.*
	- class OceanGrid

- **target_grid.py** ~ *my view of computer grid space.*
	- class TargetGrid

- **result.py** ~ *the outcome of a hit or miss.*
	- class Result
	- class Miss
	- class Hit

- **game.py**
	- class Game:


- **run.py**



## Color Choices
I chose universally understood colors for each element on the board:

- The Sea is blue
- The ships are green
- A Hit is red
- A Miss is white

## Accessibility

As well as colors the different elements of the game have different characters used, so the player isn't relaying on just color to view the different outcomes on the board, (e.g. ~X!).

Text is also printed out with every move to give a clear feedback to the player.


## Testing

*All tested in the terminal and also on Heroku.*

### Validator Testing

- **Python**
  <https://jshint.com/>

  ![image of jshint results](readme-images/js-valid.png)


### Manual Testing

*...and how I went about it.*

- Played through the game
- I entered bad coordinates to check that it failed as expected


**Code that prints back each area the ship is placed on**

            for i in range(0, ship.length):
                print(f"CHECK v: {row_start + i},{column_start}")
                if self.grid_data[row_start + i][column_start] != OceanGrid.OCEAN_SPACE:
                    # collision with another ship
                    return False


![loop check for ship placement](readme_img/error1.png "image of code of loop check")

## Error Handling

- I implemented it to show an error when you would upload an image, as before that PapaParse would still parse the image
  into an array, so it wouldn't catch the error,

- I also set a limit of two columns so you couldn't upload a blank file.




## Deployment TODO:

Deployed using [Heroku](https://www.heroku.com)

- App already created
- Installed Heroku in the terminal 
- Run the command: heroku login -i
- login with my username & password
- Then run the following command: heroku git:remote -a 


- heroku git: remote -a project3-python-game
- In pycharm terminal enter: git push heroku main



Once everything compiled & ran corectly I checked everything was working ok. I checked that the files would upload ok. I checked
response times and refresh time, the links, and the buttons.

**Battleship** game can be found here - https://project3-python-game.herokuapp.com/ *(same link as above)*.

## Version Control
The version control is done using [GitHub](https://github.com). 

The link to the project is https://github.com/dmcginley/Project3-python-game




##### HOW TO CLONE THE PROJECT

##### Heroku

## Resources

*General reading and resources.*

- [Battleship Instructions PDF](https://www.hasbro.com/common/instruct/battleship.pdf)
- [Python 3.10.4 documentation](https://docs.python.org/3/)
- [Real Python (realpython.com)](https://realpython.com/documenting-python-code/#basics-of-commenting-code)
- []()
- []()
- []()

#### Books

- [Python Basics ~ *by Fletcher Heisler, David Amos & Dan
  Bader*](https://www.goodreads.com/book/show/43448128-python-basics-dan-bader)

##### Videos

- [Python Tutorial ~ Python Full Course for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=3)

- [12 Beginner Python Projects ~ Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=5)

- [Python for Beginners ~ Microsoft Developer](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6)

- [More Python for Beginners ~ Microsoft Developer](https://www.youtube.com/playlist?list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj)

- [100 Days of Code: The Complete Python Pro Bootcamp for 2022](https://www.udemy.com/course/100-days-of-code/)


## Credits

*Sites content, media, and help with implementing code from tutorials & online help.*

- [colored 1.4.3](https://pypi.org/project/colored/) ~ Simple library for color and formatting to terminal
- [The Battleship ascii art](https://asciiart.cc/view/11041)
- [stack**overflow** - print one character at a time in Python](https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line)


#### Tutorials

- [Code Institute - *Defining Classes in
  Python*](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+2020_T1/courseware/272f493b4d57445fbd634e7ceca3a98c/c75ed529d8f14d5aa5f359281c76c834/)
- [Battleship! LESSON](https://iampeterkr.github.io/battleship/?utm_source=pocket_mylist) ~ Used as a way of thinking
  about the game
- [Making a Python Battleship Game With Source Code](https://pythondex.com/python-battleship-game?utm_source=pocket_mylist) ~
  Similarly used as reference

##### Videos

- [How to Code Battleship in Python - Single Player Game](https://www.youtube.com/watch?v=tF1WRCrd_HQ&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=38)

- [Game Board with 2D Array / Processing + Python](https://www.youtube.com/watch?v=nsLTQj-l_18&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=39)
- []()
- []()
- []()
