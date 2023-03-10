# MANUAL TESTING ON DEPLOYD WEBSITE

## THE VISITOR SCENARIO

### ERROR PAGES

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| Restricted endpoints | Edit other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | Pass |
| | Delete other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | Fail |
| | View other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | Fail |
| Nonexistent endpoints | Type link+/aösdjknas | Throw 404 with a navlink to ranking list | Pass |
| Server error | Plant a bug and run page | Throw 500 with a navlink to ranking list | Pass |

### MAIN PAGES

#### Landing page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to home page through URL | Display correctly | Pass |
| Ranking list link | Click the link | Redirect to ranking list page | Pass |
| Log in link | Click the link | Redirect to login page | Pass |

#### Ranking list

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via navbar | Display correctly with published swordfighters name, current ranking place, which series they appear on and an upvote button. | Pass |
| Fighter card image link | Click the link | Redirect to fighter's individual page | Pass |
| Fighter card name link | Click the link | Redirect to fighter's individual page | Pass |
| Fighter card upvote button | Click the link | Redirect to login page | Pass |

#### Swordfighter page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via ranking list card | Display correctly with published swordfighter name, which series they appear on, a description of the character, the number of upvotes for the character, an upvote button, comment form with a sign in btn instead of sign up. | Pass |
| Fighter upvote button | Click the button | Redirect to login page | Pass |
| Comment form | Write a comment and push associated button "Log in to comment" | Redirect to login page | Pass |
| Comments section | Read comment section | No buttons for flag or delete should be visible | Pass |

#### Contribute page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via navbar | Should render the suggestion form with a button styled link that says Sign in instead of submit button. | Pass |
| Sign in button | Click the button | Should redirect to sign in page. | Pass |

### ACTION PAGES

#### Are you sure delete page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page through URL confirmed by a logged in user. | Should throw a 403 error. | Fail |

#### Edit swordfighter page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page through URL confirmed by a logged in user. | Should throw a 403 error. | Fail |

### FUNCTIONAL

#### base.html

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to home page through URL | Should throw a 403 error. | pass |
| Navbar logo link| Click the link | Should redirect to landing page | pass |
| Contribute link | Click the link | Should redirect to contribute page. | pass |
| Ranking link | Click the link | Should redirect to ranking list page. | pass |
| Create account link | Click the link | Should redirect to create account page. | pass |
| Log in link | Click the link | Should redirect to login page. | pass |

### ACCOUNT

#### sign in

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via navbar | Should display page with submit form to log in| pass |
| Form | Submit valid form with username and password| Should sign in the user. | pass |
| Form | Submit invalid form with unregistered username and password| Should reload the same page with error msg. | pass |

#### sign up

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --------------- | ------------------------------------------- | -------------------------------------------- | --------- |
| On Load | Navigate to page via navbar | Should display page with submit form to sign up| pass |
| Form | Submit valid form with username and password with repetition| Should create user instance, sign in the user and redirect to landing page.| pass |

#### sign out

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --------------- | ------------------------------------------- | -------------------------------------------- | --------- |
| On Load | Navigate to page through URL | Should redirect to home page. | pass |


# THE USER SCENARIO

### ERROR PAGES

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| restricted endpoints | edit other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | pass |
| | delete other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | pass |
| | View other users suggestion through endpoint URL | Throw 403 with a navlink to ranking list | pass |
| nonexistent endpoints | type link+/aösdjknas | Throw 404 with a navlink to ranking list | pass |
| servererror | plant a bug and run page | Throw 500 with a navlink to ranking list | pass |

### MAIN PAGES

#### landingpage

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to home page through URL | Display correctly | pass |
| Ranking list link | Click the link | Redirect to ranking list page | pass |
| Log in link | Click the link | Redirect to landing page as I am already logged in | pass |

#### rankinglist

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via navbar | Display correctly with published swordfighters name, current ranking place, which series they appear on and an upvote button. | pass |
| Fighter card image link | Click the link | Redirect to fighters individual page | pass |
| Fighter card name link | Click the link | Redirect to fighters individual page | pass |
| Fighter card upvote button | Click the button | A message should be displayed saying I successfully upvoted, the number of upvotes field should increase by one and the upvote button should be replaced by an "undo upvote" button. | pass |
| Fighter card undo upvote button | Click the button | A message should be displayed saying I successfully removed my upvote, the number of upvotes field should decrease by one and the upvote button should be reappear instead of the "undo upvote" button. | pass |

#### swordfighter page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via ranking list card | Display correctly with published swordfighter name, which series they appear on, a description of the character, the number of upvotes for the character, an upvote button and a comment form with a submit button. | pass |
| Fighter upvote button | Click the button | A message should be displayed saying I successfully upvoted, the number of upvotes field should increase by one and the upvote button should be replaced by an "undo upvote" button. | pass |
| Fighter card undo upvote button | Click the button | A message should be displayed saying I successfully removed my upvote, the number of upvotes field should decrease by one and the upvote button should be reappear instead of the "undo upvote" button. | pass |
| Comment form | Write a comment and push associated button "Submit" | My comment should appear in the comments section as well as a success message at the top of the page. | pass |
| Comments section | Read comment section | A delete button should be displayd on my comments and a "Flag this comment" should display on other users comments. | pass |
| Comment delete button | Click the button | My comment should be deleted from the comment section and a message should be displayed indicating I successfully removed it. Confirm from the admin page that the comment was

#### contribute page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via navbar | Should render the suggestion form with a button styled link to submit the form. If any suggestions have been made for swordfighters those should be displayed as preview cards with Status indicator and buttons. If published, a button link to view the character page. If "pending approval", a view page button, delete button and edit button. | Pass |
| Submit button | Click the button | Should give a message response, if the suggestion was submitted successfully or not. If the suggestion was a success, the suggestion should have been automatically added to the suggestions field below the form. | Pass |
| "View page" button | Click the button | Should redirect to the character page. | Pass |
| Delete button | Click the button | Should redirect to an "Are you sure you want to delete <swordfighter's name>?" page. | Pass |
| Edit button | Click the button | Should redirect to an "Edit swordfighter" page. | Pass |

### ACTION PAGES

#### RU sure delete page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate to page via "Delete button" on "Contribute" page. | Should display a card asking "Are you sure you want to delete <swordfighter's name>?" And one buttons for Delete and one for Return to contribute page. | Pass |
| Delete button | Click the button | Should navigate back to contribute page with success message and swordfighter should have been removed from "My suggestions" section. | Pass |
| Return | Click the button | Should redirect back to contribute page. | Pass |

#### Edit swordfighter page

| Element to test | Test procedure | Expected outcome | Pass/Fail |
| --- | --- | --- | --- |
| On Load | Navigate via edit button on contribute page | Should display a form like the one on the contribute page with the swordfighter's current information prefilled in the input fields. | Pass |
| Submit | Click the button | Should redirect to contribute page and display success, or fail message. If success, the changes should be visible in the suggestions section. | Pass |
| Return to contribute | Click the button | Should redirect to contribute page. | 

### FUNCTIONAL

#### base.html

Element to test | Test procedure | Expected outcome | Pass/Fail
--- | --- | --- | ---
On Load | Navigate to home page through URL | Should redirect to landing page. | Pass
Navbar logo link | Click the link | Should redirect to landing page. | Pass
Contribute link | Click the link | Should redirect to contribute page | Pass
Ranking link | Click the link | Should redirect to ranking list page | Pass
Sign out, <username> | Click the link | Should redirect to "Are you sure you want to sign out" page | Pass

### ACCOUNT

#### sign in

Element to test | Test procedure | Expected outcome | Pass/Fail
--- | --- | --- | ---
On Load | Navigate to page via URL | Should redirect to landing page | Pass

#### sign up

Element to test | Test procedure | Expected outcome | Pass/Fail
--- | --- | --- | ---
On Load | Navigate to page via URL | Should redirect to landing page | Pass

#### sign out

Element to test | Test procedure | Expected outcome | Pass/Fail
--- | --- | --- | ---
On Load | Navigate to page through nav link in navbar | Should display a card with question "Are you sure you want to sign out?" and a button to confirm signout | Pass
Signout button | Click the button | Should trigger a message and redirect to home page. | Pass

# THE ADMIN SCENARIO
### ADMIN PAGES

#### Swordfighters

| Element to test | Test procedure | Expected outcome | Pass/Fail |
--- | --- | --- | ---
| Swordfighters list view | Login to admin page and navigate to Swordfighter model | The ability to filter based on status | Pass |

#### Comments

| Element to test | Test procedure | Expected outcome | Pass/Fail |
--- | --- | --- | ---
| Comments list view | Login to admin page and navigate to Comments model | The ability to filter based on status and order by number of flags | Pass |

# BUGS

| Test Theme | restricted endpoints | |
--- | --- | --- |
| Test | delete other users suggestion through endpoint URL | View other users suggestion through endpoint URL |
| Expected outcome| Throw 403 with a navlink to ranking list | Throw 403 with a navlink to ranking list |
| Test outcome | Was able to delete swordfighter though published and added by other user. | Was able to delete swordfighter though published and added by other user. |
| Fix | Created new authorisation valid function to Helper class in views. | Created new authorisation valid function to Helper class in views. |
