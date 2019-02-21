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

