# Testing

## Index

 * [Error resolution and Debugging](#error-resolution-and-debugging)
 * [Manual testing](#manual-testing)
 * [Code Institue Linter testing](#code-institue-linter-testing)
 * [Lighthouse Testing](#lighthouse-testing)

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


### Booking 1:1 Section

| Test Description (Book 1:1)   | Expected Outcome | Actual Outcome |
| ----------- | ----------- | ----- |
|  On 'Click' Loads up booking form  | Booking form appears for user | Pass
|  User can fill out form using widgets  | Can enter in all relevant fields | Pass
|  User MUST fill out all input data fields  | Throws error messsage for any fields missing info | Pass
|  On 'Submit' AKA 'Book Now' | User is taken to and shown booked session reminder | Pass













