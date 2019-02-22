# M - Cart

Stream 4 Project : Fullstack Frameworks with Django - Code Institute.

This is a ficticious e-commerce website that sells winter wears for women. The products are divided into four categories. Jackets, Coats, Sweaters and Sweatshirts. 

### Demo

A live demo can be found [here](https://project4-m-cart.herokuapp.com/).

### UX 

Online shopping for dress is some thing very interesting to me. M cart is a shopping site for ladies winter wear. 

The site allows filtering of products by four categories and the brands that sell the products. The Products belongs to four main categories, Jackets, Coats, Sweaters and Sweatshirts.
No template was used to build this site. There were some specific UX and UI designs that were taken into consideration when styling this site. 

The navigation bar contains a logo for the site and its name M-cart, Then a dropdown SHOP which on hover displays all four categories of products. onclicking one of the categories will take to Products list in that categorie.
When customer is not logged in there will be a dropdown with a user icon which on hover shows SignUp and Login, onclicking one of them will take to appropriate forms.
if the customer is logged in The navebar will show the user name and Logout button. The last thing in the nav bar is the bag. which shows the number of items in the bag if we have added something. Onclicking the bag we can see the details of products 
added in the bag we can also remove the items if we wish so. 


The user can login as Admin or a customer. A customer can signup or Login to to the M cart account and do shopping, if logged in as admin has more authorizations.  

Customer can view all the products with out logging in but to review or to place order one have to login. The review featur is not displayed in mobile view

Admin can add, delete and edit a product. Admin can also add more image for the product through admin pannel.

In Product list all products are displayed as thumpnails which contains an image , name of Product its brand and price. onclicking which will take to product details page.
The product details page contains the product image, image slide show, name of product,price, brand,Product discriptions, available sizes, size chart, review if any and if the user is logged in he/she can write a review.
The Place order button takes to place order / Checkout page which shows the total amount, quantity, and product image and product details, of product user is about to order and a form to give user delivery details and card details.

The footer has a small discription about the website, the social website account of the site, Products return and delivery details.

### Technologies Used

* HTML
* CSS
* Bootstrap
* Python3
* Django2 Framework
* Javascript
* Jquery
* SQLite Database
* Stripe Payment

### Development Process

The backend was done first, with the styling added after. As styling was almost finished there were some back-end additions that needed to be made for testing 

One the styling was looking the way I wanted, I started working on the responsiveness of the website in tablet and then in mobile and completed one by one.

### Testing

#### Automated Testing

All automated testing was done using Travis-CI. There is automated testing done for all apps with views, models, and forms (where applicable). The testing currently provides 78% coverage
for the app. There is quite a bit of repetition in the testing.

Coverage was tested by running the following in the command line: 
```
$ sudo pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html
```
A htmlcov folder will be created now. By running 'htmlcov/index.html' we will be able to see the coverage.

#### Manual Testing

Manual tests were also done to ensure links,form submissions,Models, stripe payments etc are working correctly.

Manual testing was done to ensure:

+ The site works as intended.
+ Logging in and out and registering works as intended.
+ The place order page is not accessible if no items are in the cart.
+ Only admin can edit delete and add a product.
+ Reviwes can only be written if the user is logged in.
+ Models applied for size Chart and image slideshow is working correctly.

##### Links

All the links included in the website have been tested and they are all working.

##### Effects

Hover effects on icons, links, images and cards have been tested and they all have a hover effect working as expected.

##### Responsive 

The website have been tested in different viewports and it is responsve.

### Features

+ Users can easily register, log in and log out.
+ A user must be logged in to review and to order a product.
+ Users can easily add items to a bag.
+ The image for the bag in the navbar will display the amount of items currently in the bag.
+ Users can enter address and card information for making purchases.
+ While making payment the order details are available on screen and user can remove the item if they wish.
+ Payment processing via stripe.
+ Users can easily navigate through the products via brand and categories.
+ User can select the size they needed in S, M, L, XL format.
+ A size Chart is avilable as model which displays size in inches.
+ More images of the Products are displayed as Model slide shows.
+ Reviews about the product can be viewed, User can review if logged in.

#### Features Left to Implement
+ Enable users to view previous purchases.
+ Enable users to create an address book so they do not have to enter address information every time they purchase items.
+ Enable users to edit the product requirement in bag and in place order sections.
+ Sending email confirmation upon succesful purchases.
 
### Deployment 

The M - cart site is hosted on heroku.
Static assets are hosted on Amazon S3.

### Credits 

##### Media 

All images and contents have been obtained through different searches through [Google](www.google.com) and [Myntra](https://www.myntra.com/).

##### Acknowledgements

Design of the site was based on [Myntra](https://www.myntra.com/).
