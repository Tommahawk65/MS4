
**Full Stack Frameworks with Django Milestone Project**
 
[Link to Live Website](https://guitar-boutique.herokuapp.com/)

[GitHub Repo]()

## Index – Table of Contents

* [User Experience (UX)](#user-experience) 
* [Features](#features)
* [Technologies Employed](#technologies-employed)
* [Database](#database)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


**Intro**



## UX

**Strategy**


**Scope**

## User Stories:

### Unregistered user goals

1. As a first time user, I want to easily understand the purpose of the website.
2. As a first time user, I want to be able to easily navigate throughout the site to find content.
3. As a first time user, I want to view all the items sold on the site, sorted by categories.
4. As a first time user, I want to be able to search the product range.
5. As a first time user, I want to be able to add items to my basket and receive feedback when I interact with the website.
6. As a first time user, I want to to edit and/or delete the items in my basket and receive feedback when something has changed.
7. As a first time user, I want to search the product range.
8. As a first time user, I want to be able to contact the site owners with and issues/queries.
9. As a first time user, I want to be able to visit the website on every device with formatting appropriate for all screen sizes.
10. As a first time user, I want to register an account on the website. 
11. As a first time user, I want to be able to buy items with a card. 
12. As a first time user, I want to be able to review items on the website.

### Registered user goals

1. As a returning user, I want to log in to my profile and update any personal information.
2. As a returning user, I want to see and review my past orders.
3. As a returning user, I want to be able to logout of my profile. 


### Admin

1. As a admin user, I want to be able to add, edit and delete items from the product range.
2. As a admin user, I want to see and review my past orders.
- As an admin user, I should be able to add, edit and delete items from the product range.
- As an admin user, I should have access to an admin section to see details of users and orders.




## Wireframes

#### Home Page
![Home Page](readme_assets/wireframes/homepage_wireframe.png "Homepage")

#### Product Page
![Product Page](readme_assets/wireframes/product_detail_wireframe.png "Product Page")

#### Bag
![Bag](readme_assets/wireframes/bag_wireframe.png "Bag")

#### Profile
![Profile](readme_assets/wireframes/profile_wireframe.png "Profile")


### Existing features 

#### Design 
- An attractive and simple layout with consistency.
- Simple navigation throughout the website by using the navigation bar. 
- Clear display of steps required to bake the recipe shown.
- Layout that fits with the design of a cookbook.

####  General 
- Responsive header that changes options if the user is logged in/out. 
- Contact info in footer. 
- Responsive on all devices and screen sizes. 
- Reactive elements that respond to user input (buttons). 

#### Recipes
- Recipes can be created, read, updated and deleted (CRUD) by the users that created them. 
- Recipes are displayed by category, this is displayed in the navbar.
- People can search for recipes. 
- Users can log onto their profile and view all recipes they have created. 
- Steps and ingredients can contain as many inputs as the user requires.

<span id="features-future"></span>

### Features left to implement in the future 
- Ability for users to like/favourite recipes and have that displayed on a separate page.  
- Direct file upload option for recipe image. 
- More defensive programming such as a confirmation message for recipe deletion.
- The user can delete their profile to remove their information from the database (Data Protection Laws).

# Database

### Schema
Below is the schema for my database, for the purpose of this assignment I used a NoSQL database structure with MongoDB. Some debate exists about the merits or Relational vs Non Relational databases and their suitability for projects such as this, however this was chosen based on the course structure.

The types of data stored in MongoDB for this project are:
-	ObjectId
-	String
-	Array

The schema contains three related tables, with all containing multiple documents.

#### Users
Collects the users name, email and password. Information is used for login on website. The name document is also accessed by the recipes collection to display user data.

#### Recipes
Displays all recipe information created by the user. The array inputs allows dynamic sizing as recipes don't have a standard number of steps or ingredients.

#### Category
Sets a general type of recipe to allow easier categorization.


#### Recipes

| Key                   |Value type     
|:-------------         |:------------- 
|_id                    |ObjectId       
|recipe_type            |string         
|recipe_name            |string         
|recipe_image_url       |string        
|recipe_prep_time       |string         
|recipe_cook_time       |string         
|recipe_description     |string         
|recipe_serves          |string         
|recipe_ingredients     |array         
|recipe_method          |array         
|username               |string         

#### Users

| Key                   |Value type     
|:-------------         |:------------- 
|_id                    |ObjectId 
|name                   |string        
|email                  |string         
|password               |string  


#### Category

| Key                   |Value type     
|:-------------         |:------------- 
|_id                    |ObjectId 
|category               |string        

## ERD
![ERD](readme_assets/database/ERD.png "ERD")

### Notes for improvement 

Ultimately the category table proved to not be useful in this application when writing the code, so it was largely unused. However for future expansion on this app, the ability for users to add new categories would not only make this more useful but give extra functionality too visitors of this website.

<span id="technologies"></span>

<h1>Technologies used</h1>


## Technologies Employed

*IDE*
* Gitpod

*Languages*
* Python
* HTML
* CSS
* JavaScript

*Frameworks, Templates & Libraries*
* Django
* JQuery
* Jinja
* Bootstrap
* Font Awesome
* Google Fonts

*Storage & Hosting*
* Heroku
* Github
* Amazon Web Services

*Databases*
* SQLite3 for development
* PostgresSQL for the deployed site

*Payment Service*
* Stripe

## Database

**Schema**

## Testing

The testing process can be found [here!](testing.md).

## Deployment

## Credits

**Content**

**Media**

**Code**

**Acknowledgements**
