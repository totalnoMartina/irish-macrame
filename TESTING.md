# Testing


* [Testing](#testing)
   * [Manual Testing](#manual-testing)
   * [Lighthouse](#lighthouse)
   * [Bugs and Issues](#bugs-and-issues)
## Manual Testing

- [Lighthouse](toohttps://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) to audit the site (efficiency).

- [Validator](https://validator.w3.org/)

- [Jigsaw](https://jigsaw.w3.org/css-validator)


- Google chrome dev tools were used all the way, to find bugs and fix most of them. The one that stayed is possibly caused by webhooks as I had them and then removed them so I am not retrieving information on order from admin panel (Django admin built-in)
Regarding manual testing, there are things that are checked by a few good friends of mine and me, and these are:
   * Sign Up				
      1.	Click on Sign Up button =	redirect to Sign Up page= = Y	
      2.	Click on the Login link in the form	= redirect to Login page = Y	
      3.	Enter valid email once	= field will only accept email address format	Y	
      4.	Enter valid password 1 time = field will only accept password format =	Y	
      5.	Click on Sign Up button	asks user to confirm email page = sends address a confirmation request email	= N- deactivated confirming Email adress as I would figure if one wants to signup they wil try again putting the correct one, maybe this was not the best idea but I find it too demanding sometimes when trying to signup and it is not appealing for me to have to confirm the emails, I would rather to have the time to put 2-step verification with a phone number and a one-time code to enter maybe with authenticator
	
      6.	Sign In = redirects user to Homepage =	Y	 
      7. Sign In with the same email/username and password	= takes user to Homepage  with pop-up confirming successful sign in =	Y	
      8.	Click "Logout" button in the center of the page	Redirects user to home page	= Y	
   * Logging In				
      1.	Click on Log In button	= redirects  to Log In page =	Y	
      2.	Click on the Sign Up link in the form	= redirect to Sign Up page	= Y	
      3.	Enter valid email	Field will only accept email address format	= Y	
      4.	Enter valid password	= field will only accept password format	= Y	
      5.	Click on Log In button	= redirects user to blank In page	= Y	
      6.	Click logout button	= redirects user to home page	= Y		
      7.	Click Remember Me checkbox	= remembers user	= Y	
      8.	Click logout button	= redirects user to home page	= Y	
   * Navigation				
      1.	Click on the logo	= redirects to the home page	= Y	
      2.	Click 'Browse Now' to check items in the shop =	redirects to Macrame-detailed items page	= Y	
      3.	Click cart icon button	= redirects to shoppingcart page	= Y	
      4.	Click My Profile button	= redirects to Profile page	Y	
      5.	Click Logout button	= redirects to logout page	= Y
   * Macrame Selection - Irish Macrame Shop				
      1.	Type in search bar = search results are displayed	and keywords of decription are taken into consideration = Y	
      3.	Click on like button	= Macrame is with 'heart-like' and message will appear to notify user	= Y	
      If user is logged out, the user will see a message to login and the click will be ignored
		If user is logged out, the user will see a message to login and the click will be ignored
      4.	Click on the macrame item = user will be redirected to the macrame details page	= Y	
      5.	Click on page navigation = users will be redirected to the correct page =	Y
      I tried making navigation more interesting a few times, but it kept breaking so I stayed with bootstrap one, to try keep it simple and wanted to make sure it works properly first
      6. Add Reviews in macrame-details page = only for users that are logged in, if not, users will be asked to signup/ login first and the message will pop up = Y
      7. Update Reviews by only superuser = when another user(not a superuser), only ability to post reviews, and if written in url to edit or update, message pops up saying 'only store owners can do that'
      8. Delete Reviews = superuser might want to delete a review but one thing is missing here is , ther is no checking again if users are sure to delete a review, so i might need to put more protective programming for this feature
   * My Profile 
      1. My profile page = for all logged in users to be able to update their own information = Users to be able to upload an image also =  Yes(Needs improvement in image-avatar for users)
      2. Edit/Delete Account = users should be able to delete their account, and as I did not make this possible for everyone, for the moment only admin has the power to do this = No
      3. Store my Orders = users are able to see what orderes have they had and paid = Y
   * Shopping Cart
      1. Shoppingcart when it is empty, users are redirected to a page that states: 'Your cart is empty! and a 'back to browsing macrame' page = yes
      2. Adjust items in the shopping bag with Update/remove item = users tays on the page and the number of item reloads or dissapears if selected 'Remove'
      3. Secure Checkout button - redirects user to checkout page to make a payment = Y
      4. Checkout Success = users are redirected to a succesfull pop message on a page with details on the code number of the order and message that we will contact user by email within 48 hours, so that the user is aware what order is this with these 2 details = Y
   * Admin Macrame add items - Manage Stock
      1. Only for admin user - ability to add items, edit them and delete, when added admin is redirected to macrame detail page = Y
      2. Check before deletion - admin should be wanred before deleting anything so this is not implemented right now but kept for future feature = N
## Lighthouse

The app is extensively tested for validating all forms in all crud functionality, to make sure only authenticated/superusers can reach certain pages. I used Iphone7 Safari Browser, and Chrome Browser on Chromebook, Linux OS - Debian. I meant to install Ecosia to test it for browser Compatibility and it crashed so I did not have working Ecosia Browser. There is implementation of protective programming which was highly recommended by Iulia Konovalova, a fellow student and a friend, who is the best at testing my apps. Also great help in testing and helping discouver css and targeting bugs, was Iulia's husband Alex Konovalov, who made his own 'Allauth-system' for his app and is constant inspiration for me. This project inspired me to even more get into hackathons and get into creating useful applications that this world can benefit from. And Django has become my number 1, so I am really working to improve my coding skills by making small projects.

Homepage 
![Homepage](/media/homepage-lighth.png?raw=true)

Profile Page
![Profile Page](/media/profile-light.png?raw=true)

Macrame Selection 
![Macrame Selection](/media/macrame-selection-light.png?raw=true)

Edit Macrame Item
![Edit Macrame](/media/editing-mac-light.png?raw=true)

Checkout Success
![Checkout Success](/media/checkout-success-light.png?raw=true)

Checkout
![Checkout](/media/checkout-light.png?raw=true)

Add Macrame Page
![Add Macrame Page](/media/add-mac-light.png?raw=true)

# Manual Testing

* This application is tested on Chromebook; Chrome is made possible by the [Chromium](https://www.chromium.org/chromium-projects/) open source project and other open source software.
ChromeOS is made possible by additional [open source](chrome://os-credits/) software, as is [Linux development environment](chrome://crostini-credits/).

* This application is tested on iPhone 7, Safari IOS 15.6.1 Browser



# Bugs and Issues

Navigation Burger Bar - turns to X on opening - The navigation was working until I left the app for a while(Leave of Absence for work purposes) and came back to it, the navigation of burger button to turn into 'X' on opening of navigation started to go outside of the navigation bar, going to the left so I explored how to fix, there was also Javascript function to close navigation onclick when clicked outside of the navbar which caused issues for this burger menu bar to be out of order. I decided to drop it altogether and go simple as possible I used NavBar from Bootstrap4.

I used another repository to try functions before i use them, as I was affraid to crash another app, [the-macrames repository](https://github.com/totalnoMartina/the-macrames) similar to this to try and test out the CRUD functionality of reviews being created, Updated and Deleted, so before putting the code here i struggled with the create part as it was using forms in the case of tutorials I followed and most helpful in this situation was [this one here](https://www.youtube.com/watch?v=EX6Tt-ZW0so&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=15), bug was that i could not make redirect url to go to the same page so i asked for help on Slack and Stackoverflow.

I had a bug for a while, or that I thought it was a bug, showing 404 error when on homepage, but I went to check on Slack and it turned out that I only needed to clear cache and it would render without issues, also incognito works perfect. 

I watched several tutorials on putting likes and dislikes and decided at the end I would not want to promote 'disliking' but focus more on 'liking' so i made the funsction to be able to 'like' or if it is liked to 'unlike which does not show any 'dislike'. After testing it on another app in [this repository](https://github.com/totalnoMartina/macrame-shopping). Also here the redirect needed fixing.

I tryed to test newsletter app in [this repo](https://github.com/totalnoMartina/the-macrames) as I want to make sure something works before I include it in my project as I have crashed so many apps during developing this one. At the moment it is not commited as I am having small issues figuring it out in the most simple way. I might need help from my mentor about this as I got the impression that it is easy but then some tutorials have it quite a bit complicated, so I was exploring this through [this tutorial](https://www.youtube.com/watch?v=yZPgBThZT04&list=PLGzru6ACxEAKtb29AeyHbVGUh2-0r891H&index=27).

I spoke to a fellow student Iulia Konovalova about Error pages and she recommended something like [this](https://github.com/IuliiaKonovalova/e-commerce/blob/main/ecommerce_project/views.py) and I she helped me and explained finding best way to test to see my error page. She also helped in testing this apps features, so I really appreciate her and her husband Alex Konovalov's help in making sure my error page does show as i had actually renamed the variable that comes from the module that is called 'handler404' and this made an issue.

During payment process, message shows email confirmation will be sent but no email goes anywhere also, the order total is not rendering so it charged all zeros, I must check does it have anything to do with profile app that user information on charge is not maybe stored. I tried implementing webhooks and i can see payments in Stripe succesfull but not in webhooks, so I removed them.

Last minute bug appeared on an admin page, coming from Django admin, when chosen an order, it shows 500 error and the variable 'original_bag' was not found, and my variable is called 'original_shoppingcart'. So I am able to recall orders from Admin side when not on django admin, while in django official admin, past orders dont show up. I will put this into the 'Future Feature - Bug Fixes'.

Another last minute bug appeared on Update review page in my Safari mobile IPhone7 version(quite a small screen too), as the form is slightly overflowing the screen but not too much, the ability to fill out a form is still functional but i need to fix this when working more with django form rendering, item by item, so that i could better control the County field also and the fact that stars on reviews ar possible to go until any number, the reason why I did not target to limit this to be 6 stars as I wanted, I decided to leave these details for the time when I will have more time to learn more about detailed fomr handling in Django. 
Updated Bug: As doing the last check, putting a bootstrap class of mx-auto on form of Update Review, it centers it so nothing overflows. so Bug resolved almost.
