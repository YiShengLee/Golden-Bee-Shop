# <span style="color:rgb(224,162,0)">Golden Bee Store</span>
Project 4: FullStack Final Project  
Done by: Lee Yi Sheng

![Main Picture](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/main.png)

This **GoldenBeeStore** is a website for users who are looking to view and purchase raw organic honey.

Golden Bee Store: [Click here to visit GoldenBeeStore](https://golden-bee-honey.herokuapp.com/)

## Table of contents
1. #### [Introduction](#introduction)
2. #### [User Stories](#userstories)
3. #### [UX](#UX)
4. #### [Wireframes](#wireframe)
5. #### [Features](#features)
6. #### [Technologies Used](#technology)
7. #### [Future Features to Implement](#implement)
8. #### [Testing](#testing)
9. #### [Deployment](#deployment)
10. #### [Credits](#credits)

<br>

## 1.0 Introduction <a name="introduction"></a>
Golden Bee Store is a website created for users who are looking to view
and purchase honey. A new user could register for a new account, login, 
change or reset a password, view his/her profile and logout. 
The user could also search for honey by name or a category. 
A logged in superuser has extra game CRUD rights which allow him/her 
to add a game, edit the game's record and even delete it from the database.  

Please register as a new user or use the following account to navigate around the shop:

To log in as a user, please use the following Username & Password:
```
Username: BumbleBees
Password: Freebee123!
```

To log in as a superuser or admin, please use the following Username & Password:
```
Username: WallaceGiantBee
Password: Beezy123!
```

The deployed website used Heroku: [Click here](https://golden-bee-honey.herokuapp.com/)  

The repository can be found in Github: [Click here](https://github.com/YiShengLee/Golden-Bee-Shop)

## 2.0 User Stories <a name="userstories"></a>  
As a user, someone who like to buy raw and organic honey and found this website. I'd like to see:  
- A professional, modern and clean looking website to attract me to continue clicking on the other features
- Easy to navigate around the website and point to the correct pages
- Able to search honey by name or category
- Buttons which are straightforward in their purpose that allow me to view more information or do an action
- SuperUser have full control of adding, viewing, editing and deleting honey product
- Normal user & and superuser able to add honey product to cart, checkout and make payment with credit card
- The ability to register an account, login, logout, change password, reset password and view my profile details

## 3.0 UX <a name="UX"></a>  
**User Experience**  
This project I started with mobile first design approach. 
I started creating mockups wireframe on powerpoint for mobile only. 
The design of the site is fully design by myself, showcasing smooth 
layout and interactive for most devices. Milstones had to be set in 
order to finish this project Below are steps by steps of the journey 
that required to be achieved for this website.

1. User are welcomed with a simple and refreshing front page with caurosel image. A slogan is shown on each picture.
2. Eye-catching icon of all the buttons to further enhance the website's purpose.
3. On larger screens, there are options on top of the navigation page for easy navigation. On smaller screens, a hamburger will be formed on the right hand side of the website.
4. A search function is provided on top the product section t0 enable users to search for honey product by name or category.
5. If the user venture into a invalid section of the website, a error page will display.
6. Flash messages are displayed on top of the home page (below the navbar) for certain successful or not successful actions such as adding to cart, removing from cart, logged in, etc.
7. Users are able to add honey product to cart if they would like to purchase it.
8. In the 'cart' page, a display of honey is available. Users are able to add or reduce the quantities they would like to buy. Grand total amount will be automated calculated and display the amount.
9. If the user clicks on the 'PROCEED TO CHECKOUT' button, a form is displayed asking for the user to fill in the particulars for delivery. On the click of the 'SUBMIT PAYMENT' button, payment is made and this is verified with a 'tick" image when payment is successful.
10. For superusers, a form is provided in the 'Add Product' page where the user could fill up and add a honey product to the catalogue. The asterisks (*) imply that the fields are required to be filled before form submission.
11. User are required to fills in all the fields and select a image to upload upon clicking on the "Add Product" button, user will then be brought to the "shop" page where the latest added honey product will be displayed. Do note that each image upload must not **exceed** 1MB to be able to upload the image successfully.
12. To view more information of a honey product, click on the picture or click "more description" button.
13. If user would like to edit product, click on the "Edit honey" button to display the form and edit the information and submit. The honey product edited will then be updated.
14. The edit form is pre-filled with the original entries of the user for easy reference. Ensure to click the submit button to ensure your new information is saved.
15. User could also delete the honey product by clicking on the "Delete" button. A modal pop-up is being used to ensure that user conform deleting the honey product. 
16. If a user is logged in, a 'Your Profile' link is available for the user to check his/her username and email address. There is also options for the user to reset or change his/her password.
17. If a user is logged in, a 'LOGOUT' link is available for the user to log out.
18. If a user is not logged in, he/she could register an account with the 'REGISTER' link on the navbar. Thereafter, there is the option to login with clicking on the 'LOGIN' link.
19. If there are any errors in finding a page, the user would be brought to an error 404 page where user can return to the homepage page.
20. If there are any internal server errors along the way, the user would be brought to an error 500 page where the same sad cat image would be displayed. There is a button for the user to click to go back to the homepage.

## 4.0 Wireframes <a name="wireframe"></a>
Wireframes were created initially to help me vsualise the website in different sized screens. Initial planning was done on how to setup the database and the website. I used Microsoft Word to sketch out this ER diagram.

![Wireframes](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/wireframe.PNG)

## 5.0 Features <a name="features"></a>  
1. **Home Page (Golden Bee Store)**  

![Wireframes](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/home_page.png)
- When the user first arrives at the page, he/she is welcomed with a large carousel picture in the center, signifying that this website is about honey
- An navigational bar with a logo of a bee in a hive with links to the other pages are provided. For the mobile devices, the links are presented when the user clicks on the 'hamburger' icon of 3 horizontal lines
- There is a slogan for each carousel picture, with a "Shop Here Now" button to link user to see honey product
- At the bottom of the page, there is a footer in the honey-like color with clickable icons to link to various personal social media platforms, Github repository and LinkedIn sites if anyone would like to contact me. There are some links to important information pertaining to having legal implications that the user may be in interested in. **Disclaimer** that this website is meant for educational purposes only

2. **Add a Honey Product**

![Add Product](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/add_product.PNG)
- Available from a link on the navigation bar. This feature is available for superusers when logged in. A form is available for the user to input all fields, which are all required, and an image upload feature as a whole package for this game to be saved. Do take note that each image must not exceed 1MB to be able to be uploaded successfully

3. **Edit a Honey Product**



4. 



## 8.0 Testing <a name="testing"></a>
A full testing process can be found in a separate [tests.md](https://github.com/YiShengLee/Golden-Bee-Shop/blob/master/tests.md) file.




## 9.0 Deployment <a name="deployment"></a>
The project was built using [AWS Cloud9](https://aws.amazon.com/cloud9/).  
:heavy_exclamation_mark: Please have the following installed in your IDE environment before working on it :heavy_exclamation_mark:
- [Python 3](https://docs.python.org/3/installing/index.html)
- [Git](https://git-scm.com/downloads)

The website is deployed using Heroku and the link is [Project 4 Golden Bee](https://golden-bee-honey.herokuapp.com/).


### 9.1 How to deploy the code locally
If you wish to run this code locally, follow the instructions below:
1.	Download the code from the Github repository at [https://github.com/YiShengLee/Golden-Bee-Shop](https://github.com/YiShengLee/Golden-Bee-Shop).
2.	Click on Clone or download then Download ZIP. This will download the code into a ZIP folder locally on your computer.
3.	Uncompress the ZIP folder.
4.	Copy all the file and load it into Visual Studio Code.
    - :arrow_down: Download Link: [Visual Studio Code](https://code.visualstudio.com/) :arrow_down:

![Github Clone Image](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/GitHub_clone.png)


### 9.2 Cloning from Github
If you would like to clone this repository to your own IDE, follow the instructions below:

**Step 1: Cloning Project**  
Clone the project into your IDE with running the following command in the terminal, ensure you at project's directory in your terminal:

```
$ cd /home/user/*my_project*
```

```
git init
git clone https://github.com/YiShengLee/Golden-Bee-Shop.git
```

**Step 2: Installing Packages**  
To install all the required packages, run this in your terminal:
```
pip3 install -r requirements.txt
```

**Step 3: Run a server**  
To load the website, run this in your terminal:
```
python3 manage.py runserver 8080
```

**Step 4: Link to view project**  
A window will pop up with a link. Click on the link to view the project. 
  
<br>

### 9.3 Deploying to Heroku
This instructions shown below is from [Paul](https://github.com/kunxin-chor).  
Ensure you had [<span style="color:green">**REGISTER HEROKU**</span>](https://dashboard.heroku.com/) account.

**Step 1: Install Heroku in your system**  
In your bash terminal, install the Heroku CLI by running the following command:
```
sudo snap install heroku --classic
```

**Step 2: Install Dependencies**  
We need to install a few dependencies so that our project can work on Heroku. Run each of the following commands one by one.  
```
sudo apt install libpq-dev python3-dev
```

And the following as well:  
```
sudo pip3 install gunicorn
sudo pip3 install psycopg2
sudo pip3 install Pillow
sudo pip3 install whitenoise 
sudo pip3 install dj_database_url
```

**Step 3: Add Whitenoise**  
In the `settings.py` file, add Whitenoise to the middleware: 
```
MIDDLEWARE = [
.....
'whitenoise.middleware.WhiteNoiseMiddleware'
]
```
<span style="color:red">**IT IS IMPORTANT THAT YOU DO NOT LEAVE OUT ANY OF THE DEPENDENCIES**</span>

**Step 4: Create & Add Repository**  
Go to git hub and create a repository or you can click this [**Link**](https://github.com/new).  
In your own IDE terminal, type these commands to add the repository origin from Github:
```
git init 
git add . 
git commit -m "First commit" 
git remote add origin https://github.com/*Username*/*Repository Name*
```

**Step 5: Add Gitignore**  
Create a hidden file named `.gitignore` and add `.c9` in the file. Also add the following django files to be ignored taken from [here](http://gitignore.io/api/django).

**Step 6: Login To Heroku**  
Log into Heroku using the following command:
```
heroku login -i
```

**Step 7: Create a Heroku App**  
<span style="color:red">**!!! Make sure that you have logged into Heroku in your terminal !!!**</span>  
Create a new unique APP NAME in Heroku then run these commands, replacing the `<APP NAME>` created in Heroku site:
```
heroku create <APP NAME> 
```

**Step 8: Check Heroku APP**  
Heroku will add two origins to your git remotes. Do a check by running the following:
```
git remote -v
```

**Step 9: Copy Enuvronment to Heroku**  
1. Open you `.bashrc` file in AWS Cloud9.
2. Login to Heroku in browser: [http://www.heroku.com](http://www.heroku.com).
3. Select your app in the dashboard.
4. Click on settings.
5. Click on Real Config Vars
6. Copy the exported variables in .bashrc over to the Config Vars and <span style="color:red">**omit the quotes**</span>. See the example below!

![Heroku Settings](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/heroku_settings.PNG)

**Step 10: Create Procfile**  
Be in the root directory and run the command:
```
echo web: python app.py > Procfile
```
A file name `Procfile` will be created 

![Procfile](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/Procfile.PNG)

**Step 11: Add Command to Procfile**  
Open the Procfile, and enter the following and replace <PROJECT_FOLDER> with the name of your project folder (i.e, the **FOLDER** that contains the `settings.py` file)
```
web: gunicorn <PROJECT_FOLDER>.wsgi:application
```

**Step 12: Update ALLOWED_HOSTS**  
Add the domain name (**AND JUST THE DOMAIN NAME ONLY.** i.e without the HTTPS) of the heroku app into the ALLOWED_HOST inside settings.py 
(you can check by going to the app inside your Heroku dashboard, then click the [Open App] button on the upper right corner of the screen).

In the `settings.py`  
```
ALLOWED_HOSTS = ["golden-bee-honey.herokuapp.com", "*"]
```

**Step 13: Ensure all secret key information and sensitive data should be placed in `env.py` and linked to the `settings.py` file.**  
```
os.environ.setdefault("STRIPE_PUBLISHABLE", "") 
os.environ.setdefault("STRIPE_SECRET", "") 
os.environ.setdefault("DATABASE_URL", "") 
os.environ.setdefault("SECRET_KEY", "") 
os.environ.setdefault("AWS_SECRET_KEY_ID", "") 
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
```

**Step 14: Generate Requirements.txt**  
We need a requirements.txt file in our Git repository so that Heroku will know what packages install.  
```
pip3 freeze --local > requirements.txt
```

**Step 15: Add Static Root**
Add the following in the `settings.py` file for static files and uploads <span style="color:red">**[required steps for whitenoise to work]**</span>.
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
Example:
```
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!" />

<!-- DON'T WRITE THIS -->
<img src="/static/images/hi.jpg" alt="Hi!" />
```

**Step 16: Deploy**  
Make sure you had commit your code to your git repository!
```
git add . 
git commit -m "Deploying to Heroku" 
git push heroku master
```

**Step 17: Create a database for your Heroku app**  
Inside the bash terminal, after making sure you have <span style="color:red">**logged in**</span>, type in and run the following command:
```
heroku addons:create heroku-postgresql
```

**Step 18: Check database URL**  
Check the urls of the database you have created, type in the command:
```
heroku config
```

**Step 19: Add the url to .bashrc**  
Modify your `.bashrc` file to add in the DATABASE_URL setting:
```
export DATABASE_URL="database_url"
```
<span style="color:red">**Restart your bash terminal!**</span>

**Step 20: Change your database settings**  
First import `dj_database_url` after the other import statements in `settings.py`
```
import dj_database_url
```
Comment out your existing `DATABASES` setting in `settings.py` and replace it as shown below:
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {'default': dj_database_url.parse(os.environ["DATABASE_URL"])}
```

**Step 21: Make migrations**  
Make sure you have restarted your terminal. Make migrations with this command:
```
python3 manage.py migrate
```

**Step 22: Final Commit**  
Commit all files to Heroku using this command:
```
git add . 
git commit -m "Updated settings.py" 
git push heroku master
```

**Step 23: Create a SuperUser**  
Since we have switched to a new database, it won't have any old date, so we have to create the super user once more.
```
python3 manage.py createsuperuser
```

**Step 24: Load Heroku App**  
At the very top of the page in Heroku, click "Open App". You will now be able to view the project in Heroku

<br>

## 10.0 Credits <a name="credits"></a>

### 10.1 Code
- [w3schools](https://www.w3schools.com/)
    - Grid Layout
    - Media Query

### 10.2 Images
All images for this web site are being used under free commercial license from:
- [ShutterStock](https://www.google.com.sg/)
- [Unsplash](https://unsplash.com/)
- [Imgur](https://imgur.com/)


### 10.3 Icons
FontAwesome
- [Shopping Cart Icon](https://fontawesome.com/icons/shopping-cart?style=solid)

- [Facebook Icon](https://fontawesome.com/icons/facebook?style=brands)

- [Twitter Icon](https://fontawesome.com/icons/twitter?style=brands)

- [Instagram Icon](https://fontawesome.com/icons/instagram?style=brands)

- [Pinterest Icon](https://fontawesome.com/icons/pinterest?style=brands)

- [LinkedIn Icon](https://fontawesome.com/icons/linkedin-in?style=brands)

- [Github Icon](https://fontawesome.com/icons/github?style=brands)

- [Down Arrow](https://fontawesome.com/icons/sort-down?style=solid)

Icon8
- [Product Icon](https://icons8.com/icons/set/product)

- [Price Icon](https://icons8.com/icons/set/price)

- [Stock Icon](https://icons8.com/icons/set/stock)

- [Category Icon](https://icons8.com/icons/set/category)

- [Description Icon](https://icons8.com/icons/set/description)

- [Bee Icon](https://icons8.com/icons/set/bee)

### 10.4 Fonts
- [DM Serif Text](https://fonts.google.com/?query=DM+Serif+Text)
- [EB Garamond](https://fonts.google.com/?query=EB+Garamond)
- [Permanent Marker](https://fonts.google.com/?query=Permanent+Marker)
- [Sriracha](https://fonts.google.com/?query=Sriracha)
- [Trade Winds](https://fonts.google.com/?query=Trade+Winds)
- [Kitchen](https://www.fontspace.com/west-wind-fonts/kitchen-kapers)
- [HoneyFont](https://www.fontspace.com/kiddiefonts/save-the-honeybee)

### 10.5 Others
- [Flash Message](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/)
- [Model Field Referance](https://docs.djangoproject.com/en/2.2/ref/models/fields/)
- [Modal Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/)
- [Bootstrap Validation](http://bootstrapvalidator.votintsev.ru/getting-started/)

<br>
&emsp;**Bee Happy, Have A Sweet Life.**  
**&copy; Golden Bee 2020 | Yi Sheng Lee**