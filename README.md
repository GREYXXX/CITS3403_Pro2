# CITS3403_Pro2
# Authors: Shu Zhou 22552162, Ruilin Hu 22592495, Xi Rao 22435044, Xinhao Hao 21890522

## A brief introduction
Multi-user quiz application allow administrators to set question sets, users to submit answers to the questions, and manual or automatic assessment of those answers.

This project is developed under MAC OS.

This project should be ran while virtual environment is activated.
To install virtual environment(venv), type in your terminal:

`python -m venv venv`  

## Dependency

Dependencies needed for running the system:

Flask

flask-login

sqlalchemy

flask-sqlalchemy

sqlalchemy-migrate

flask-wtf

Selenium

To install required modules, use command line:

`pip3 install module_name`

For example, to install Flask:

`pip3 install Flask`

## Running System

To run the project, use command line:

`flask run`

The system will be running on http://localhost:5000

## Let's take a tour!

While the project is running, the first page is a welcome page.

### For normal users:


If you don't have an account yet, press register now! Otherwise, just login.

After logged in, you can use the nevigation bar to choose:

    Quiz: To choose question set

    Result: To check marks you got

To answer questions, just type your answer in following text box (case sensitive).

### For administrators:

All admin accounts are already stored in database, although admin can make normal users admin.

Admin users can use nevigation bar to choose:

    Upload questions

    Delete questions

    Mark: manually mark questions

    User management: add user(register), remove user, make other user admin


## How to contribute to the project?

Please first make sure you got all required modules in dependency installed. Flask and jinja2 are used in this project.

### Tests implemented:

Unit test: Simple test for database, model.

System test: Test for views.

![](2020-05-25-22-12-59.png)
![](2020-05-25-22-13-21.png)

(Note: It might not working well on windows or other operating system cause it might pop error 'selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: '. But it worked well on my mac system.)

### How to run tests?

Before running Unittest, you have to download chromedrive and change setting in app/__init__.py.

Download chromedriver from https://chromedriver.chromium.org/

(Note: The version of chrome you download has to be the same as your chrome browser)

First make sure your project is running in background using command:

`flask run &`

To run the test, use command line:

`python -m test.unit`

`python -m test.test`

## External js
app.js Author: Vincent Garreau  - vincentgarreau.com
particals.js Author: Vincent Garreau  - vincentgarreau.com

Background of Application.html.
