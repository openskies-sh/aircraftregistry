
# Comprehensive Registry Testing

## Table of Contents

- [Comprehensive Registry Testing](#comprehensive-registry-testing)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Background](#background)
  - [Goals](#goals)
  - [Registry Load testing](#registry-load-testing)
  - [Results](#results)
  - [Appendix](#appendix)
  - [Revision History](#revision-history)

## Introduction

The aim of this document is to develop operating parameters and performance envelope for an operational, interoperable registry. The registry, identity and authentication associated with it are a series of complex interconnected technologies and processes that need comprehensive testing at different levels of the stack. This is a living document and additional tests will be added over time. All testing code is available in the `tests` folder of the repository, these tests were written in the [Locust.io](https://locust.io/) framework.

## Background

It is understood that Civil Aviation Agencies (CAAs) will be building and aircraft and drone registries independelty using their existing IT staff or external contractors. At some point they will have to "bring this registry online" to enable automated querying and reading a sub-set of data in the registry.

It is anticipated that these data queries will have to be made to the registry from outside [interested parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md#interested-parties) to read data from it. Eventually, we forsee a situation where in addition to reading data from a registry, there will be automated operations to write data in it as well, it is out of scope for this document. Interoperable registries will be federated . At this time (November 2019) the focus of the document is to develop tests and scenarios for reading data from the registry.

## Goals

There are two major goals of this document, to develop a assessment of the security standards, hardware tests and develop data on the operational requirements for the registry, these include:

- *Hardware requirements*: The recommended hardware required to run a registration server that has to respond to the data requests.
- *Required reliability*: On the internet, the amount of uptime required for service is critical and directly related to the investment required to run the service. E.g. a 99.99% uptime vs a 99.99999% uptime requires different investment and technology strategy. In the context of the registry, the goal of these tests is to understand the level of SLA required for the service.
- *Response Probability*: In the context of the registry, metrics need to be developed as to how fast the requestor should expect a response and additionally the probability of receiving a response.
- *Criticality and reliability*: Is the registry system mission critical or safety critical or security critical? If the registry system fails what are the implications for the flights.
- *Push vs Pull*: Should the registry be a pull system or a push i.e. can / should the vehicles "subscribe" to the registry for updates (e.g. via Server Push or WebSockets) or should they request data using normal requests (HTTP pull).

## Registry Load testing

At this initial stage, we will just test the read throughput, no write calls will be made to the registry. For more background, please review the article by [Airbus Altiscope](https://medium.com/altiscope/introducing-altiscope-creating-blueprints-for-the-sky-9eaf931e2a60), we will assume the following:

- Operational Corridor: _274.2 km2_
- Operational scenario: _Medium Density Urban_
- Number of vehicles in the air: _1255 flights per hour / 17 flights per minute_
- Number of police / law enforcement devices: _5_
- Number of "common citizen" Remote ID requests: _500_

As is detailed in the API specification, we will query two API endpoints:

- [GET Operator Details](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-single-operator-details-get) (regular and privileged): Get details for the operator, when used as a privileged request, additional information such as personally identifiable information about the operators is also passed.
- [GET Aircraft details](https://aircraftregistry.herokuapp.com/api/v1/#operator-api-operator-aircraft-details-get) (regular and privileged): A request is made to the registry using the Electronic Serial number and records about the aircraft are relayed back.

| Test ID |  Test name | Objective | Duration | Details|
| --- | --- | --- | --- | --- |
| A | Rush hour load | The goal of this test is to see the server performance to numerous authenticated requests. We will query randomly the unprivileged endpoints of "aircraft details" and "operator details" | Continuously for 5 mins.  | 1255 vehicles make a request per second for 3 minutes.  |
| B | Law Enforcement requests | All law enforce and devices in the area make requests to the registry simultaneously with privileged requests. | Continuously for 1 minute. | Every law enforcement device in the area will make a request for data to both end points for 3 minutes.  |
| C |Citizen requests | The citizens in the area  | Continuously for 3 min. | The citizens will make a authenticated request for data from the un-privileged endpoints for data about the aircraft and also the operator. |
| D | Unauthenticated requests | The main goal of this is to test how quickly the server can respond to requests that are unauthenticated | Continuously for 3 min.  | All the interested parties will make requests to the registry without sending authentication credentials. |
| E | Unauthorized requests | The main goal of this is to test how quickly the server can respond to requests that are unauthorized (e.g. wrong scopes) | Continuously for 3 mins.  | The server will decrypt the token, read the scopes and then will understand that the requestor does not have the permission to view the data. |

## Results

| Test ID |  Test output | Raw data | Key Observation |
| --- | --- | --- | --- |
| A ([view test source](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/test-id-A.py)) | ![img-test-a](https://i.imgur.com/Za4vRnr.jpg) | [csv test output](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/output/test-a.zip) | The response time plateaus earlier than the max number of users, this means that there is software limit to the performance of Django / Python project that is independent of the number of users querying the system. This can be fixed by further scaling and investment in the servers. |
| B ([view test source](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/test-id-B.py))| ![img-test-b](https://i.imgur.com/V0IJ5fw.jpg) | [csv test output](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/output/test-b.zip)| In this test the number of queries are very low compared (see RPS) to the previous one, in this case as well the response time is more or less the same. This means that the system performance is not really dependent on the number of requests, it is in the software. |
| C ([view test source](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/test-id-C.py)) | ![img-test-c](https://i.imgur.com/gL5PKhd.jpg) | [csv test output](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/output/test-c.zip)| Same comments as above, with slightly less users (RPS 4.3 -> RPS 0.8) the response time is more or less the same.  |
| D ([view test source](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/test-id-D.py))| ![img-test-d](https://i.imgur.com/BNUFBSA.png) | [csv test output](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/output/test-d.zip)| For unauthenticated requests there is a high failure rate, this seems to be a function of Django, need to investigate why there is such a high drop rate. |
| E ([view test source](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/test-id-E.py))| ![img-test-e](https://i.imgur.com/9kG9Bjv.jpg) | [csv test output](https://github.com/openskies-sh/aircraftregistry/blob/master/tests/output/test-e.zip)| As expected all requersts should fail because they are unauthenticated in this case, we pause in the middle and then add the requests again to see if the increase in the response times has any change. |

## Appendix

Conceptually, there are three types of tests that can be undertaken in a registry:

- *Stress tests*: This type of testing is about the fault tolerance of the system, understanding the redundancies in place and the scenarios where for e.g. the registry will return a HTTP 408 request time out response. It will broadly describe the limitations of the system. In the context of manned aviation it is the loss of communication between the ATC and the pilot, at which point a set of lost communication procedures will be needed to be followed. In the context of the registry stress testing is more about peak load conditions and also ensuring that requests are not "dropped" or lost given the database load.

- *Performance tests*: This test validates that the registry performs properly for the performance standard. This is a demonstration that the system meets the requirements of performance and response times. The main goal of performance tests is to develop redundancies and make appropriate changes in the software architecture.

- *Load tests*: The primary goal of these tests is to find software bugs e.g. memory leaks, latency / congestion, buffer overflows etc.). This type of test checks the operating capacity of the registry system. This also tests multiple requests to the registry with different scopes requesting different type of information.

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 1.0 | 2-July-2020 | Dr. Hrishikesh Ballal | Removed UTM specific details and renamed repository |
| 0.8 | 10-March-2020 | Dr. Hrishikesh Ballal | Updated with NASA TCL 4 Corpus Chirsti Data |
| 0.7 | 10-February-2020 | Dr. Hrishikesh Ballal | Updated with NASA TCL 4 information and extrapolated data  |
| 0.6 | 23-January-2020 | Dr. Hrishikesh Ballal | Added Key Observations in test results  |
| 0.5 | 16-December-2019 | Dr. Hrishikesh Ballal | Added results for tests C,D and E |
| 0.4 | 6-December-2019 | Dr. Hrishikesh Ballal | Added results section and first test |
| 0.3 | 4-December-2019 | Dr. Hrishikesh Ballal | Updated test details sections |
| 0.2 | 11-November-2019 | Dr. Hrishikesh Ballal | Added additional section about goals |
| 0.1 | 5-November-2019 | Dr. Hrishikesh Ballal | First draft |
