# The Rank Your Sword Fighter Project

The Rank Your Sword Fighter Project aims to create a user input based ranking of the greatest sword fighters in anime/manga. As characters in the different series are hard to compare, this aims to provide an expression of popular opinion about what sword fighter characters to keep an eye on as series progress if one is in to the genre. Furthermore, the website hopes to be a good way to introduce people to the genre as you can make more accurate guesses about what to forward to friends in order to spark interest, if you got some understanding of popular opinion.

![Responsice Mockup](https://github.com/jensbrauer/rateYourSwordfighter/blob/main/docs/mockup.PNG)

## Features 

This page has an initial landing page, giving some explanation to the features you can expect to find and navigational links to go there. Also it is decorated with a cool image to set the mood for the experience.
The navbar logo and the text provided is aimed to be somewhat self explanatory and navigational links are ment to be obvious at firsst glance.
The page is meant to call to action and increase in value by user interaction.

### Existing Features

- __Navigation Bar__
  - Featured as a fixed item always displaying at the topp of the page, in order for the user to always have navigation options at hand.

- __The landing page__
  - The landing page is mainly created to highlight the amazing artwork highlight the genre for the content.
  - It also displays the features of the page, what the user can expect to find and is ment to call for action.

- __Ranking List__
  - The ranking list is the main feature of the webpage. Accesible to visitors to view and users to interact with.

- __Individual Character Pages__
  - In the individual characters pages, everyone can explore some more detailed information about the characters but most importantly acces the comment field where one can read about peoples qualitative description and thoughts about the character.


- __Contribute Page__ 
  - The contribute page is also a call to action feature where users are encouraged to upload suggestions for characters that they want featured in the ranking list. As characters and series are constantly developed, the feature should remain relevant.


### Features Left to Implement

- A feature scrapped in the planing process was the ability for users to upload "content" such as video material, artwork and other cool stuff related to the characters. This could be included in the character pages and add more user interaction as well as read-value.

## Testing 

The site has been thouroughly tested in a structured manual way. Thre scenarios where created to represent interaction on the site; The Visitor Scenario, The User Scenario and the Admin Scenario. All pages where tested and their features such as buttons, links etc where tested and evaluated.
All tests and outcomes including bugs and fixes where documented seperatly and can be found [here!](https://github.com/jensbrauer/rateYourSwordfighter/blob/eaed5dd3abf7461c073be31517ea21a69d77a971/TEST.md)


### Validator Testing 

- Lighthouse reports can be accessed in docs file
  - ![Landingpage](https://github.com/jensbrauer/rateYourSwordfighter/blob/main/docs/mockup.PNG)
  - ![Rankingpage](https://github.com/jensbrauer/rateYourSwordfighter/blob/main/docs/mockup.PNG)
  - ![Contributepage](https://github.com/jensbrauer/rateYourSwordfighter/blob/main/docs/mockup.PNG)

- HTML
  - [W3C validator](https://validator.w3.org/nu) returned no errors.
- CSS
  - [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator) returned no errors.

-PEP8 Validation
  - [Code Institutes CI Python Linter, PEP8 heroku app](https://pep8ci.herokuapp.com/) returned som problems that was not addressed due to time constraints:
    - ranking/views.py return 13 instances of line too long.
    - ranking/urls.py return no errors.
    - ranking/forms.py returned 15 errors related to white space and line to long.
    - ranking/models.py returned 5 errors of line to long.

### Unfixed Bugs

No bugs found during testing have been unfixed.

## Deployment

### The finalized version of the app was deployed on Heroku.
#### Process step by step:
- Clone this repository
- Create a new app on heroku

- Set up config vars under settings;
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - CLOUNDINARY_URL: (cloudinary api url)

- Link the Heroku app to the repository
- Under "Manual deploy", select main branch and press "Deploy Branch"
- After the build is finished, a success message will be displayed together with a button to view to deployed app.

This is the live link for the deployed project - https://rate-your-swordfighter.herokuapp.com/


## Credits 

### Media

- The landing page image used on the home page is from [Tyane Robinson](https://www.kindpng.com/userpngs/14556/) at [KindPng](https://www.kindpng.com/).





