# Comprehensive Registry Testing

The registry, identity and authentication associated with it are a series of complex interconnected technologies and processes that need comprehensive testing at different levels of the stack. The aim of this document is to develop use cases and the associated testing criteria for a operational, interoperable registry. This is a living document and additiional tests will be added over time. All testing code is available in the `tests` folder of the repository. 

It is understood that Civil Aviation Agencies (CAAs) will be building and aircraft and drone registries. At some point they will have to "bring this registry online". This means that automated queries will have to be made to the registry, from outside [interested parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md#interested-parties) to read data from it. Eventually, we forsee a situation where in addition to reading data from a registry, there will be automated operations to write data in it as well. We also foresee a situation where federated calls to the registry will have to be made where multiple registries have to be queried simultaneously. At this time (November 2019) the focus of the document is to develop tests and scenarios for reading data from the registry.

## Goals

The aim of these tests is to generate data and understand some key questions regarding the registry:

<<<<<<< HEAD
- *Required reliability*: On the internet, the amount of uptime required for service is critical and directly realted to the investment required to run the service. E.g. a 99.99% uptime vs a 99.99999% uptime requires different investment and technology strategy. In the context of the registry, the goal of these tests is to understand the level of SLA required for the service.
- *Response Probability*: In the context of the registry, metrics need to be developed as to how fast should the requestor expect a response and additionally the probability of receiving a respone.
- *Uptime and reliability*: Is the registry system mission crticial or safety critical or security critical? If the registry system fails what are the implications for the flights.
- *Push vs Pull*: Should the registry be a pull system or a push i.e. can / should the vehicles "subscribe" to the registry for updates (e.g. via Server Push or WebSockets) or should they request data using normal requests (HTTP pull).

## Scenarios

To conduct comprehensive testing for the registry, we create a software simulation. The simulation essentially is digital environment with a number of drones and aerial vehicles flying in the sky. Out of these vehicles we would simulate a percent of them making calls to the registry at any given point of time. The simulation will also have a temporal compnent in that it will run for a certain amount of time: 15 minutes. In addtion to the vehicles making calls to the registry, we would like to simulate different stakeholders making requests for data into the registry. 
=======
- *Required reliability*: On the internet, the amount of uptime required for a service is critical and directly related to the investment required to run it. E.g. a 99.99% uptime vs a 99.99999% uptime requires different levels of investment and technology strategy. In the context of the registry, the goal of these tests is to understand the level of SLA required for the service in production.
- *Response Probability*: In the context of the registry, metrics need to be developed as to how fast should the requestor expect a response and additionally the probability of receiving a respone in different network conditions. 
- *Uptime*: Is the registry system mission crticial or safety critical service? If the registry system fails what are the implications for the flights, while not directly related to the technical performance of the registry, the tests need to develop a opinion on this topic. 
- *Push vs Pull*: Should the registry be a pull system or a push i.e. can / should the vehicles "subscribe" to the registry for updates (e.g. via Server Push or WebSockets) or should they request data using normal requests (HTTP pull).

## Background

It is understood that Civil Aviation Agencies (CAAs) will be building aircraft and drone registries indedpendently using their existing IT contractors / procurement procedures. In a UTM context, the registry is a live and "active" member of the sky and the CAAs will have to "bring these registries online". This means that authenticated queries will have to be made to the registry by [interested parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md#interested-parties). We anticipate a bulk of these queries would be to read data from it. Eventually, we forsee a situation where in addition to reading data from a registry, there will be automated operations to write data in it as well. We also foresee a situation where federated calls to the registry will have to be made where multiple registries have to be queried simultaneously. At this time (November 2019) the focus of the document is to develop tests and scenarios for reading data from the registry and not on writing data into the registry. This is because we expect that writing data into sovereign registrties by third parties will not be allowed. 

Conceptually, there are three types of tests that can be undertaken in a registry:

 - *Stress tests*: This type of testing is about the fault tolerance of the system, understanding the redundancies in place and the scenarios where for e.g. the registry will return a HTTP 408 request time out response. It will broadly describe the limitations of the system. In the context of manned aviation it is the loss of communication between the ATC and the pilot, at which point a set of lost communication procedures will be needed to be followed. In the context of the registry stress testing is more about peak load conditions and also ensuring that requests are not "dropped" or lost given the database load. 

 - *Performance tests*: This test validates that the registry performs properly for the performance standard. This is a demonstration that the system meets the requirements of performance and response times. The main goal of performance tests is to develop redundancies and make appropriate changes in the software architecture. 

 - *Load tests*: The primary goal of these tests is to find software bugs e.g. memory leaks, latency / congestion, buffer overflows etc.). This type of test checks the oeprating capacity of the registry system. This also tests multiple requests to the registry with different scopes requesting different type of information. 

## Scenarios

To conduct comprehensive testing for the registry, we will create a software simulation. The simulation essentially is digital environment with a number of drones and aerial vehicles flying in the sky. Out of these vehicles we would simulate a percent of them making calls to the registry at any given point of time. The simulation will also have a temporal compnent in that it will run for a certain amount of time: 15 minutes. In addtion to the vehicles making calls to the registry, we would like to simulate different stakeholders making requests for data into the registry.
>>>>>>> 7c6c204b4de6040881224fd6f0198503562b62c8

## Test details

At this initial stage, we will just test the read throughput, no write calls will be made to the registry. To set the scene, we will assume the following: 

- Operational corridoor: _1 km length x 200 m width_
- Operational scenario: _Medium Density Urban_
- Number of people / residents nearby: _1000 individuals_
- Flying over people: _Not permitted_
- Number of vehicles in the air: _500_
- Number of police / law enforcement devices: _5_
- Number of "common citizen" Remote ID requests: _20_

As is detailed in the API specification, we will query two API endpoints:

- [GET Operator Details](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) (regular and privileged): Get details for the operator, when used as a privileged request, additional information such as personally identifiable infromation about the operators is also passed.
- [GET Aircraft details](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-operator-aircraft-details-get) (regular and privileged): A request is made to the registry using the Electronic Serial number and records about the aircraft are relayed back.

| Test ID |  Test name | Objective | Duration | Details| Request payload |
| --- | --- | --- | --- | --- | --- |
| A| Rush hour load | The goal of this test is to see the server performance to numerous authenticated requests. We will query randomly the unprivileged endpoints of "aircraft details" and "operator details" | Continuously for 5 mins.  | Every vehicle makes a request per second for 5 minutes.  | TBC |
|B | Law Enforcement requests | All law enforcemand devices in the area make requests to the registry simmultaneously with privileged requests. | Continously for 1 minute. | Every law enforcement device in the area will make a request for data to both end points for 1 minute.  | TBC |
|C |Citizen requests | The citizens in the area  | Continuously for 5 mins. | The citizens will make a authenticated request for data from the un-privileged endpoints for data about the aircraft and also the operator. | TBC |
| D | Unauthenticated requests | The main goal of this is to test how quickly the server can respond to requests that are unauthenticated | Continuously for 5 mins.  | All the interested parties will make requests to the registry without sending authentication credentials. | TBC |
| E | Authenticated requests | The primary goal here is to test token decryption performance on the server.  | Continuously for 2 mins.  | All the interested parties in the area will make authenticated requests to the registry for data from unprivileged endpoints. | TBC |
| F | Unauthorized requests | The main goal of this is to test how quickly the server can respond to requests that are unauthorized (e.g. wrong scopes) | Continuously for 5 mins.  | The server will decrypt the token, read the scopes and then will understand that the requestor does not have the permission to view the data.  | TBC |

## Appendix

Conceptually, there are three types of tests that can be undertaken in a registry:

- *Stress tests*: This type of testing is about the fault tolerance of the system, understanding the redundancies in place and the scenarios where for e.g. the registry will return a HTTP 408 request time out response. It will broadly describe the limitations of the system. In the context of manned aviation it is the loss of communication between the ATC and the pilot, at which point a set of lost communication procedures will be needed to be followed. In the context of the registry stress testing is more about peak load conditions and also ensuring that requests are not "dropped" or lost given the database load.

- *Performance tests*: This test validates that the registry performs properly for the performance standard. This is a demonstration that the system meets the requirements of performance and response times. The main goal of performance tests is to develop redundancies and make appropriate changes in the software architecture.

- *Load tests*: The primary goal of these tests is to find software bugs e.g. memory leaks, latency / congestion, buffer overflows etc.). This type of test checks the oeprating capacity of the registry system. This also tests multiple requests to the registry with different scopes requesting different type of information.


## Acknowledgements

We are thankful to [Dr. Karthik Balakrishnan](https://www.linkedin.com/in/kbalakri) for his comments and review.

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.2 | 11-November-2019 | Dr. Hrishikesh Ballal | Added additional section about goals |
| 0.1 | 5-November-2019 | Dr. Hrishikesh Ballal | First draft |
