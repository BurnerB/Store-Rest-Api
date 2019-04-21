### STORE-APP

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8ff36e0ba8d14b60bdf33a8a5d99f733)](https://app.codacy.com/app/BurnerB/Store-Rest-Api?utm_source=github.com&utm_medium=referral&utm_content=BurnerB/Store-Rest-Api&utm_campaign=Badge_Grade_Dashboard)

### Endpoints covered
| Method        | Endpoint                 | Description|
| ------------- | --------------------------|------------|
| POST           |`/register`   |Register a user|
| POST           | `/login`   |login or sign in a user|
| POST          | `/refresh`    |refresh a users access token |
| GET          | `/user/<user-id>`     |get a specific user|
| DELETE          | `/user/<user-id`|delete a specific user|
| POST          | `/item/<item-name>`       |add an item|
| PUT         | `/item/<item-name>` |modify or add a specific item|
| GET | `/item/<item-name>`|get a specific item|
| GET  |`/items` |get all items|
| DELETE          | `/item/<item-name>`|delete a specific item|
| POST          | `/store/<store-name>`       |create a store|
| GET        | `/store/<store-name>` |get a specific store|
| DELETE | `/store/<store-name>`|delete a specific store|
| GET  |`/stores` |get all stores|

## Getting Started
#### Setting up your system

Make sure you already have Python3, Pip and Virtualenv installed in your system..
#### How to get started
Start by making a directory where we will work on. Simply Open your terminal and then:

`mkdir STORE-APP`

Afterwhich we go into the directory:

`cd STORE-APP`

#### Create a Python Virtual Environment for our Project
Since we are using Python 3, create a virtual environment by typing:
`virtualenv -p python3 venv`

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:
`source venv/bin/activate`

#### Clone and Configure a Flask Project
Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:
`git clone https://github.com/BurnerB/STORE-APP.git`

Next, install the requirements by typing:
`pip install -r requirements.txt`

### How to run the app
On the terminal type:
`python app.py`
