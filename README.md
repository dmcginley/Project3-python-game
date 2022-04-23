# Project 3 - Pyhton game

<p>&nbsp;</p>

Site URL:

Repository for the project: https://github.com/dmcginley/project2-chart-my-data

Live website: https://dmcginley.github.io/project2-chart-my-data


<p>&nbsp;</p>

![Finished image of site](readme-images/screenshot.png "the site mobile desktop and tablet")

## Table of contents

<p>&nbsp;</p>

## Wireframe

![wireframe image of site](readme-images/wireframe.png "the site wireframe of desktop and mobile")

## Who is this website for

## User Stories
~~~
As a user...

I want...

So that...
~~~

*"As a user, I want to be able to play a Battleship game in the terminal like the old style game where I can call out the coordinates link 'B1' to try and hit a ship."*

Acceptance criteria:

- Chart terminal based game.

- Use a coordinates method from 1 to 10, and a to j .

<p>&nbsp;</p>

### User Stories todo

- *"As a user, colors
- *"As a user, clear message when a ship is hit or missed
- *"As a user, 
- *"As a user,
- *"As a user,
- *"As a user, error message if I miss the board
- *"As a user, error message if I enter the wrong coordinates

<p>&nbsp;</p>

*"As a user, I want.... 
so that I can....."*

Acceptance criteria:

- 
-
-



<p>&nbsp;</p>

## Technologies Used

### The Code

* **Python3**

### Libraries used

- [colored 1.4.3](https://pypi.org/project/colored/) ~ Simple library for color and formatting to terminal

### Graphic/UX Design

* **Figma, Gimp, & Inkscape.**

## Design Decisions

I decided to create a website that would take the user on a journey for uploading a CSV file to be able to view it as a
chart, rather than just having a chart and expecting that they would automatically know what to do with it.

## Features

## Color Choices

## Responsiveness

## Accessibility

## Consistency

## Testing

*All tested in Incognito mode.*

### Validator Testing

- **HTML**
  <https://validator.w3.org/>

  ![HTML validator testing image](readme-images/html-valid.png)


- **CSS**
  <https://jigsaw.w3.org/css-validator/>

  ![CSS validator testing image](readme-images/css-valid.png)
- **JS**
  <https://jshint.com/>

  ![image of jshint results](readme-images/js-valid.png)

The 3 "unused variables" refer to the functions that are not called inside the JS file, they are callbacks from the HTML
page.

### Manual Testing

*...and how I went about it.*

Checked each time that it switched between the bar and line chart smoothly.

Checked each button went to the proper location.

### Responsive Testing

300px, to laptop 1920px, and to the desktop at 2560px (QHD).

On larger screens, I made sure that the chart did get too large as after a certain size it became clumsy to use.

## Error Handling

- I implemented it to show an error when you would upload an image, as before that PapaParse would still parse the image
  into an array, so it wouldn't catch the error,

- I also set a limit of two columns so you couldn't upload a blank file.

.......................

.......................

.......................

.......................

- I changed the "hitRadius" so that the chat (especially the line chart) is easier to hover on, I found this from
  reading the [Chartjs docs.](https://www.chartjs.org/docs/latest/charts/line.html)

- [jshint](https://jshint.com/) was showing a error so I reformated the clearData() function.

## Deployment TODO:

Deployed using GitHub Pages. <https://github.com/dmcginley/project2-chart-my-data/settings/pages>

I went to my Repository (project2-chart-my-data), and under the "Settings" tab went down to the "Pages" section on the
left menu.
There I could easily deploy my site.

Once everything was deployed I checked everything was working ok. I checked that the files would upload ok. I checked
response times and refresh time, the links, and the buttons.

*GAME* can be found here - https://dmcginley.github.io/project2-chart-my-data (same link as above)

##### HOW TO CLONE THE PROJECT

##### Heroku

## Resources

*General reading and resources.*

- [Battleship Instructions PDF](https://www.hasbro.com/common/instruct/battleship.pdf)
- [Python 3.10.4 documentation](https://docs.python.org/3/)
- []()

#### Books

- [Python Basics - *by Fletcher Heisler, David Amos & Dan
  Bader*](https://www.goodreads.com/book/show/43448128-python-basics-dan-bader)

##### Videos

- [Python Tutorial - Python Full Course for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=3)
- [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&list=PLPZlbsSRAxIoVPwTVmNYjV5HPqc-L1ARg&index=5)

## Credits

*Sites content, media, and help with implementing code from tutorials & online help.*

- [colored 1.4.3](https://pypi.org/project/colored/) ~ Simple library for color and formatting to terminal
- []()
- []()

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

## Content
