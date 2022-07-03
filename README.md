**Full Stack Frameworks with Django Milestone Project** 
 
![Responsive Mockup of site](readme_assets/responsive_site.png) 
[Link to Live Website](https://guitar-boutique.herokuapp.com/) 
 
## Project goals  
 
The goal of this project was to create an interactive web store for musicians and guitar lovers to buy and explore products. This site should be easy to navigate and appealing to the target audience. 
 
## User Stories: 
 
### Unregistered user goals 
 
1. As a first time user, I want to easily understand the purpose of the website. 
2. As a first time user, I want to be able to easily navigate throughout the site to find content. 
3. As a first time user, I want to view all of the items sold on the site, sorted by categories. 
4. As a first time user, I want to be able to search the product range. 
5. As a first time user, I want to be able to add items to my basket and receive feedback when I interact with the website. 
6. As a first time user, I want to edit and/or delete the items in my basket and receive feedback when something has changed. 
7. As a first time user, I want to search the product range. 
8. As a first time user, I want to be able to contact the site owners with any issues/queries. 
9. As a first time user, I want to be able to visit the website on every device with formatting appropriate for all screen sizes. 
10. As a first time user, I want to register an account on the website.  
11. As a first time user, I want to be able to buy items with a card.  
12. As a first time user, I want to be able to review items on the website. 
 
 
 
### Registered user goals 
 
1. As a returning user, I want to log into my profile and update any personal information. 
2. As a returning user, I want to see and review my past orders. 
3. As a returning user, I want to be able to logout of my profile.  


 
### Admin 
 
1. As an admin user, I want to be able to add, edit and delete items from the product range. 
2. As an admin user, I want to see and review my past orders. 
3. As an admin user, I should be able to add, edit and delete items from the product range. 
4. As an admin user, I should have access to an admin section to see details of users and orders. 


 
## Design  
 
- ### Colour scheme  
I used a dark background contrasted with white text to give a modern look to the website. 
 
- **The black colour** is used in the background image.  
- **The white colour** is used in most of the text for the site to achieve the desired contrast.  
- **The grey colour** is used in product cards and title backgrounds to add interest to images and frame them in a visually appealing way.  
 
- ### Fonts 
I chose the Koulen font as after much testing in my wireframes, I felt it suited the site best for achieving a modern yet rustic design to my site. 
 
- ### Icons 
The icons used are all font awesome icons. I chose this library due to its large selection of choices.  
 
- ### Images 
The images I used for this project came from [PNG Item](https://www.www.pngitem.com/). These images are used on all the product cards, as I wanted images with no background to fit in with my cards.  
 
## Wireframes 
 
### Home Page 
![Home Page](readme_assets/wireframes/homepage_wireframe.png "Homepage") 
 
### Product Page 
![Product Page](readme_assets/wireframes/product_detail_wireframe.png "Product Page") 
 
### Bag 
![Bag](readme_assets/wireframes/bag_wireframe.png "Bag") 
 
### Profile 
![Profile](readme_assets/wireframes/profile_wireframe.png "Profile") 


 
## Existing features  
 
### Design  
- An attractive and simple layout with consistency. 
- Simple navigation throughout the website by using the navigation bar.  
- Product information displayed clearly on each items page. 
- Consistent design throughout. 
 
### General  
- Responsive header that changes options if the user is logged in/out.  
- Contact info in footer.  
- Responsive on all devices and screen sizes.  
- Reactive elements that respond to user input (toasts/buttons).  
 
### Products 
- Products can be created, read, updated and deleted (CRUD) by the site admin.  
- Products are displayed by category; this is displayed in the navbar. 
- Users can search for products.  
- Users can view information about each product along with reviews. 
 
### Bag 
- Users can add/delete items to the bag.  
- Users can update product quantity in the bag. 
- Users can see the total price of the order.  
- Users can continue browsing the site while the bag is stored. 
 
### Checkout 
- Users can input their delivery information into the checkout.  
- Card payments are accepted via Stripe. 
 
### Profile 
- Users can store their personal information in the profile page.  
- Previous orders can be viewed. 
 
#### Reviews 
- Registered users can add reviews to products. 
- The author of the review and edit/delete the review.  
 
### Contact 
- Users can submit a contact form in case they need to get in contact with the storeowner. 


 
### Search functionality 
- Users can search all products on the site by name, description or category. 
 
### Toasts 
 
- Toasts are popups to give users instant visual feedback when they interact with the website. 
- They can also be used to contain information about the current basket, or give error/warning messages. 


### Django-allauth feature 
 
- Allauth is a Django extension that allows easy user authentication for this website. 
- Templates for logging in a resetting passwords were pre made and customized to match the website. 
 
### Automatic e-mails 
 
- Emails are sent to the user for the purpose of account authentication, order confirmation and contact form confirmation. 
 
### Features left to implement in the future  
- Newsletter to allow constant updates for registered users.  
- The user can delete their profile to remove their information from the database (Data Protection Laws). 
- Ability to show stock levels of products in real time. 
- Full card functionality, Stipe is currently in test mode. 
 
## Database 
 
### Schema 
Django uses SQL databases by default. I was using SQLite in development. In Heroku once deployed it switches to a PostgreSQL database for deployment, which was hosted by AWS. 
 
The schema contains many related tables, large proportions are created by Django and Allauth by default, below I have described those created custom by myself. 
 
#### Product Review 
Takes in the username of the current logged in user and creates a review connected to the currently viewed product. 
 
#### Product 
Collects all products available on the site, contains information on name, description, price, sizes and image. 
 
#### Category 
Sorts the products into separate types to allow easier navigation for the user. 
 
#### Order 
Stores all past orders of each user’s, which can be accessed later. 
 
#### User Profile 
Collects the username and email for the purpose of login authentication and applying to orders and reviews. 
 
#### Contact 
Stores messages sent by users to the site admin 

### ERD 
![ERD](readme_assets/database/ERD.png "ERD") 
 
## Technologies 
 
The website is designed using the following technologies: 

### Programming languages 
 
- HTML - the project used HTML to define structure and layout of the web page. 
- CSS - the project used CSS style sheets to specify style of the web document elements; 
- JavaScript - the project used JavaScript to implement Stripe, EmailJS and custom Javascript. 
- Python - the project back-end functions are written using Python. 
 
### Libraries 
 
- [Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome icons were used throughout the website. 
- [jQuery](https://jquery.com/) - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation. 
 
### Frameworks & Extensions 
 
- [Django](https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
- [Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages. 
- [Stripe](https://stripe.com/ie) – Allows individuals and businesses to make and receive payments over the Internet. 
 
### Database 
* [Heroku Postgres](https://www.heroku.com/postgres/) – PostgreSQL is one of the world's most popular relational database management systems. 
 
### Others 
 
- [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git. 
- [Gitpod](https://gitpod.io/workspaces/) - One-click ready-to-code development environments for GitHub. 
- [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies’ build, deliver, monitor and scale apps. 
- [AWS-S3](https://aws.amazon.com/s3/) – Object storage service that offers industry-leading scalability, data availability, security, and performance. 
 
## Testing 
 
**Testing section is located [here](/testing.md)** 

## Deployment 
 
The following steps were taken throughout the project to achieve deployment of the live site. 
 
### Create Github Repository 
 
- The repository was created using the green 'new' button on Github and selecting the Code Institute Full Template from the dropdown menu.  
 
### Django

In the terminal type the following commands to create and initialize the project: 
- Install Django 
``` 
pip3 install django 
``` 
 
- Create project-level application 
``` 
django-admin startproject [project_name] . 
``` 
 
- Create Super user to access the Django admin panel. Follow the prompts to input a username, email and password. 
 
``` 
python3 manage.py createsuperuser 
``` 
- Install apps to implement site features. 
 
``` 
python3 manage.py startapp [app_name] 
``` 
 
### Heroku

•	Go to [Heroku](https://www.heroku.com)

•	Create an account if you don’t have one already, log in if you do

•	Create a new app, making sure to use only lower case letters and no spaces for the name

•	Choose the region closest to you and select “Create App”

•	When the app has been created, click on the “Resources” tab to add the Postgres database

•	Type in “Heroku Postgres” and select it from the dropdown list

•	This will automatically create a DATABASE_URL variable in Heroku Config Vars which can be found by clicking on the “Settings” tab, and clicking the “Reveal Config Vars” button

•	Go to the “Deployment” tab to set automatic deployments when pushing to GitHub

•	Set the deployment method to “GitHub” and search for your repository

•	Click “Connect”, then “Enable automatic deployments”

•	Back in your IDE, install both `dj_database_url` and `psycopg2-binary` in order to use Heroku Postgres

•	In your `settings.py` file, comment out the existing sqlite DATABASES and add the following code;
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }   

```

•	Login to Heroku within your IDE by typing `heroku login –i`

•	Once logged in, you will need to run migrations to migrate your models to Postgres;

•	In the terminal, enter `heroku run python3 manage.py migrate --plan` to show what will be migrated

•	If you are happy with the migrations, enter `heroku run python3 manage.py migrate`

•	Make sure to also create a super user so you can access the admin page by entering `python3 manage.py createsuperuser`

•	Create a `requirements.txt` file and a `procfile`

•	Install `gunicorn` and make a create your `requirements.txt` by entering `pip3 freeze > requirements.txt` in your terminal

•	Create a `procfile` by entering the following into your terminal;

`web: gunicorn name_of_your_app.wsgi:application`

•	Once this is done, `add`, `commit` and `push` your changes to GitHub

### Environment Variables

#### GitPod IDE

``` 
| Key                   | Value                            |
|-----------------------|----------------------------------|
| AWS_ACCESS_KEY_ID     | ## YOUR AWS_ACCESS_KEY_ID ##     |
| AWS_SECRET_ACCESS_KEY | ## YOUR AWS_SECRET_ACCESS_KEY ## |
| DATABASE_URL          | ## YOUR DATABASE_URL ##          |
| DEVELOPMENT           | True                             |
| EMAIL_HOST_PASS       | ## YOUR EMAIL APP PASS CODE ##   |
| EMAIL_HOST_USER       | ## YOUR EMAIL ADDRESS ##         |
| SECRET_KEY            | ## YOUR SECRET_KEY ##            |
| STRIPE_PUBLIC_KEY     | ## YOUR STRIPE_PUBLIC_KEY ##     |
| STRIPE_SECRET_KEY     | ## YOUR STRIPE_SECRET_KEY ##     |
| STRIPE_WH_SECRET      | ## YOUR STRIPE_WH_SECRET ##      |
``` 

#### Heroku

``` 
| Key                   | Value                            |
|-----------------------|----------------------------------|
| AWS_ACCESS_KEY_ID     | ## YOUR AWS_ACCESS_KEY_ID ##     |
| AWS_SECRET_ACCESS_KEY | ## YOUR AWS_SECRET_ACCESS_KEY ## |
| DATABASE_URL          | ## YOUR DATABASE_URL ##          |
| EMAIL_HOST_PASS       | ## YOUR EMAIL APP PASS CODE ##   |
| EMAIL_HOST_USER       | ## YOUR EMAIL ADDRESS ##         |
| SECRET_KEY            | ## YOUR SECRET_KEY ##            |
| STRIPE_PUBLIC_KEY     | ## YOUR STRIPE_PUBLIC_KEY ##     |
| STRIPE_SECRET_KEY     | ## YOUR STRIPE_SECRET_KEY ##     |
| STRIPE_WH_SECRET      | ## YOUR STRIPE_WH_SECRET ##      |
| USE_AWS               | True                             |
``` 
 
### Amazon Web Services (AWS) 
 
Amazon Web Services was used to host the static files and media files for the site. 
 
- Follow the steps on the [AWS website](https://aws.amazon.com/) to create a new account and sign in. 
 
- Search for and navigate to the S3 service and follow the following steps to create a new 'bucket' 
- In the S3 dashboard, click the 'create bucket' button. 
- Give the bucket a name, select the region nearest to your location and un-check the 'block public access' settings checkbox. 
- Hit 'create bucket' 
 
- Configure the properties for the bucket. 
- In the properties tab of the bucket, navigate to the 'Static website hosting' section and click edit. 
- Enable Static website hosting using the checkbox. 
- Input the default index and error documents as 'index.html' and 'error.html'. 
- Save changes. 
 
- Configure the permissions for the bucket. 
- In the permissions tab of the bucket. 
- Select edit in the Cross-origin resource sharing(CORS) section and 
pPaste the following code into the CORS configuration section. 
``` 
[ 
{ 
"AllowedHeaders": [ 
"Authorization" 
], 
"AllowedMethods": [ 
"GET" 
], 
"AllowedOrigins": [ 
"*" 
], 
"ExposeHeaders": [] 
} 
] 
``` 
- Back in the permissions menu, hit edit on the bucket policy section and select 'generate policy'. 
- Select policy type of 'S3 bucket policy' 
- Allow all principles by entering a '*' in the Principal field. 
- Select 'get object' from the action dropdown. 
- Copy the 'arn' from the edit bucket policy page and paste into the Amazon Resource Name (ARN) field. 
- Click 'add statement' 
- Click ‘generate policy’ and copy the code. 
- Paste the code into the policy field in the edit bucket policy section, adding a '/*' to the resource line. 
- Hit save. 
 
- Navigate to the 'edit access control list (ACL) section and grant 'list' access for everyone by selecting the checkbox. 
 
- Create a user to access the S3 bucket using IAM. 
- Navigate to the IAM page from the AWS dashboard. 
- Create group. 
- Select 'group' from the menu and click to create a new group, following the instructions to name and then create. 
- Create policy 
- Select 'policies' from the menu and click 'create policy'. 
- Select the 'JSON' tab and click 'import managed bucket'. 
- Search for, and import the 'S3 full access' policy. 
- Copy the ARN from the bucket policy section and paste this in as the 'Resource' value. 
- Click 'review policy' and give it a name and description and hit 'create policy. 
- Add policy to group. 
- Navigate to the group’s menu and select the group. 
- Click 'attach policy', search for the newly-created policy from the previous step. 
- Select the policy using the checkbox and click 'attach policy' 
- Create user 
- Select 'users' from the menu and click 'add user'. 
- Name the user and grant programmatic access using the checkbox. 
- Select the group created in the previous steps. 
- Click through to the end of the options and click 'create user' 
- Download and save the user CSV file. 
 
- Connect Django to S3 
- Install packages Boto3 and Django storages and add to our requirements.txt file. 
``` 
pip3 install boto3 
``` 
``` 
pip3 install django-storages 
``` 
``` 
pip3 freeze > requirements.txt 
``` 
- Add 'storages' to the installed apps in settings.py. 
- Add the following settings to settings.py. 

```python
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'guitar-boutique'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
``` 
 
- Create custom_storages.py at the top-level of the project and input the locations for Django to store the files. 

```python 
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
``` 
 
- With all these settings complete, remove the 'DISABLE_COLLECTSTATIC variable from Heroku and AWS is ready to use. 
 
- Add media to AWS 
- Navigate to the S3 bucket on the AWS site. 
- Click to create a new folder and name it 'media' 
- Within the folder, click the button to upload files and add any relevant site media. 
- Under permissions, select to grant public read access. 
 
## Credits
 
- All Product images are from (https://www.pngitem.com/) 
 
- [Bootstrap](https://https://getbootstrap.com/): Bootstrap has been used throughout this project. I have taken examples from the website to form the grid layout, carousel, forms, buttons, navbar and footer. 

- Product descriptions taken from (https://www.andertons.co.uk/) 
 
- Background image from (https://wallpapercave.com/black-website-background) 
 
## 7. Acknowledgements 
 
- My Mentor for continuous helpful feedback. 
- Tutor support at Code Institute for their support. 