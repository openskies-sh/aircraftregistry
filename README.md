## Aircraft Registry

This is a softare stack for a interoperable drone registry. It is extensive and covers a large number of topics and you can start reading it in the order below:

1. *Registration Overivew* (READ FIRST)
   - [Registry Landscape Whitepaper](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md)
  
   - [Registry Identity and Authentication](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md)
  
   - [Comprehensive Registry Testing](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registry-testing.md)

2. A registry backend server with API endpoints and documentation to read data off the database [https://aircraftregistry.herokuapp.com](https://aircraftregistry.herokuapp.com)

3. A registry frontend application with all endpoints and sample data for you to explore (you will need credentials from us) [Airegister Frontend](https://airegister.herokuapp.com/)

## Get started

Registry and Registration systems in the context of unmanned aviation is a vast topic covering a number of things: security, identity etc.

## Contribute

You can open issues to this repository, review the Landscape document to review the background and look at open issues to look at the current work in progress.

## Technical Details  / Self-install

This is a Django project that uses Django and Django Rest Framework and the API Specification

### 1. Install Dependencies

Python 3 is required for this and install dependencies using `pip install -r requirements.txt`.

### 2. Create Initial Database

Use `python manage.py migrate` to create the initial database tables locally. It will use the default SQLLite.

### 3. Populate initial data

Use `python manage.py loaddata registry/defaultregistrydata.json` to populate initial data.

### 4. Launch browser 
Launch browser to http://localhost:8000/api/v1/ to launch the API Explorer


**Update July 2019**: **This is a fork of the [GUTMA Registry](https://github.com/gutma-org/droneregistry) that is maintainted and adds Identity and Authentication to access the endpoints and also has an updated API**