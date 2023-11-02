# TotalPlay

Total Play is my own personal love letter(s) for TTRPG's (Table top role playing games), in recent years there has been a resurgence of D&D/Pathfinder/Warhammer40k and these have brought in a whole new generation of gaming. With so many new start upsout there, and older classic games coming out with new stuff, it's hard to keep up and know what might be best to play for yourself.

This blog intertwines reading about whats out there but also allows people to book 1:1 sessions with myself, to chat about any TTRPG's.

## CONTENTS

* [Introduction](#TotalPLay)

* [Sections and Pages](#sections-and-pages)
    *  [Header](#header)
    *  [Sign Up](#sign-up)
    *  [Login Page](#login-in)
    *  [Book 1:1 Section](#book-11-section)
    *  [Made Bookings Section](#made-bookings-section)
    *  [Edit Booking](#edit-booking)
    *  [Footer](#footer)
    *  [Admin](#admin)
* [User Experience](#user-experience)
    *  [User Stories](#user-stories)
* [Design](#design)
    *  [Colour Palette](#colour-palette)
    *  [Typography](#typography)
    *  [Wireframes](#wireframes)
* [Future Ideas](#future-ideas)
* [Technologies Used](#technologies-used)   
    *  [Languages Used](#languages-Used)
    *  [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)


## Sections and Pages

### **Header** 

Within the website I have two different headers, one that allows newcomers to view the blogs, and gives the option to sign in.
The second allows registered users to Book 1:1's and allows them to view and edit/delete there sessions for useful CRUD functionality.
<details>
<summary>Header Signed In ></summary>

![Header](/documentation/image_folders/header_pics/signed_in_pic.png)
</details>
<details>
<summary>Header Signed Out ></summary>

![Header-Out](/documentation/image_folders/header_pics/signed_out_pic.png)
</details>

### **Sign up**
Here users are asked to give there username and password with an option for email. To sign up to TotalPLay. The most is used thanks to bootstraps battery included features, as shwon to us in Code Institues "I think therefore I blog" web app.

<details>
<summary>Register ></summary>

![Register](/documentation/image_folders/register_pics/register.png)
</details>


### **Login In**

Here our pre registered users can sign into thre accounts:
<details>
<summary>Sign In ></summary>

![Login](/documentation/image_folders/login_pics/login.png)
</details>


### **Book 1:1 Section**
One of our User Stories is allowing our User to create and book there own sessions. I wanted the expereince to be straight forward and simple to use. 
Our user is able to do the following:
* Book a meeting at a time and date
* Choose the occasion/ ttrpg they wish to discuss.
* Edit bookings
* Cancel bookings
<details>
<summary>Bookings ></summary>

![Booking](/documentation/image_folders/Book_session_pic/booking.png)
</details>

* Date Selector:
On the booking form, the user can choose the date they'd prefer. As well as picking the date from the widget, they can also type it in as well.
 

* Time Selector:
Here there is a widget of a dropout selection of times, pressing on any of them selects the time chosen and enters it into the form.
 

* Occasion/ TTRPS Selector:
There are so many choices out there I gave a couple of ideas, starting options. As well as a "Help me choose!?" and none incase there was something other they wanted to discuss.

<details>
<summary>Choice Options ></summary>

![Occasion](/documentation/image_folders/Book_session_pic/choice_occasion.png)
</details>

### **Made Bookings Section**
* As well as our users being able to book sessions, keeping track, and changing/deleteing isone of our other aims. Allowing our users the ability to login and mould the back end to edit and delete our bookings whenever suits. 
<details>
<summary>Made Bookings ></summary>

![made booking](/documentation/image_folders/made_booking/made_bookings.png)
</details>

#### Cancel Bookings
* Once a user has cancelled a booking they are redirected back to the home page and given a confirmation message that there 1:1 has been cancelled. 

<details>
<summary>Cancellations ></summary>

![Cancel Booked](/documentation/image_folders/made_booking/cancel_confirmed.png)
</details>

### **Edit Booking**
* As part of good CRUD functionality, our user can edit a pre booked session. Editing any and all original choices, with the original booking values kept for the user to see and confirm.

<details>
<summary>Edit Bookings ></summary>

![Edit Booked](/documentation/image_folders/made_booking/edit_bookings.png)
</details>

### **Footer**

Having a footer is a must, and mine links to all relevant social medias, as well as stating the makers name - my own.
<details>
<summary>Footer ></summary>

![Footer](/documentation/image_folders/footer_img/footer.png)
</details>

### **Admin**

Behind the scenes in the admin page, our superusers can use this as a place to create, edit and modify all there relevant posts. 
* *Our admin can also score there blogs, if the ttrpg is any good.*
<details>
<summary>Blogs ></summary>

![Blogs](/documentation/image_folders/admin_pics/blog.png)
</details>

* *This is also a place where comments are viewed and reviewed for release.*
<details>
<summary>Comments ></summary>

![Comments](/documentation/image_folders/admin_pics/comments.png)

</details>

* *Our administrators can also view and delete any bookings that have been made as well.*

<details>

<summary>Booking Admin ></summary>

![booking admin](/documentation/image_folders/admin_pics/booking_admin.png)
</details>

## **User Experience**

### *User Stories*

## **Desgin**

### *Colour Palette*

### *Typeography*

### *Wireframes*

## Future Ideas

After building the app, there were a couple of ideas that in the future I would like to implement. 
* I would like to add a feature that connects the bokings to a google/ facebook etc calenders.
* Connect up a welcome email to people who have registered.

## Technologies used

### Languages Used
- HTML5
- CSS3
- Javascript
- Python

### Frameworks, Libraries and Programs Used
- [GitHub](https://github.com)
- [Gitpod](https://gitpod.io/workspaces)
- [Fontawesome](https://fontawesome.com/)
- [Chrome Dev Tools](https://www.google.com/intl/en_ie/chrome/)
- [Favicon.io](https://favicon.io/)
- [Django](https://docs.djangoproject.com/) - Using a lot of there documentation through-out.
- [Cloudinary](https://cloudinary.com/)
- [Bootstrap](https://getbootstrap.com/docs/)
- [Heroku](https://id.heroku.com/)
- [Freepik](https://www.freepik.com/)


## Testing

  ### All notes related to testing are found [here](documentation/testing.md).

## Bugs

## Deployment

* Go to the Heroku Dashboard. Create new apllication
* In the 'Settings' tab of your app select 'Reveal Config Vars'.
* Create/ Add 'SECRET_KEY' connecting to your django environment.
* Create/ Add 'DATABASE_URL' connecting to your postgreSQL database.
* Create/ Add 'ClOUDINARY_URL' connecting to cloudinary's cloud hosting service for media.
* Link repository from GitHub to Heroku
* Go to deploy page, select auto deployment
* Deploy Main Branch

## Credits


