
# SendIt
[![Build Status](https://www.travis-ci.org/nanfuka/SendIt.svg?branch=develop)](https://www.travis-ci.org/nanfuka/SendIt)
[![Coverage Status](https://coveralls.io/repos/github/nanfuka/SendIt/badge.svg?branch=develop)](https://coveralls.io/github/nanfuka/SendIt?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/1d54a16ededb4dc8aefe/maintainability)](https://codeclimate.com/github/nanfuka/SendIt/maintainability)
>>>>>>> develop

# description
SendIT is a courier service that helps users deliver parcels to diferent destinations. SendIT provides courier quotes based on weight categories

## Project Features
* Users can create an account and log in
* Users can create a parcel delivery order.
* Users can change the destination of a parcel      delivery order.
* Users can cancel a parcel delivery order.
* Users can see the details of a delivery order.
* Admin can change the status and present           location of a parl delivery order



# description
Fast-food-fast is a food delivery service app for a restaurant that facilitates  interaction between the restaurant users and administrator. The users should be able to  to reach out to the restaurant and make their food orders. they should also should be able to see a history of ordered foods.    The admin should be able to add, edit or delete the fast-food and  view the list of fast-food items. The administrator should also be able to view a list of orders, accept, decline orders or Mark orders as complete

### API End Points Version 1

Endpoint | Functionality| Access
------------ | ------------- | -------------
GET /api/v1/parcels | Fetch all parcel delivery orders 
GET /api/v1/parcels/<parcelId> | Fetch a specific parcel delivery order
GET /api/v1/<userId>/parcels | Fetch all parcel delivery orders by a specific user
POST /api/v1/parcels | Create a parcel delivery order. 
PUT /parcels/<parcelId> | Cancel the specific parcel delivery order

## Tests
The Project has been tested on
* TravisCI

## Heroku 
Go to [Super Fast Parsel Delivery Services](https://sendsit.herokuapp.com/)

## Instalation

Clone the GitHub repo:
 
` git clone https://github.com/nanfuka/SendIt.git`

cd into the folder and install a Virtual Environment

` virtualenv venv`

Activate the virtual environment

`venv\scripts\activate`

Install all application requirements from the requirements file found in the root folder

`$ pip install -r requirements.txt`

Start Server 

`python app.py`.


## Contributors
* Deborah nanfuka

## How to Contribute
1. Download and install Git
2. Clone the repo `git clone https://github.com/nanfuka/SendIt.git`