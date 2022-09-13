# Irish Macrame by Black Moon Designs

![](media/images/someimage--.png?raw=true)

# Contents

* [Project Purpose - Overview](#project-purpose-overview)
* [User Experience Design](#user-experience-design)
   * [Strategy](#strategy)
   * [Target Audience](#target-audience)
   * [Color Palette](#color-palette)
   * [User Stories](#user-stories)
   * [Scope](#scope)
   * [Features](#features)
      * [General Features](#general-features)
      * [Future Features](#future-features)
   * [Structure](#structure)
   * [Wireframes](#wireframes)
* [Agile Methodology](#agile-methodology)
* [Technologies Used](#technologies-used)
* [Code Validation](#code-validation)
* [Testing](#testing)
   * [Manual Testing](#manual-testing)
   * [Lighthouse](#lighthouse)
   * [Bugs and Issues](#bugs-and-issues)
* [Deployment and making a clone](#deployment-and-making-a-clone)
   * [Deployment to heroku](#deployment-to-heroku)
   * [Forking the Github Repository](#forking-the-github-repository)
   * [Making a local clone](#making-a-local-clone)
   * [Setting up your local environment](#setting-up-your-local-enviroment)
   * [Getting Stripe keys](#getting-stripe-keys)
   * [Getting email variables from gmail](#getting-email-variables-from-gmail)
 * [Credits](#credits)
   * [Online Resources](#online-resources)
   * [Tutorials, stackoverflow and people](#tutorials-stackoverflow-and-people)

# Project Purpose - Overview

A website that promotes handmade macrame items for sale, made by an artist Marika from Poland. She collects wood samples from the forests around the suburban Dublin and creates items tying Irish Cotton around them to make items like Macrames and similar handmade products. She shipps and packs each item hersel and cares for the outlook of every package herself. Her shop started on Etsy on [this link](https://www.etsy.com/ie/shop/BlackmoondesignsArt?ref=simple-shop-header-name&listing_id=1018475936)

# User Experience Design

Color palette is chosen by the macrame creator, boho, earthy notes in colours.
 image of the palette
## Strategy

### Facebook Page

The artist of macrame items actually had already made real FB page which I could not find just by engering keywords, but just after the artist shared this [link](https://www.facebook.com/BlackMoonDesigns13)

![Facebook page image of the page](/media/fb-blackmoondesign.png?raw=true)
![Facebook page image of the content on the page](/media/fb-blackmoon-content.png?raw=true)


## Target Audience

A Macrame shop is for people who like handmade unique macrame products, and have a fond for irish cotton and wood. It is perfect for Gift shopping or for special occasions. Wood taken from Irish forests outside of Dublin and surroundings and Cotton provided from (ask Marika where does she get her supplies to refer)

## Color palette

Artist suggested more warm, boho, soft colors so i went for a combination of these ![colors](/media/palette-colors.png?raw=true)


## User Stories

The user stories were categorised into different priorities, from highest to lowest: "Should Have" "Must Have" "Could Have" "Might Have" "Won't Have". Some User Stories that have been labeled as "Could Have" are not prioritized to be implemented in this edition of this app.

The User Stories that have been satisfied are:

* Create User Navigation : users are able to easy navigate through pages
* Create a homepage and a page for presenting the products - Landing page clearly states the purpose of the app to be a shopping app
* Create a button guiding to browse products - A button to direct to browsing products as main user story 
* Create Searching feature - Ability to search macrames by word if it shows up in description or name
* Create Shopping bag page/view - A page that shows options to add macrame product to choose for purchase
## Scope

## Features

## General Features

---> pictures of the user stories

- Main Navigation on the right hand side, supposing the users are more rigght-handed so it is easier to manage and access on mobile versions. -- provide images of Navigation
- Main Logo and Homepage/landing page (add some text if Marika agrees)
- Main Shopping button outlined in the middle of the homepage as the most obvious thing to do next, to shop for macrames
- Products page with listed items for sale and option to add likes to items on this page without entering the detailed part of the page (will consider if i need liking also inside detailed page) and the detailed product page with ability to add products in the shopping cart
- Messages to notify the user when he/she is logged in succesfully or made an order
- User profile wher users can update their personal information
- Admin ability to add, update and remove product without accessing the admin panel featured in Django
- Add/ Update/ Remove product into the shopping cart
- Checkout page for reaching the payment and completing with stripe payments system

## Future Features

- Add pagination to macrame items page
- Ability to write responses to the reviews of users by the author

## Structure
## Wireframes

First three pages for wireframes

![First three pages for wireframes](/media/home-list-detail.png?raw=true)

# Agile Methodology


![Project Agile](/media/user-stories-image-kanban.png?raw=true)


To create the User stories I used Github Issues and then I grouped them according to MoSCoW prioritization technique. The link with live issues can be found [here](https://github.com/users/totalnoMartina/projects/6). Some of the User Stories will be left for the future development and they are labeled as 'Could Have'.
# Technologies Used

- HTML5/CSS3
- Font Awesome v4
- Javascript
- Bootstrap 4.6
- Python3 -- Django 4
- Stripe

# Code Validation

Html 
CSS
Javascript
Python

# Testing
## Manual Testing
- Test manually on all devices you have - iphone, linux chromebook, ipad
## Lighthouse

![Homepage](/media/homepage-lighth.png?raw=true)

I need to improve contrast by adding borders just for better Accessibility

# Bugs and Issues

Naviagation Burger Bar - The navigation was working  fine but when I left the app for a while(Leave of Absence for work purposes) and came back to it, the navigation of burger button to turn into 'X' on opening of navigation started to go outside of the navigation bar, going to the left so I will have to explore as i have Javascript function to close navigation onclick when clicked outside of the navbar which might cause issues for this burger menu bar to be out of order. Also I thought of dropping it altogether.

I used another app similar to this to try and test out the CRUD functionality of reviews being created, Updated and Deleted, so before putting the code here i struggled with thecreate part as it was using forms in the case of tutorials I followed adn most helpful in this situation was [this one here](https://www.youtube.com/watch?v=EX6Tt-ZW0so&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=15), bug was that i could not make redirect url to go to the same page so i am exploring solution for this one.

I watched several tutorials on putting likes and dislikes and decided at the end I would not want to promote 'disliking' but focus more on 'liking' so i made the funsction to be able to 'like' or if it is liked to 'unlike which does not show any 'dislike'. After testing it on another app in [this repository](https://github.com/totalnoMartina/macrame-shopping). Also here my redirect needs fixing, I am trying to find solution for the like to work without refreshing the whole page so still exploring this.

I am also trying to test newsletter app in [this repo](https://github.com/totalnoMartina/the-macrames) as I want to make sure something works before I include it in my project as I have crashed so many apps during developing this one. At the moment it is not commited as I am having small issues figuring it out in the most simple way. I might need help from my mentor about this as I got the impression that it is easy but then some tutorials have it a bit complicated, so I am exploring this through [this tutorial](https://www.youtube.com/watch?v=yZPgBThZT04&list=PLGzru6ACxEAKtb29AeyHbVGUh2-0r891H&index=27).

I spoke to a fellow student Iulia Konovalova about Error pages and she recommended something like [this](https://github.com/IuliiaKonovalova/e-commerce/blob/main/ecommerce_project/views.py) and I am just now finding best way to test to see my error page, so still looking into this.

During payment process, message shows email confirmation will be sent but no email goes anywhere also, the order total is not rendering so it charges all zeros, I must check does it have anything to do with profile app that user information on charge is not maybe stored
# Deployment and making a clone
## Deployment to heroku

**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens.**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "Settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automaticaly
    * Secret_key - one can be generated [here](https://miniwebtool.com/django-secret-key-generator/) or make up your own secret key.


**Go back to your code**

12. Procfile needs to be created in your app
Content of Procfile has a structure like this :
```
web: gunicorn PROJECT_NAME.wsgi
```

13. In settings in your app add your name of your Heroku App to ALLOWED_HOSTS without the starting slashes and 'https:'

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"

23. Click the button "View"

The live link can be found [here](live/page/here/???).

## Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/totalnoMartina/irish-macrame)
2. In the same line as the name of your repository, on the right side there are a few buttons, locate the "Fork" button and click on it
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/totalnoMartina/irish-macrame)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/totalnoMartina/irish-macrame
```

7. Press Enter. Your local clone will be created.

## Setting up your local enviroment

1. Create Virtual enviroment on your computer or use gitpod built-in virtual enviroment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add-on when creating an app. 
* Secret_key - the django secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 
* Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1) you will have to register with google and create new app to get the API key. Follow the instructions on the website.

```
DEVELOPMENT
SECRET_KEY

STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY 
STRIPE_WH_SECRET

```
PostgreSQL and Cloudinary URL keys are needed only on Heroku, not in local IDE

3. Run command 
```
pip3 freeze --local > requirements.txt
```

## Getting Stripe keys
Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Than click add endpoint
You should be redirected to this webhook's page. Reveal webhook sign in secret and copy to Settings and to heroku as STRIPE_WH_SECRET variable


## Getting email variables from gmail


- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address


Github and Heroku - explain all steps
# Credits
## Online Resources

* [Font Awesome](https://fontawesome.com/)
* [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Google Fonts](https://fonts.google.com/)
*[Coolors Website](https://coolors.co/)
## Tutorials, stackoverflow and people

Most of the code has been used from Code Institute curriculum for the e-commerce related code, mainly from 'Boutique Ado' regarding items, bag and payment section, and for deployment steps, cloudinary and starting apps has been followed by the walkthrough project 'I think, Therefore I Blog'. Many thanks to teachers that presented us a way to make an e-commerce website using Django.

First bugs were related to CSS, as it was not loading background linear so I used [stackoverflow](www.stackoverflow.com) and found [this solution](https://stackoverflow.com/questions/45134867/css-html-how-to-stop-linear-gradient-from-repeating-vertically-and-horizontall).
The [MyColor](https://mycolor.space) was used to help choose colors. [Google Fonts](https://fonts.google.com/) was used for selection of fonts for the website.
Finding a cool navigation was not an easy task but [here](https://mdbootstrap.com/docs/b4/jquery/navigation/hamburger-menu/) I found one that suits.

Finding way to easy CRUD functionality through this [link](https://www.youtube.com/watch?v=EX6Tt-ZW0so&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=15)
More info on CRUD on this [website](https://www.youtube.com/watch?v=Y5vvGQyHtpM)

More help for the review idea on this [video](https://www.youtube.com/watch?v=Y5vvGQyHtpM)

A great example of a README.md found [here](https://github.com/JoGorska/mileage-tracker/blob/main/README.md#tank-mileage-tracker) by [JoGorska](https://github.com/JoGorska) , a very inspiring individual and Alumni at the Code Institute.

I wanted likes to be only available to users that are logged in so I found more information on [django documentation here](https://docs.djangoproject.com/en/3.2/topics/auth/default/)

Found a guide on supscriptions/newsletters for non-registered user which I might use as I have used the dynamic rendering of the curent year using a jinja template on this [link](https://medium.com/geekculture/subscribe-to-newsletter-in-django-427da9db74ed)

A [link](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail) that helped me handle csrf token error in the begining because i am using Django 4.

As I was trying to find best explanation of deployment steps I found most genuine approach from [JoGorska README.md](https://raw.githubusercontent.com/JoGorska/bonsai-shop/main/README.md) of the project bonsai-shop and used the same approach to explain this.

I would like to thank to my mentor Tim Nelson, fellow students Iulia Konovalova and JoGorska, as well as the CI community and Slack community for the support and sharing the bugs and solutions that help each other grow, it is highly apreciated and forever remembered to be passed on to another student/fellow coder in the future.
