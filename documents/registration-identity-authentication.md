# Registration Identity and Authentication

This document details the technical implementation of identity and authentication for the registry. We detail the roles, privilages and the permissions required to access data in the registry. The goal of this document is to propose standard roles and privilages associated with API end points to ensure registry interoperability and queries.

## Identity / Login method
Users will log into the regitry using a number of methods, it could be using their phone, email or corporate identity. Broadly, they will login and the get a JWT credentials. The credentials are decoded / de-encrypted on the registry server and return the data back. Broadly the flow looks like the following.

<img src="https://i.imgur.com/4rMHnJH.jpg" height="400">

Security is a vast and deep topic, for the purpose of this document, we are not advocating a specific security mechanism or technology. At this time (October-2019) it is unclear which security technology or mechanism is the most suitable for unmanned aviation. In the community there is a debate about whether OAUTH that powers major internet sites is good enough or "aviation grade". It is clear that security in aviation is a open topic that needs more research and more importantly testing.

However, it is the opinion of the author that being stuck in the technology mechanism prevents us from moving forward. We are more interested in developing the API, the scopes, identities and  roles and permissions and assume that any current or future technology can be used to communicate and transmit this information. For the sake of performance testing, we are using Auth0 a commercial service and also building our own fork of the popular [ory/hydra](https://github.com/openskies-sh/hydra) server that is OpenID and OpenID Connect compatible. 

We are not advocating any of these products or technologies but the goal is to have security and identity backend that can be changed / upgraded as this field evolves.

## Personally Identifiable Information

The registry by its nature will store personally identifiable information (PII) and the database will come under the local or national privacy and data protection laws. In many cases, this means that the data has to be stored in different servers and / or relevant security and isolation procedures must be followed. At a API level however, we propose different privilages, roles and scope that enable the interested party making the query to access this information. 

## Rate limits
In the [API Specification](https://aircraftregistry.herokuapp.com/api/v1/), we have a section for rate limits for queries arising out of the registries. We acknowledge that rate limits is a vast topic in itself and for certain types of users (e.g. law enforcement), rate limits may need to be disabled. This is a decision that needs to be taken at the implementation level to ensure that the throttling is turned off. The section below makes note of such exception (see Notes column)


## API End point scopes
The list below details the registry endpoints as depicted in the API blue print and the associated scopes with it.

| [End point](https://droneregistry.herokuapp.com/api/v1/) |   | Scopes required | Notes |
| --- | --- | --- | --- |
| [/person/add/](https://aircraftregistry.herokuapp.com/api/v1/#person-and-address-api-add-a-new-person-post) | POST | write:person write:person:privilaged |  PII Information |
| [/address/add/](https://aircraftregistry.herokuapp.com/api/v1/#person-and-address-api-add-a-new-address-post) | POST | write:address write:address:privilaged | PII Information  |
| [/operators/add/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-add-a-new-operator-post) | POST | write:operator write:operator:privilaged | PII Information |
| [/operators/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-all-operators-get) | GET | read:operator | PII Information  |
| [/operators/{operatorid}/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) | GET | read:operator read:operator:all |- |
| [/operators/{operatorid}/privilaged/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-privilaged-single-operator-details-get) | GET | read:operator read:operator:all read:operator:privilaged read:operator:unthrottled | Some calls may need to be unthrottled |
| [/operators/update/{operatorid}/](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-update-existing-operator-details-post) | POST | write:operator write:operator:privilaged | - |
| [/contacts/](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-all-contacts-get) | GET | read:contact read:operator:all read:person | - |
| [/contacts/{contactid}/](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-single-contact-details-get) | GET | read:contact read:person | - |
| [/contacts/{contactid}/privilaged](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-privilaged-single-contact-details-get) | GET | read:contact read:contact:all read:contact:privilaged read:address:all read:person:all | Some calls may need to be unthrottled |
| [/pilots/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-all-pilots-get) | GET | read:pilot read:pilot:privilaged read:person:privilaged read:address:privilaged | - |
| [/pilots/{pilotid}/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get) | GET | read:person read:pilot | - |
| [/pilots/{pilotid}/privilaged](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get-1) | GET | read:pilot read:pilot:all read:pilot:privilaged read:person:privilaged read:address:privilaged | Some calls may need to be unthrottled |
| [/contacts/update/{pilotid}/](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-update-existing-pilot-details-post) | POST | write:pilot write:pilot:privilaged | - |
| [/operators/{operatorid}/aircraft/](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator) | GET | read:aircraft read:aircraft:all read:aircraft:privilaged | - |
| [/aircraft/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-single-aircraft-details-get) | GET | read:aircraft | - |
| [/operators/{operatorid}/aircraft/](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator-post) | POST | write:aircraft write:aircraft:privilaged | - |
| [/operators/{operatorid}/aircraft/update/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-update-registered-equipment-post) | POST | write:aircraft write:aircraft:privilaged | - |

## Roles
Below are roles listed as they are developed in the registry. In the coming weeks, more roles will be developed as per individual and professional roles in the different organizations mentioned in the [Interested Parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-identity-authentication.md) section.

| Name | Applicable Interested Party | Description | Notes |
| --- | --- | --- | --- |
| Drone Pilot | USS, Operator | A pilot who is associated with a operator and has a drone and is trained and licenced to fly it. They may own multiple equipment. | --- |
| Regulator Employee | ANSP, CAA | A regular employee in a regulator or ANSP who needs to authorize flights and view data in the registry. | --- |
| Regulator Manager | ANSP, CAA | A regular employee in a regulator or ANSP who needs to authorize flights and view data in the registry. | May need unthrottled privilages |
| Law Enforcement "Standard" | Police | A regular employee in law enforcement at a local level (e.g. on patrol). | --- |
| Law Enforcement "Enhanced" | Police | A employee in law enforcement at a regional level (e.g. national investigation agency, head ). | May need unthrottled privilages |

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.2 | 4-October-2019 | Dr. Hrishikesh Ballal | Added sections about PII, Rate Limits|
| 0.1 | 26-September-2019 | Dr. Hrishikesh Ballal | First draft |
