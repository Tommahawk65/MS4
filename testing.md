h1>Testing</h1>
# Code Validation

### HTML5
[W3C HTML Validator](https://validator.w3.org/#validate_by_input) Passed all tests.
![HTML Validator](/readme_assets/testing/html_validation.png)

### CSS3
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) No Errors.
![CSS Validator](/readme_assets/testing/css_validation.png)

### JS
[JSHint](https://www.jshint.com/) No Errors.

![Javascript Validator](/readme_assets/testing/js_validation.png)

### Python
[Python] Tested inside Gitpod. Minimal errors, those that arose were due to code institute project lessons.

# Features and Functionality

### Security Testing

- Website was tested on multiple devices.
- Tested to ensure unregistered users can't access user profiles.
- Tested to ensure add/edit/delete functions for products are only available to superusers.
- Tested to ensure add function of reviews are only available to registered users.
- Tested to ensure edit/delete function of reviews are only available to the author of review.
- Tested to ensure card validation works correctly.
- Error messages display when an error occurs on site.

### Responsiveness

- The responsiveness of this site was tested using an Apple MacBook Pro, an Ipad 2, an Iphone X, an Iphone XR, a Samsung notepad and a Windows laptop.

### New Users

All navigation and interaction work properly.

- Nav features were tested on multiple devices as they display differently depending on screen size.

Responsive on all devices.

- All pages were viewed to ensure everything renders in an acceptable way. Breakpoints all work as expected.

Navbar.

- Tested nav links in the same way as above. The navbar options should change depending on if you are logged in as well as if you are a superuser. These were checked to ensure they behave as expected.

Add a product.

- Superusers can add a product to the site.

Edit/Delete product.

- Super users are able to update any information about a product, they are also able to delete the product completely.

View/search products.

- This was tested on multiple devices; it should work the same regardless of whether you are logged in or not.

Register for account.

- Form validation works correctly ensuring the user entered a valid email. Once created the password is properly hashed and the details are stored on the database. The user receives an email that is required to verify the account.

Add product to basket.

- All users should be able to add products to their basket, a toast should appear instantly with information on the total price and bag contents, along with a button to continue to checkout.

- Clicking on the basket should give you a detailed view of its contents, along with a delivery price and the order total.

Checkout.

- Items in bag are transferred to checkout page, users will need to enter their delivery details and card information.

- I manually tested to ensure proper validation of all input felids, the card payment feild should only accept the Stripe test code.

- Users receive an email with the order detail upon a successful purchase.

- Past purchases are displayed properly on user profile page.


### Logged in user

User Profile.

- Logged in users can view their past orders and update their default delivery information.


Reviews.

- I checked to ensure reviews can only be added by logged in users. I also confirmed that only the author of the review can edit and delete it.

Logout.

- User is able to logout and is given access to reviews and their profile.

## Lighthouse Testing

![Lighthouse Test 1](/readme_assets/testing/Lighthouse_1.png)

![Lighthouse Test 2](/readme_assets/testing/Lighthouse_2.png)

![Lighthouse Test 3](/readme_assets/testing/Lighthouse_3.png)

![Lighthouse Test 4](/readme_assets/testing/Lighthouse_4.png)



## General Testing

* All internal page links work.

* External link works properly and opens on new tab.

* Pages/buttons hide/show as expected.

* All toast messages display correctly.

* Error pages display correctly on invalid input.

* 404 and 500 error pages show properly.