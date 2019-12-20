# Registry Identity and Authentication

This document details the technical implementation of identity and authentication for the registry. We detail the roles, privilages and the permissions required to access data in the registry. The goal of this document is to propose standard roles and privilages associated with API end points to ensure registry interoperability using standardized queries and resposes.

## Identity / Login method
Users will log into the registry using a number of methods: it could be using their phone, email or corporate identity. Conceptually, they will verify their identity using these methods and get encrypted tokens back with the appropriate scopes (JavaScript Web Tokens for this document). The credentials are decoded / de-encrypted on the registry server and depending on the scopes present and the API called relevant the data is sent back as a standard HTTP responses. In the case of a "non-federated" / singular registry the flow looks like the diagram below.

<img src="https://i.imgur.com/ud4RORf.jpg" height="400">

For a broader application of querying multiple registries (registry broker) and how this ties into the ICAO Trust Framework, please review the intergration section in the [broker whitepaper](https://github.com/openskies-sh/aircraftregistry-broker/blob/master/documents/registration-brokerage-specification.md#integration-with-icao-trust-framework).

## Comment
Security is a vast and deep topic, for the purpose of this document, we are not advocating a specific security mechanism or technology. At this time (October-2019) it is unclear which security technology or mechanism is the most suitable for unmanned aviation. In the community there is a debate about whether OAUTH that powers major internet sites is good enough or "aviation grade". It is clear that security in aviation is a open topic that needs more research and more importantly testing.

However, it is the opinion of the author that being stuck in the technology mechanism prevents us from moving forward. We are more interested in developing the API, the scopes, identities and  roles and permissions and assume that any current or future technology can be used to communicate and transmit this information. For the sake of performance testing, we are using Auth0.com a commercial service and also building our own fork of the popular [ory/hydra](https://github.com/openskies-sh/hydra) server that is OpenID and OpenID Connect compatible.

We are not advocating any of these products or technologies but the goal is to have security and identity backend that can be changed / upgraded as this field evolves and there is a consensus on the appropriate technology for aviation.

## Registry tables and Scopes

The registry backend specifies a set of [tables](https://github.com/openskies-sh/aircraftregistry/blob/master/registry/models.py) for a database to hold data about the People, Operators and Equipment. In this section we specify the scopes and privilages for each table, as expected every table as `read` and `write` scopes additionally, we specify the following:
- `all` scopes are for foreign keys of the table
- `privileged` scopes are for privileged endpoints and interested parties.
- `unthrottled` scopes are for specific endpoints and roles (see below).

| Table | Scopes assigned | Notes |
| --- | --- | --- |
| Person | __Read__: read:person read:person:privileged read:person:all <br><br> __Write__: write:person write:person:privileged  |  All information about a person, it could be a contact, pilot etc. PII Information is in this capacity |
| Address | __Read__: read:address read:address:privileged read:address:all <br><br> __Write__: write:address write:address:privileged |  All information about addresses, PII information  |
| Activity | __Read__: read:acitivity <br><br> __Write__: write:activity |  All information about acitivites undertaken by a operator |
| Authorization | __Read__: read:authorization <br><br> __Write__: write:authorization |  All information about authorization for the operator |
| Operator | __Read__: read:operator read:operator:all read:operator:privileged <br><br> __Write__: write:operator write:operator:privileged |  All information related to a operators in the registry|
| Contact | __Read__: read:contact read:contact:all read:contact:privileged<br><br> __Write__: write:contact write:contact:privileged |  All information about a contact. PII Information. |
| Test |  __Read__: read:test <br><br> __Write__: write:test|  All information about tests taken by the pilot |
| Pilot |  __Read__: read:pilot read:pilot:all read:pilot:privileged<br><br> __Write__: write:pilot write:pilot:privileged |  All information about the pilot, PII Information |
| TestValidity |  __Read__: read:testvalidity read:testvalidity:all <br><br> __Write__: write:testvalidity write:testvalidity:all |  Write information about TestValidity|
| TypeCertificate |  __Read__:read:typecertificate <br><br> __Write__: write:typecertificate |  All information about aircraft type certificate |
| Manufacturer |  __Read__: read:manufacturer read:manufacturer:all <br><br> __Write__: write:manufacturer | All information about manufacturers |
| Aircraft |  __Read__: read:aircraft read:aircraft:all read:aircraft:all<br><br> __Write__: write:aircraft write:aircraft:all |  All information about drones and aircraft in the registry |

## Digital Identity Risk Assessment
**to be completed** 

In the context of Digital Identity we use the following definitions:

 - IAL refers to the identity proofing process.
 - AAL refers to the authentication process.
 - FAL refers to the strength of an assertion in a federated environment, used to communicate authentication and attribute information (if applicable) to a relying party (RP).


## Information Security Assessment

The registry by its nature will store personally identifiable information (PII) and the database will come under the local or national privacy and data protection laws. In many cases, this means that the data has to be stored in different servers and / or relevant security and isolation procedures must be followed. At a API level however, we propose different privilages, roles and scope that enable the interested party making the query to access this information.

For the purpose of testing the registry, we have reviewed two specific documents / publications from National Institute of Standards and Technology (NIST). [1][2][3]

| [End point](https://droneregistry.herokuapp.com/api/v1/) |  Security Category |
| --- | --- |
| [/operators](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-all-operators-get) |   Security Category <sub><sup>Public Information</sup></sub> = {(confidentiality, n/a), (integrity, moderate), (availability, low)} |
| [/operators/{operatorid}](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) | Security Category <sub><sup> Personal Identity and Authentication Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)} |
| [/operators/{operatorid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-privilaged-single-operator-details-get) | Security Category <sub><sup>Citizen Protection Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)} |
| [/contacts](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-all-contacts-get) |  Security Category <sub><sup> Personal Identity and Authentication Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)} |
| [/contacts/{contactid}](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-single-contact-details-get) | Security Category <sub><sup>Personal Identity and Authentication Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)} |
| [/contacts/{contactid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-privilaged-single-contact-details-get) | Security Category <sub><sup>Citizen Protection Information</sup></sub> = {(confidentiality, n/a), (integrity, moderate), (availability, low)} |
| [/pilots](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-all-pilots-get) | Security Category <sub><sup>Personal Identity and Authentication Information</sup></sub>  = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)}|
| [/pilots/{pilotid}](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get) | Security Category <sub><sup>Personal Identity and Authentication Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)} |
| [/pilots/{pilotid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get-1) | Security Category <sub><sup>Citizen Protection Information</sup></sub> = {(confidentiality, moderate), (integrity, moderate), (availability, moderate)}  |
| [/operators/{operatorid}/aircraft](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator) | Security Category <sub><sup>Key Asset and Critical Infrastructure Protection </sup></sub> = {(confidentiality, high), (integrity, high), (availability, high)} |
| [/aircraft/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-single-aircraft-details-get) | Security Category <sub><sup>Key Asset and Critical Infrastructure Protection </sup></sub> = {(confidentiality, high), (integrity, high), (availability, high)} |

## Rate limits
In the [API Specification](https://aircraftregistry.herokuapp.com/api/v1/), we have a section for rate limits for queries arising out of the registries. We acknowledge that rate limits is a vast topic in itself and for certain types of users (e.g. law enforcement), rate limits may need to be disabled. This is a decision that needs to be taken at the implementation level to ensure that the throttling is turned off. The section below makes note of such exception (see Notes column)

## Payload and scopes
In this section we will describe the payload that will be used to query the registry. Below is a decrypted JWT token (sent as a Bearer Token with the request) to demonstrate the details of the token. Here the `scope` is the most important parameter since it details the privilages allocated to the role.

``` JSON
{
  "iss": "https://authprovider.auth0.com/",
  "sub": "auth0|823f58f0ad39c506",
  "aud": [
    "https://authprovider/registration",
    "https://authprovider.us.auth0.com/userinfo"
  ],
  "iat": 8644995913,
  "exp": 7333345260,
  "azp": "hnhxSbRihoaBXOsLcgy2nbIIEIZNt01U",
  "scope": "read:operator read:operator:all read:operator:privileged openid profile",
  "permissions": []
}

```

The goal here is to demonstrate how the JWT token encapsulates the role and scopes associated with the login. Once these scopes are passed to the registry then the appropriate response is received.

## API End point scopes
The list below details the registry endpoints as depicted in the API blue print and the associated scopes with it.

| [End point](https://droneregistry.herokuapp.com/api/v1/) | Request Type  | Scopes required | Notes |
| --- | --- | --- | --- |
| [/operators](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-all-operators-get) | GET | read:operator | PII Information  |
| [/operators/{operatorid}](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) | GET | read:operator read:operator:all |- |
| [/operators/{operatorid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-privilaged-single-operator-details-get) | GET | read:operator read:operator:all read:operator:privileged read:operator:unthrottled | Some calls may need to be unthrottled |
| [/contacts](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-all-contacts-get) | GET | read:contact read:operator:all read:person | - |
| [/contacts/{contactid}](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-single-contact-details-get) | GET | read:contact read:person | - |
| [/contacts/{contactid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#contact-api-privilaged-single-contact-details-get) | GET | read:contact read:contact:all read:contact:privileged read:address:all read:person:all | Some calls may need to be unthrottled |
| [/pilots](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-all-pilots-get) | GET | read:pilot read:pilot:privileged read:person:privileged read:address:privileged | - |
| [/pilots/{pilotid}](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get) | GET | read:person read:pilot | - |
| [/pilots/{pilotid}/privileged](https://aircraftregistry.herokuapp.com/api/v1/#pilot-api-single-pilot-details-get-1) | GET | read:pilot read:pilot:all read:pilot:privileged read:person:privileged read:address:privileged | Some calls may need to be unthrottled |
| [/operators/{operatorid}/aircraft](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-equipment-registered-by-a-operator) | GET | read:aircraft read:aircraft:all read:aircraft:privileged | - |
| [/aircraft/{aircraftid}](https://aircraftregistry.herokuapp.com/api/v1/#aircraft-api-single-aircraft-details-get) | GET | read:aircraft | - |

## Roles

Below are roles listed as they are developed in the registry. In the coming time, more roles will be developed as per individual and professional roles in the different organizations mentioned in the [Interested Parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md#interested-parties) section. These roles and scopes would have to be linked to the registry and provided via the authentication system. We have linked the role to the appropriate "Entity ID" to cross reference the two tables.

| Role Name | Applicable Interested Party | Entity ID | Description | Scopes to be assigned | Notes |
| --- | --- | --- | --- | --- | --- |
| Drone Pilot | Private USS Operator | <b>B</b> | A pilot who is associated with a operator and has a drone and is trained and licenced to fly it. They may own multiple equipment. | read:operator read:person read:pilot write:address write:person |
| USS Administrator | USS Service provider |<b>B</b> |  A administrator within a USS, they can be the contact person between the regulator and USS. | write:operator write:person write:pilot write:address write:person read:operator read:person read:pilot read:address|
| Regulator Employee | ANSP or CAA | <b>A</b>,<b>B</b> | A regular employee in a regulator or ANSP who needs see flights and view data in the registry (but not authorize them). | read:operator read:person write:operator write:contact read:contact:all read:person:all read:contact read:pilot read:pilot read:aircraft write:aircraft write:person read:activity read:authorization | --- |
| Regulator Manager | ANSP or CAA | <b>A</b>,<b>B</b> | A regular employee in a regulator or ANSP who needs to authorize flights and view data in the registry. | read:operator read:operator:all read:operator:privileged read:person write:address write:address:privileged write:operator:privileged write:operator write:contact read:contact:all read:person:all read:contact read:pilot read:pilot:privileged read:address:privileged read:aircraft read:aircraft:privileged write:aircraft write:aircraft:privileged write:person write:authorization write:activity read:authorization read:activity | May need unthrottled privilages |
| Law Enforcement "Standard" | Police | <b>D</b> | A regular employee in law enforcement at a local level (e.g. on patrol). | read:operator read:operator:all read:operator:privileged read:person write:address write:address:privileged write:operator:privileged write:operator write:contact read:contact:all read:person:all read:contact read:pilot read:pilot:privileged read:address:privileged read:aircraft read:aircraft:privileged write:aircraft write:aircraft:privileged write:person write:authorization write:activity read:authorization read:activity |--- |
| Law Enforcement "Enhanced" | Police | <b>D</b> | A employee in law enforcement at a regional level (e.g. national investigation agency, head ). | read:operator read:operator:all read:operator:privileged read:person read:contact:all read:person:all read:contact read:pilot read:pilot:privileged read:aircraft read:aircraft:privialged read:authorization read:activity read:unthrottled | May need unthrottled privileged |

## References
[1] - [Guide for Mapping Types of Information and Information Systems to Security Categories](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v1r1.pdf)

[2] - [Volume II: Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v2r1.pdf)

[3] - [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63-3.html#sec4)

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.5 | 6-December-2019 | Dr. Hrishikesh Ballal | Added assessment of endpoints to NIST recommendations |
| 0.4 | 11-October-2019 | Dr. Hrishikesh Ballal | Added scopes to roles |
| 0.3 | 9-October-2019 | Dr. Hrishikesh Ballal | Added Payload and scope section |
| 0.2 | 4-October-2019 | Dr. Hrishikesh Ballal | Added sections about PII, Rate Limits|
| 0.1 | 26-September-2019 | Dr. Hrishikesh Ballal | First draft |
