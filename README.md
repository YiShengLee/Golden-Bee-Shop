# <span style="color:rgb(224,162,0)">Golden Bee Store</span>
Project 4: FullStack Final Project
Done by: Lee Yi Sheng

![Main Picture](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/main.png)

This **GoldenBeeStore** is a website for users who are looking to view and purchase raw organic honey.

Golden Bee Store: [Link](https://golden-bee-honey.herokuapp.com/)

## Table of contents
1. #### [Introduction](#introduction)
2. #### [User Stories](#userstories)
3. #### [UX](#UX)
4. #### [Features](#features)
5. #### [Technologies Used](#technology)
6. #### [Future Features to Implement](#implement)
7. #### [Testing](#testing)
8. #### [Deployment](#deployment)
9. #### [Credits](#credits)

<br>

## Introduction <a name="introduction"></a>


## 7.0 Deployment <a name="testing"></a>
A full testing process can be found in a separate [tests.md](https://github.com/YiShengLee/Golden-Bee-Shop/blob/master/tests.md) file.




## 8.0 Deployment <a name="deployment"></a>
The project was built using [AWS Cloud9](https://aws.amazon.com/cloud9/).  
:heavy_exclamation_mark: Please have the following installed in your IDE environment before working on it :heavy_exclamation_mark:
- [Python 3](https://docs.python.org/3/installing/index.html)
- [Git](https://git-scm.com/downloads)

The website is deployed using Heroku and the link is [Project 4 Golden Bee](https://golden-bee-honey.herokuapp.com/).


### 8.1 How to deploy the code locally
If you wish to run this code locally, follow the instructions below:
1.	Download the code from the Github repository at [https://github.com/YiShengLee/Golden-Bee-Shop](https://github.com/YiShengLee/Golden-Bee-Shop).
2.	Click on Clone or download then Download ZIP. This will download the code into a ZIP folder locally on your computer.
3.	Uncompress the ZIP folder.
4.	Copy all the file and load it into Visual Studio Code.
    - :arrow_down: Download Link: [Visual Studio Code](https://code.visualstudio.com/) :arrow_down:

![Github Clone Image](https://github.com/YiShengLee/Golden-Bee-Shop/raw/master/static/images/GitHub_clone.png)


### 8.2 Cloning from Github
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

### 8.3 Deploying to Heroku
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

## 9.0 Credits <a name="credits"></a>

### 9.1 Code
- [w3schools](https://www.w3schools.com/)
    - Grid Layout
    - Media Query

### 9.2 Images
All images for this web site are being used under free commercial license from:
- [ShutterStock](https://www.google.com.sg/)
- [Unsplash](https://unsplash.com/)
- [Imgur](https://imgur.com/)


### 9.3 Icons
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

### 9.4 Fonts
- [DM Serif Text](https://fonts.google.com/?query=DM+Serif+Text)
- [EB Garamond](https://fonts.google.com/?query=EB+Garamond)
- [Permanent Marker](https://fonts.google.com/?query=Permanent+Marker)
- [Sriracha](https://fonts.google.com/?query=Sriracha)
- [Trade Winds](https://fonts.google.com/?query=Trade+Winds)
- [Kitchen](https://www.fontspace.com/west-wind-fonts/kitchen-kapers)
- [HoneyFont](https://www.fontspace.com/kiddiefonts/save-the-honeybee)

### 9.5 Others
- [Flash Message](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/)
- [Model Field Referance](https://docs.djangoproject.com/en/2.2/ref/models/fields/)
- [Modal Bootstrap](https://getbootstrap.com/docs/4.0/components/modal/)
- [Bootstrap Validation](http://bootstrapvalidator.votintsev.ru/getting-started/)

<br>
&emsp;**Bee Happy, Have A Sweet Life.**  
**&copy; Golden Bee 2020 | Yi Sheng Lee**