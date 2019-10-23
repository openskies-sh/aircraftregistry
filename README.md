**Update July 2019**: **This is a fork of the [GUTMA Registry](https://github.com/gutma-org/droneregistry) that is maintainted and adds Identity and Authentication to access the endpoints and also has an updated API**

## Aircraft Registry Sandbox

This is a sandbox for working on a interoperable drone registry. It has three main things, you can start in the order below: 

1. [Registry Landscape Whitepaper](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md)
2. Interoperatble API Specification, the technical specification for a registry. You can see the API specification and explore API endpoints at [https://aircraftregistry.herokuapp.com](https://aircraftregistry.herokuapp.com) 
3. A working API with all endpoints and sample data for you to explore [https://aircraftregistry.herokuapp.com/api/v1/](https://aircraftregistry.herokuapp.com/api/v1/)

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
