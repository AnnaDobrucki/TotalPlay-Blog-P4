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

* After trying to render my form, I found that using 'form.as.p' allowed the form to occur as a paragraph which helped to place it in the template.

* I had a couple of issues trying to get the form to redirect after the info had been pushed to the database, one of the CI tutors helped me understand that I needed to import the keyword of redirect. 

* Had trouble with trying to Validate the Registration Page, after multiple tries, I went to tutor help that informed me this was an AllAuth templates error issue that I wouldn't be able to fix, and to mention within the ReadMe. 

* An error I was unsure of fixing was the low resolution picture on the home page. This came from the back-end admin site, allowing admins to build and post there own blogs. Should an Admin use a picture of lower resolution that is there perogative, however it did mean the performance lighthouse test wasn't in the 90's for this reason. This woukd be something I'd want to fix in future to not allow low res pictures to be uploaded on the site.

## Validation
Below are all verifications of code validations. 

## HTML Validation

For HTML validation I was instricted by tutors to do the following:
1) Open page in browser.
2) View page sorce code.
3) Copy and paste into relevant Validator.

### Home Page Validation

<details>

<summary>Home Page Validation ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/home_page_val.png)
</details>

### Sign In Validation 

<details>

<summary>Sign In Validation ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/sign_in_val.png)
</details>

### Register

* Please see [Error and Debug Section](#error-resolution-and-debugging)

### Book 1:1 Session Page

<details>

<summary>Booking Session ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/booking_validation.png)
</details>

### Book Edit Page 

<details>

<summary>Edit Page ></summary>

![booking admin](/documentation/image_folders/validation_html_pics/edit_page_val.png)
</details>

## Linter PEP8 testing

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

## Lighthouse Testing 

### Home Page 

[Home Page Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/home_page_lighthouse.png)

### Register Page 

[Register Page Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/register_lighthouse_pic.png)

### Booking Page 1:1

[Booking Page Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/booking_page_lighthouse.png)

### Made Bookings Page 

[Made Bookings Page Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/made_bookings_lighthouse.png)

### Edit Booking Page 

[Home Page Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/edit_bookings_lighthouse.png)

### Sign Out Page 

[Sign out Lighthouse Pic](/documentation/image_folders/Lighthouse_test_pics/sign_out_lighthouse.png)



















