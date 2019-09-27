# Registration Identity and Authentication 

In this document, we will detail the roles and scopes implemented in the registry. 



## API End point scopes
The list below details the registry endpoints as depicted in the API blue print and the associated scopes with it.

| [End point](https://droneregistry.herokuapp.com/api/v1/) |   | Scopes required |
| --- | --- | --- |
| [/person/add/](https://aircraftregistry.herokuapp.com/api/v1/#person-and-address-api-add-a-new-person-post) | POST | write:person write:person:privilaged |
| [/address/add/](https://aircraftregistry.herokuapp.com/api/v1/#person-and-address-api-add-a-new-address-post) | POST | write:address write:address:privilaged |
| [/operators/add/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-add-a-new-operator-post) | POST | write:operator write:operator:privilaged |
| [/operators/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-all-operators-get) | GET | read:operator |
| [/operators/{operatorid}/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) | GET | read:operator read:operator:all |
| [/operators/{operatorid}/privilaged/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-privilaged-single-operator-details-get) | GET | read:operator read:operator:all read:operator:privilaged |
| [/operators/update/{operatorid}/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-update-existing-operator-details-post) | POST | write:operator write:operator:privilaged |
| [/contacts/](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-all-contacts-get) | GET | read:contact read:operator:all read:person |
| [/contacts/{contactid}/](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-single-contact-details-get) | GET | read:contact read:person |
| [/contacts/{contactid}/privilaged](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-privilaged-single-contact-details-get) | GET | read:contact read:contact:all read:contact:privilaged read:address:all read:person:all |
| [/pilots/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-all-pilots-get) | GET | read:pilot read:pilot:privilaged read:person:privilaged read:address:privilaged |
| [/pilots/{pilotid}/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get) | GET | read:person read:pilot |
| [/pilots/{pilotid}/privilaged](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get-1) | GET | read:pilot read:pilot:all read:pilot:privilaged read:person:privilaged read:address:privilaged |
| [/contacts/update/{pilotid}/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-update-existing-pilot-details-post) | POST | write:pilot write:pilot:privilaged |
| [/operators/{operatorid}/aircraft/](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator) | GET | read:aircraft read:aircraft:all read:aircraft:privilaged |
| [/aircraft/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-single-aircraft-details-get) | GET | read:aircraft |
| [/operators/{operatorid}/aircraft/](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator-post) | POST | write:aircraft write:aircraft:privilaged |
| [/operators/{operatorid}/aircraft/update/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-update-registered-equipment-post) | POST | write:aircraft write:aircraft:privilaged |

## Identity / Login method
Users will log into the regitry using a number of methods, it could be using their phone, email or corporate identity. Broadly, they will login and the get a JWT credentials. The credentials are decoded / de-encrypted on the registry server and return the data back. Broadly the flow looks like the following. 

<img src="https://i.imgur.com/4rMHnJH.jpg" height="400">

## Roles
Below are roles listed as they are developed in the registry. In the coming weeks, more roles will be developed as per individual and professional roles in the different organizations mentioned in the [Interested Parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md) section.

| Name | Applicable Interested Party | Description |
| --- | --- | --- |
| Drone Pilot | USS, Operator | A pilot who is associated with a operator and has a drone and is trained and licenced to fly it. They may own multiple equipment. |
| Regulator Employee | ANSP, CAA | A regular employee in a regulator or ANSP who needs to authorize flights and view data in the registry. |
| Regulator Manager | ANSP, CAA | A regular employee in a regulator or ANSP who needs to authorize flights and view data in the registry. |

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.1 | 26-September-2019 | Dr. Hrishikesh Ballal | First draft |
