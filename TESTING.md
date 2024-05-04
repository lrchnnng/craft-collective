[Return to README](https://github.com/lrchnnng/craft-collective/blob/main/README.md)

# Testing <!-- omit from toc -->
- [Automated vs Manual Testing](#automated-vs-manual-testing)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Known bugs and fixes](#known-bugs-and-fixes)

## Automated vs Manual Testing

## Manual Testing
### Responsivity
|Responsivity | Mobile S (320px)| Mobile L (425px)| Tablet (768px) | Desktop (1024px)|
|---|:---:|:---:|:---:|:---:|
|Responsive UI Components|✓|✓|✓|✓|
|Responsive Text|✓|✓|✓|✓|
|Responsive Forms|✓|✓|✓|✓|
|Responsive Button Placement|✓|✓|✓|✓|
|Responsive Nav Bar|✓|✓|✓|✓|
|Responsive Footer|✓|✓|✓|✓|

### Page Testing
|Nav Bar Testing|Yes/No|
|---|:---:|
|Nav bar test and styles are loaded||
|Mobile header appears up to medium sized screens||
|All nav links work as intended||
|Nav logo directs user to index page||
|If user logged in as admin, nav bar shows `Product Management`, `My Profile` and `Logout` links||
|If user is logged in but not admin, nav bar shows `My Profile` and `Logout` links||
|If user is not logged in, nav bar shows `Register` and `Login`||
|`home.` links to the index page||
|`who we are.` triggers a dropdown menu for `about us.` and `FAQ.`||
|`about us.` links to about us page||
|`FAQ.` links to FAQ page||
|`all products.` links to all products page||
|`bracelets.` links to bracelets category page||
|`earrings.` links to earrings category page||
|`necklaces.` links to necklaces category page||
|`rings` links to rings category page||
|In mobile view `search icon` triggers a drop down input field||
|`search bar` allows text input and searches products||
|`bag` total price updates when item is added to the bag and when clicked directs user to the bag page||

|Footer Testing|Yes/No|
|---|:---:|

|Toasts Testing|Yes/No|
|---|:---:|

|Allauth Testing|Yes/No|
|---|:---:|

|Index Page Testing|Yes/No|
|---|:---:|

|About Us Page Testing|Yes/No|
|---|:---:|

|FAQ Page Testing|Yes/No|
|---|:---:|

|All Products Page Testing|Yes/No|
|---|:---:|

|Product Detail Page Testing|Yes/No|
|---|:---:|

|Shopping Bag Testing|Yes/No|
|---|:---:|

|Checkout Page Testing|Yes/No|
|---|:---:|

|Profile Page Testing|Yes/No|
|---|:---:|

|Product Management Page Testing|Yes/No|
|---|:---:|

### User Story Testing

**Shopper**
1. I want to be able to view a list of products to purchase.
2. I want to be able to view products from a specific category.
3. I want to be able to view the details of individual products.
4. I want to be able to easily view the total of my purchases at an time.
5. I want to be able to sort the list of available products.
6. I want to be able to sort a specific category of product.
7. I want to be able to search for a product by name or description.
8. I want to be able to easily see what I've searched for and the number of results.
9. I want to be able to easily select the size, metal type and quantity of a product when purchasing it.
10. I want to be able to view items in my bag before purchasing.
11. I want to be abe to adjust the quantity of the individual items in my bag.
12. I want to be able to easily enter payment information.
13. I want to be able to feel my personal information is safe and secure.
14. I want to be able to view an order confirmation after checkout.
15. I want to be able to receive an email confirmation after checking out.

**Site User**
1. I want to be able to easily register for an account.
2. I want to be able to easily login or logout.
3. I want to be able to easily recover my password in case I forget it.
4. I want to be able to receive an email confirmation after registering.
5. I want to have a personalised user profile.

**Store Owner**
1. I want to be able to add a product.
2. I want to be able to edit/update a product.
3. I want to be able to delete products.

#### Viewing and Navigating
|User|I want to...|In order to...|Explaination|Image|
|---|---|---|---|---|
|Shopper|View a list of products|Select products to purchase|Explain|![Desc](link)|
|Shopper|View specific categories of products|Quickly find products I'm interested in without having to search through all products|Explain|![Desc](link)|
|Shopper|View individual product details|Identify the price, description, product image, available sizes and metal types|Explain|![Desc](link)|
|Shopper|Easily view the total of the purchases at any time|Avoid spending too much|Explain|![Desc](link)|

#### Registration and User Accounts
|User|I want to...|In order to...|Explaination|Image|
|---|---|---|---|---|
|Site User|Easily register for an account|Have personal account and be able to view my profile|Explain|![Desc](link)|
|Site User|Easily login or logout|Access my personal account information|Explain|![Desc](link)|
|Site User|Easily recover my password in case I forget it|Recover access to my account|Explain|![Desc](link)|
|Site User|Receive an email confirmation after registering|Verify that my account registration was successful|Explain|![Desc](link)|
|Site User|Have a personalised user profile|View personal order history and order confirmations, and save my payment information|Explain|![Desc](link)|

#### Sorting and Searching
|User|I want to...|In order to...|Explaination|Image|
|---|---|---|---|---|
|Shopper|Sort the list of available products|Easily identify the best rated, best prices and categorically sorted products|Explain|![Desc](link)|
|Shopper|Sort a specific category of product|Find the best-priced or best-rated products in a specific category, or sort the products in that category by name|Explain|![Desc](link)|
|Shopper|Search for a product by name or description|Find specific product I’d like to purchase|Explain|![Desc](link)|
|Shopper|Easily see what I’ve searched for and the number of results|Quickly decide whether the product I want is available |Explain|![Desc](link)|

#### Purchasing and Checkout
|User|I want to...|In order to...|Explaination|Image|
|---|---|---|---|---|
|Shopper|Easily select the size, metal type and quantity of a product when purchasing it|Ensure I don't accidentally select the wrong product, quantity, size or metal type.|Explain|![Desc](link)|
|Shopper|View items in my bag to be purchased|Identify the total cost of my purchases and all items I will receive|Explain|![Desc](link)|
|Shopper|Adjust the quantity of individual items in my bag|Easily make changes to my purchase before checkout|Explain|![Desc](link)|
|Shopper|Easily enter payment information|Check out quickly and with no hassles|Explain|![Desc](link)|
|Shopper|Feel my personal and payment information is safe and secure|Confidently provide the needed information to make a purchase|Explain|![Desc](link)|
|Shopper|View an order confirmation after checkout|Verify that I haven't make any mistakes|Explain|![Desc](link)|
|Shopper|Receive an email confirmation after checkout|Keep the confirmation of what I have purchased for my records|Explain|![Desc](link)|

#### Admin and Management
|User|I want to...|In order to...|Explaination|Image|
|---|---|---|---|---|
|Store Owner|Add a product|Add new items to my store|Explain|![Desc](link)|
|Store Owner|Edit/update a product|Change product prices, descriptions, images and other product details|Explain|![Desc](link)|
|Store Owner|Delete a product|Remove items that are no longer for sale|Explain|![Desc](link)|

## Automated Testing
### HTML Validation
|Page|Y/N|
|---|:---:|
|templates/base.html||
|templates/allauth/base.html||
|account_innactive.html|✓|
|templates/allauth/account/base.html|✓|
|email_confirm.html|✓|
|email.html|✓|
|login.html|✓|
|logout.html|✓|
|password_change.html|✓|
|password_reset_done.html|✓|
|password_reset_from_key_done.html|✓|
|password_reset_from_key.html|✓|
|password_reset.html||
|password_set.html|✓|
|signup_closed.html|✓|
|signup.html|✓|
|verification_sent.html|✓|
|verified_email_required.html|✓|
|main-nav.html||
|mobile-top-header.html||
|toast_error.html|✓|
|Ttoast_info.html|✓|
|toast_success.html|✓|
|toast_warning.html|✓|
|profile.html|✓|
|add_product.html|✓|
|edit_product.html|✓|
|products.html|✓|
|product_detail.html|✓|
|index.html|✓|
|about_us.html|✓|
|faq.html|✓|
|checkout.html|✓|
|checkout_success.html|✓|
|bag.html|✓|

### CSS Validation
|Source|Y/N|
|---|:---:|
|base.css||
|checkout.css||
|profile.css||

### Wave Accessibility Evaluation

### Python Testing 

## Known Bugs and Fixes
- Email confirmation not loading in terminal
    - Attempted to fix with try/except statements, printing the error in the terminal if there is an issue sending the email. 
        - No issues with sending the email detected but confirmation still not showing in the terminal.
    - Added a print statement to check that the _send_confirmation_email() function is being called
        - Statement not printed in terminal indicating an issue with the function being called and executed.
    - In python shell I tested the email functionality outside of the webhook handler context in order to isolate the issue. 
        - The confirmation email successfully printed in the terminal 