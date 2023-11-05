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

### *Admin Users*

- To allow super users the ability to have easy access to the admin side. Allowing for a responsive website that allows them to shape there website, blog and bookings as they see fit.

### *User Stories*

Using the GitHub I used the agile methods and tools to allow myself to create and keep track of the User Stories I set out for myself in the beginning. 
<details>

<summary>User Stories Git Hub ></summary>

![booking admin](/documentation/image_folders/UserStories_pics/user_stories.png)
</details>

1) As a Site user I can make an account to leave likes and comments on things I read.
2) As a Site User I can comment on each post so I can share my opinions
3) As a Site user I can make my own account to leave likes and comments
4) As a Site User I can see all comments so I can read the conversation
5) As a Site user I can unlike a previous posr so that share my feelings
6) As a Site User I can click on a post to read the entire blog
7) As a Site User I can view varying posts and select ones to read
8) As a Site user I can book a 1:1 chat about Role Playing Games to learn more about this field
9) As a Site User I can edit/delete and view my bookings so that I can resolve any issues and remind myself of future bookings.
10) As a Site Admin I can see who has booked appointments to allow me to manage my diary and promotion
11) As a Site Admin I can manage peoples bookings in case of emergencies or cancellations
12) As a Site Admin I can create, read, update + delete posts so I can manage my blog


## **Desgin**

### *Colour Palette*

### *Typeography*

### *Wireframes*

## Future Ideas

After building the app, there were a couple of ideas that in the future I would like to implement. 
* I would like to add a feature that connects the bokings to a google/ facebook etc calenders.
* Connect up a welcome email to people who have registered.
* Due to time constraints I left one user story unfufilled of allowing users to edut comments. This would be a feature I'd enjoy making in future. 

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

Through-out this project I was inspired and helped by a number of sources, in order to make custom code:

1) Creating the Form/ Booking Sign Up:
    - Allowed me insight into how to render my formonce built [Geeks for Geeks](https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/)
    - Understanding the Model Form build thanks to django documentation [Django](https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/)
    - Watching this clinic based walkthrough, whilst overwhleming, did allow me some insight into times and dates [Clinic Walkthrough Youtube](https://youtu.be/s5xbtuo9pR0)
    - This article was informative about how to get widgets within my form [Let's Code More](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/)

2) After some tutor help and read the following article I was able to redirect my users to different templates [Real Python](https://realpython.com/django-redirects/)

3) This article on validators helped me to create the scoring system that I added to the POST Model [Django](https://docs.djangoproject.com/en/4.2/ref/validators/)

4) The base of the blog is thanks to the skeleton code of Code Institue's 'I think therefore I blog walkthrough'.

* I'd also like to credit thanks to all the tutors that helped guide me through-out at Code Institue.
