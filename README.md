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

*"As a user, I want to be able to upload a CSV file to a chart so that I will be able to view my date more visually."***

Acceptance criteria:

- Chart upload button.

- User’s CSV displays on chart.

<p>&nbsp;</p>

*"As a user, I want to view my chart with a dark theme to lessen my eye strain from bright screens."*

Acceptance criteria:

 - Dark theme with lighter chart and chart elements.

- Buttons kept lighter than the background.

- Correct contrast between colors for the dark theme.

<p>&nbsp;</p>


## Technologies Used
### The Code
* **Python3**

### Libraries used
- **Py_somthing** https://www.........


### Graphic/UX Design
* **Figma, Gimp, & Inkscape.**

## Design Decisions

I decided to create a website that would take the user on a journey for uploading a CSV file to be able to view it as a chart, rather than just having a chart and expecting that they would automatically know what to do with it.


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

The 3 "unused variables" refer to the functions that are not called inside the JS file, they are callbacks from the HTML page.

### Manual Testing
*...and how I went about it.*



Checked each time that it switched between the bar and line chart smoothly.

Checked each button went to the proper location.

### Responsive Testing

 300px, to laptop 1920px, and to the desktop at 2560px (QHD).

On larger screens, I made sure that the chart did get too large as after a certain size it became clumsy to use.

## Error Handling

- I implemented it to show an error when you would upload an image, as before that PapaParse would still parse the image into an array, so it wouldn't catch the error,

- I also set a limit of two columns so you couldn't upload a blank file.

.......................

.......................

.......................

.......................

- I changed the "hitRadius" so that the chat (especially the line chart) is easier to hover on, I found this from reading the [Chartjs docs.](https://www.chartjs.org/docs/latest/charts/line.html)

- [jshint](https://jshint.com/) was showing a error so I reformated the clearData() function.

## Deployment
Deployed using GitHub Pages. <https://github.com/dmcginley/project2-chart-my-data/settings/pages>

I went to my  Repository (project2-chart-my-data), and under the "Settings" tab went down to the "Pages" section on the left menu.
There I could easily deploy my site. 

Once everything was deployed I checked everything was working ok. I checked that the files would upload ok. I checked response times and refresh time, the links, and the buttons.


Chart Data can be found here - https://dmcginley.github.io/project2-chart-my-data (same link as above)

## Image optimization for the web

For all the images I edited them in [Gimp](https://www.gimp.org/) changing the resolution when required. I'd pass the images through
Tinypng and then put them in the image folder.
- [Tinypng](https://tinypng.com/)

- [favicon.io](https://favicon.io/favicon-converter/) - used for generating the set of images for the tab in the browser.

## Resources
*General reading and resources.*

- [uxplanet.org *8 Tips for Dark Theme Design*](https://uxplanet.org/8-tips-for-dark-theme-design-8dfc2f8f7ab6) 

- [4 Ways to Empty an Array in JavaScript](https://www.javascripttutorial.net/array/4-ways-empty-javascript-array/?utm_source=pocket_mylist)

- [User Stories *from Mountain Goat Software.com*](https://www.mountaingoatsoftware.com/agile/user-stories)

- [Papa Parse - *Documentation*](https://www.papaparse.com/docs)

- [Acceptance Criteria](https://www.productplan.com/glossary/acceptance-criteria/#:~:text=In%20Agile%2C%20acceptance%20criteria%20refer,consider%20the%20user%20story%20finished.)



#### Books 
- [Eloquent JavaScript - *by Marijn Haverbeke*](https://www.goodreads.com/book/show/52016825-javascript)

- [JavaScript and jQuery: Interactive Front-End Web Development - *by Jon Duckett*](https://www.goodreads.com/book/show/16219704-javascript-and-jquery)

## Credits
*Sites content, media, and help with implementing code for tutorials/online help.*

- [w3schools](https://www.w3schools.com/js/default.asp) - JavaScript
- [Mozilla Developer](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - JavaScript
- [d3js](https://d3js.org/)
- [Efficiently load third-party JavaScript](https://web.dev/efficiently-load-third-party-javascript/)
- [meta description](https://web.dev/meta-description/?utm_source=lighthouse&utm_medium=devtools)

#### Tutorials

- [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LMR101+2021_T1/courseware/73e9c0413ead4a21b389e33c77706102/4fe6474cab114387ad0e72bf7ec1c201) - working with Arrays & Objects.

- [Tabular Data - Working With Data & APIs in JavaScript](https://www.youtube.com/watch?v=RfMkdvN-23o)

- [JavaScript Programming Tutorial 39 - Average of Array Values](https://www.youtube.com/watch?v=QgUnJhUTGoI)

- [JavaScript Break and Continue](https://www.w3schools.com/js/js_break.asp) - to break out of the loop for the buttons.

- [How to Parse CSV String in Javascript with Papaparse JS](https://www.youtube.com/watch?v=s6SgVjIvIV8&list=PLPZlbsSRAxIpfL9s3LPCXqllojDEqxAXl&index=11) - using PapaParse.

- [How to Create a Chart with a Remote CSV File with Chart JS](https://www.youtube.com/watch?v=HFAjrai-d58)

- [How to Write Good User Stories](https://www.youtube.com/watch?v=tKSUokG3Y0w)

## Content
The "how to use" text on the home page, (Toggle Between Bar Or Line Chart section).

class = **"note-text-container"**
[Bar Graph vs Line Graph *from https://www.smartdraw.com*](https://www.smartdraw.com/bar-graph/#:~:text=data%20over%20time.-,Bar%20Graph%20vs%20Line%20Graph,differences%20in%20data%20among%20groups.)

Image of cat for error message downloaded from [pexels](https://www.pexels.com/photo/photo-of-orange-tabby-cat-with-red-handkerchief-1741205/).
