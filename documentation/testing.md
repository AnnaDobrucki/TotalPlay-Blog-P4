# Testing

## Index

 * [Error resolution and Debugging](#error-resolution-and-debugging)
 * [Validation](#validation)
 * [Manual testing](#manual-testing)
 * [Lighthouse Testing](#lighthouse-testing)


## Error resolution and Debugging

Through-out this project there were various bugs and error's that I had help fixing through-out.

* Understanding how to wire up URL's was a hard thing to remember and master. I had to end up renaming a path because two urls had the same structure, I realised django will use the first one that matches, so it was trying to use the string 'bookings' as a slug for my post detail url. 

* I had a font awesome problem, a tutor Osin pointed out that I had accidentally used the wrong version. After a quick update my score rating symbols started to work.

* I had to understand why my code wasn't validating, until a tutor told me to run the html from the inspect code from broswer. 

* After creating the new model for bookings, making the form and views. I was baffled why I kept getting an error not being able to find the bookings form. After remembering I had to migrate and update this (and remembering to wire up url's) transferes user to the booking form.



## Validation
Below are all verifications of code validations. 

### HTML Validation

For HTML validation I was instricted by tutors to do the following:
1) Open page in browser.
2) View page sorce code.
3) Copy and paste into relevant Validator.

* Home Page Validation

<details>

<summary>Home Page Validation ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/home_page_val.png)
</details>

* Sign In Validation 

<details>

<summary>Sign In Validation ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/sign_in_val.png)
</details>

* Register

<details>

<summary>Register ></summary>

![booking admin](/documentation/image_folders/)
</details>

* Book 1:1 Session Page

<details>

<summary>Booking Session ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/booking_validation.png)
</details>

* 

### Admin.py 

<details>

<summary>Admin.py Validation ></summary>

![booking admin](/documentation/image_folders/linter_pics/admin.py_linter.png)
</details>

### Forms.py

<details>

<summary>Form.py Linter ></summary>

![booking admin](/documentation/image_folders/linter_pics/form.py_linter.png)
</details>

### Models.py 

<details>

<summary>Models.py Linter ></summary>

![booking admin](/documentation/image_folders/linter_pics/models.py_linter.png)
</details>

### Urls.py 

<details>

<summary> Urls.py Linter ></summary>

![booking admin](/documentation/image_folders/linter_pics/urls.py_linter.png)
</details>

### Views.py 

<details>

<summary> Views.py Linter ></summary>

![booking admin](/documentation/image_folders/linter_pics/views.py_linter.png)
</details>

## Manual Testing 

### Landing Page

| Test Description (Home Page)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
|  Start Load Page   | All current posts should load  | Pass
| Ability to see scores | Should be able to visually see the Dice rating | Pass
| On 'click' to any TotalPlay | Should redirect to Home Page| Pass
| On 'click' to any blog post | Should redirect to full article | Pass
| On 'click' to Register | Should redirect to Registration Page| Pass
| On 'click' to Sign In | Should redirect to Sign In| Pass
| ----------- | ----------- | ----- |
| Within Blog Clicked| See all comments made| Pass
| Within Blog Clicked| See all likes given| Pass
| Click to remove like | Like removed| Pass
| Logged in user can type comments | See comments box| Pass
| User without log in | Refered to create or log in to make comment| Pass


### Admin Page 

| Test Description (Admin Page Backend)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
|  Log in as Super User  | Allows access to administrative roles | Pass
| Allow Creation of New Post  | Once puplished posts appear on Home Screen| Pass
| Edit New and Old Posts | Edit and review old posts to keep up to date| Pass
| Delete Posts  | Should cascade upon deletion, and remove from Home Page | Pass
| ----------- | ----------- | ----- |
| Review Comments | Visually see all comments made | Pass
| Authorise Comments | Approve comments show on relevant blog | Pass
| ----------- | ----------- | ----- |
| Go into booking section | See all sessions booked with all relevent info ie name/time etc.| Pass
| Go into booking section | Can delete session| Pass


### Registration Page 

| Test Description (Registration Page Backend)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
| Allows new user create username and password  | Username and Password fields MUST be filled | Pass
| Message to new user account | A message box appears to tell new user they have sucesfully signed in| Pass

### Sign In Page 
| Test Description (Sign In Backend)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
| On 'click' user is redireted to Sign In page| Sign in page is shown | Pass
| On 'click' user can go to registration page if needed| Registration page renders| 
| On correct username and password user is logged in| Successful message is given to confirm| Pass
| Once logged in user has access to Bookings and Made Bookings| Nav Bar extends with new icons| Pass

### Sign Out Page 
| Test Description (Sign Out Backend)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
| On 'click' user is redireted to log out page | Log out page is shown | Pass
| User is asked if they wish to sign out | Sign Out button is present to user| Pass
| On 'click' user is logged out sucessfully | Message to confirm log out complete | Pass


### Booking 1:1 Section

| Test Description (Book 1:1)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
|  On 'Click' Loads up booking form  | Booking form appears for user | Pass
|  User can fill out form using widgets and input fields | Can enter in all relevant fields | Pass
|  User MUST fill out all input data fields  | Throws error messsage for any fields missing info | Pass
|  On 'Submit' AKA 'Book Now' | User is taken to and shown booked session reminder | Pass

### Made Booking Section 

| Test Description (Made Booking)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
|  User can see all bookings made | All booking are shown | Pass
|  User 'on click' can edit made bookings | Sends user to edit.html | Pass
|  Edit.html has previous data available  | Renders all previous data | Pass
|  Updating Edit form  | Updates with new data user has made | Pass
|  On 'click' deletes session  | User is redirected to home page and shown confirmation of deletion | Pass
















