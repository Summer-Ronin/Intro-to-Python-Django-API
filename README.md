# Intro to Django REST API

Created: September 4, 2021 11:41 PM
Git repo: https://github.com/Summer-Ronin/Intro-to-Python-Django-API

# Installing requirements

- Read this article for more things about pip: [https://cutt.ly/RWEStzu](https://cutt.ly/RWEStzu)
- The **requirements.txt** is in the root folder so you need to

```bash
pip install -r requirements.txt
```

- If you don't have autopep8 yet, let's get one. In VS Code, you just have to use Shift + Alt + F then there will be pop-up and just click it, you will have your autopep8 installed automatically

```bash
pip install autopep8
```

## ⚠ Errors you may have ⚠

- Errors with your text editor when activate venv in PowerShell, [check this out for more](https://stackoverflow.com/questions/41117421/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system)

```bash
Activate.ps1
cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:3
+ & "d:/Courses/VueJs_and_Django_Rest/Part 1/Part 1/2. Build Your First ...
+   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException                                                                               nestore\onlinest
    + FullyQualifiedErrorId : UnauthorizedAccess
```

- To solve this, open PowerShell with Admin mode and type this command

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

# Intro to **requests module**

- The **requests** module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
- For more details travel to this one: [https://www.w3schools.com/python/module_requests.asp](https://www.w3schools.com/python/module_requests.asp)
- In this repo, I use [PokeAPI](https://pokeapi.co/) to try it out, I recommend you go for more than just PokeAPI, for example:
    - [Marvel API](https://developer.marvel.com/)
    - [API-Football](https://www.api-football.com/)
    - [NASA API](https://api.nasa.gov/)
    - [Open Weather API](https://openweathermap.org/)

# Steps to start Django project

- Create Django project using django-admin

```bash
django-admin startproject <name-of-your-app>
```

- Then, you will see your onlinestore app created with folder tree like this

![Untitled](Intro%20to%20Django%20REST%20API%20782425ebf9964e4692a6d4c7da6a1d05/Untitled.png)

- If you are still outside onlinestore app folder, you have to move to it first then migrate [man](http://mange.py)age.py file

```bash
python manage.py migrate
```

- And you will see this result

![Untitled](Intro%20to%20Django%20REST%20API%20782425ebf9964e4692a6d4c7da6a1d05/Untitled%201.png)

- Then create superuser that we also call it admin

```bash
python manage.py createsuperuser
```

- You will be asked to insert name, email address and password . In Django 2, it is optional to input email and password but in Django 3, you must input your password and verify it so you gotta have to do that

![Untitled](Intro%20to%20Django%20REST%20API%20782425ebf9964e4692a6d4c7da6a1d05/Untitled%202.png)

- I highly recommend using a strong password of you are working as a team, input email address and stuffs and do it like me cause we are still in our academic environment
- Now, when everything is setup, you have to test it out with

```bash
python manage.py runserver
```

- When everything is correct, you can expect to see this

![Untitled](Intro%20to%20Django%20REST%20API%20782425ebf9964e4692a6d4c7da6a1d05/Untitled%203.png)

- Next time, I will update debugger for django in VS Code which I feel comfortable working with currently

# Development overview

- Django follows the MVT (Model - View - Template) model - [Find out more here](https://www.javatpoint.com/django-mvt)

![Untitled](Intro%20to%20Django%20REST%20API%20782425ebf9964e4692a6d4c7da6a1d05/Untitled%204.png)

Basic Django Development Flow

- To access to admin page, go to