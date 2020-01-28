## Aircraft Registry

This is a softare backend for a interoperable drone registry. This topic is extensive and covers a large number of topics and you can start reading it in the order below:

1. *Registration Overivew* (READ FIRST)
   - [Registry Landscape Whitepaper](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md)
  
   - [Registry Identity and Authentication](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md)
  
   - [Comprehensive Registry Testing](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registry-testing.md)

2. A deployed registry backend server (this repository) with API endpoints and documentation to read data off the database [https://aircraftregistry.herokuapp.com](https://aircraftregistry.herokuapp.com)

3. A deployed [registry frontend](https://github.com/openskies-sh/aircraft-registry-spa) application with all endpoints and sample data for you to explore (you will need credentials from us) [Airegister Frontend](https://airegister.herokuapp.com/)
  
4. A deployed [registry broker](https://github.com/openskies-sh/aircraftregistry-broker) application with all endpoints and sample data for you to explore (you will need credentials from us) [Aircraft Registry Broker](https://aircraftregistry-broker.herokuapp.com/)

## Get started

Registry and Registration systems in the context of unmanned aviation is a vast topic covering a number of things: security, identity etc. this is a comp

## Contribute

You can open issues to this repository, review the Landscape document to review the background and look at open issues to look at the current work in progress.

## Technical Details  / Self-install

This is a Django project that uses Django and Django Rest Framework and the API Specification

### 1. Install Dependencies

Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. For Local testing turn off Securing API endpoints

Go to `settings.py` and set `SECURE_API_ENDPOINTS` as `False` to disable secure endpoints for local testing. This means that you dont need the JWT tokens for Identity and Authenication, for more information about Identity and Roles are managed, please review [Identitiy and Authentication paper](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md) 

### 2. Create Initial Database

Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite.

### 3. Populate initial data

Use `python manage.py loaddata registry/defaultregistrydata.json` to populate initial data.

### 4. Launch browser 
Launch browser to http://localhost:8000/api/v1/ to launch the API Explorer

### 5. Update / Add data
This project runs on Python / Django and one of the nice thing about Django is that it comes with a Adminstration Interface. So you can go to `http://localhost:8000/admin` and login using a adminsitrator account and use the user interface to add / modify entries. 

You will have to create a "superuser" first by typing in `python manage.py createsuperuser` to create the user first. 

**Update July 2019**: **This is a fork of the [GUTMA Registry](https://github.com/gutma-org/droneregistry), that I [Dr. Hrishikesh Ballal](https://www.hrishikeshballal.net) created when I was working at GUTMA, I have now forked that repository and the work continues. The main difference here is that it has JWT based Identity and Authentication to access the endpoints and also has an updated API**