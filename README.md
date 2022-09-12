# Irish Macrame by Black Moon Designs

![](media/images/someimage--.png?raw=true)

# Contents

* [Project Purpose - Overview](#project-purpose-overview)
* [User Experience Design](#user-experience-design)
   * [Strategy](#strategy)
   * [Target Audience](#target-audience)
   * [User Stories](#user-stories)
   * [Scope](#scope)
   * [Features](#features)
      * [General Features](#general-features)
      * [Future Features](#future-features)
   * [Structure](#structure)
   <!-- * [Browser Compatibility](#browser-compatibility) -->
* [Skeleton](#skeleton)
   * [Wireframes](#wireframes)
* [Agile Methodology](#agile-methodology)
* [Technologies Used](#technologies-used)
* [Code Validation](#code-validation)
* [Testing](#testing)
   * [Manual Testing](#manual-testing)
   * [Lighthouse](#lighthouse)
   * [Bugs and Issues](#bugs-and-issues)
* [Deployment](#deployment)
* [Credits](#credits)

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
- Main Navigation on the right hand side, supposing the users are more rigght-handed so it is easier to manage and access on mobile versions. -- provide images of Navigation
- Main Logo and Homepage/landing page (add some text if Marika agrees)
- Main Shopping button outlined in the middle of the homepage as the most obvious thing to do next, to shop for macrames
- Products page with listed items for sale and option to add likes to items on this page without entering the detailed part of the page (will consider if i need liking also inside detailed page) and the detailed product page with ability to add products in the shopping cart
- Messages to notify the user when he/she is logged in succesfully or made an order
- Add/ Update/ Remove product into the shopping cart
- Checkout page for reaching the payment and completing with stripe payments system


## Future Features

- Add pagination to macrame items page
- Ability to write responses to the reviews of users by the author

## Structure
# Skeleton
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

# Bugs and Issues

Naviagation Burger Bar - The navingation was working just fine but when I left the app for a while(Leave of Absence for work purposes) and came back to it, the navigation of burger button to turn into 'X' on opening of navigatrion started to go outside of the navigation bar, going to the left so I will have to explore as i have Javascript function to close navigation onclick when clicked outside of the navbar which might cause issues for this burger menu bar to be out of order.

I used another app similar to this to try and test out the CRUD functionality of reviews being created, Updated and Deleted, so before putting the code here i struggled with thecreate part as it was using forms in the case of tutorials I followed adn most helpful in this situation was [this one here](https://www.youtube.com/watch?v=EX6Tt-ZW0so&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=15), bug was that i could not make redirect url to go to the same page so i am exploring solution for this one.

I watched several tutorials on putting likes and dislikes and decided at the end I would not want to promote 'disliking' but focus more on 'liking so i made the funsction to be able to 'like' or if it is liked to 'unlike which does not show any 'dislike'. After testing it on another app in [this repository](https://github.com/totalnoMartina/macrame-shopping). Also here my redirect needs fixing, I am trying to find solution for the like to work without refreshing the whole page so stil lexploring this one.

I spoke to a fellow student Iulia Konovalova about Error pages and she recommended something like [this](https://github.com/IuliiaKonovalova/e-commerce/blob/main/ecommerce_project/views.py) and I am just now finding best way to test to see my error page, so still looking into this.
# Deployment

Github and Heroku - explain all steps
# Credits

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

I would like to thank to my mentor Tim Nelson, fellow students Iulia Konovalova and JoGorska, as well as the CI community and Slack community for the support and sharing the bugs and solutions that help each other grow, it is highly apreciated and forever remembered to be passed on to another student/fellow coder in the future.
