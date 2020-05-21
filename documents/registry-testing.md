
# Comprehensive Registry Testing

## Table of Contents

- [Comprehensive Registry Testing](#comprehensive-registry-testing)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Background](#background)
  - [Goals](#goals)
  - [Scenarios](#scenarios)
    - [Extrapolating real world scenarios from TCL demos](#extrapolating-real-world-scenarios-from-tcl-demos)
  - [Flight projections and network load](#flight-projections-and-network-load)
    - [Broadcast Remote ID](#broadcast-remote-id)
    - [Broadcast Remote ID bandwidth](#broadcast-remote-id-bandwidth)
    - [WiFi Aware range](#wifi-aware-range)
  - [Registry Load testing](#registry-load-testing)
  - [Results](#results)
  - [Appendix](#appendix)
  - [Acknowledgements](#acknowledgements)
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

## Scenarios

To build a comprehensive testing and load simulation, we utilize the TCL program to develop a scenario. NASA has developed a series of tests under the Technology Capabiltiy Level (TCL) program to demonstrate and operationalize key enabling technologies for UTM in an increasing order of complexity. NASA has provided detailed reports about these tests and they are available on the [NASA UTM website](https://utm.arc.nasa.gov/documents.shtml). These demonstrators increase in complexity of missions and diverse stakeholders, the most important and relevant scenarios as demosntrated in the TCL tests is in TCL 3 and 4. TCL 4 specifically focuses on high-density urban operations, the most complicated scenario for a registry and we will focus on this.

### Extrapolating real world scenarios from TCL demos

The TCL tests are just a demonstration of core technical capability but can be a useful basis to extrapolate to understand potential real-world flight densities. For more information about TCL 4 reports, please reveiew the [results and analysis](https://utm.arc.nasa.gov/docs/2020-Rios_TM_220462-USS-Net-Perf.pdf) PDF. The most relevant Measures of Performance (MOP) for this document is UTM-MOP-16:

- _"Successful High Density Operations" which is define as the following “measures the number of (live and simulated) aircraft per defined 0.2nmi​2​ of UTM operations."_
- _"For this analysis, the minimum success criteria was more precisely defined as “ 10 aircraft (atleast 3 live operations) airborne and managed by UTM within an area of 0.2 nmi​2​."_
- _"The value of 0.2 nmi​2​ is roughlyequivalent to 720 m​2​ or a circle with radius 406m, For all calculations in this paper, a circle with 406m radius was used to calculate density."_
  
<br>From the document, below is a image of the study area that is 406m in density with > 10 flights.

TCL demonstrators are not meant to be a reflection of a real world "fully active" use. In addition to Reno, there were tests in the  Corpus Christi area. We can extrapolate this using data about Reno by making some assumptions. 

| Location | Area | 
| ------------- |:-------------:| 
| Reno, Nevada | Corpus Christi, Texas| 
| <img src="https://i.imgur.com/sHWaESL.jpg"> | <img src="https://i.imgur.com/xv5ZB3W.png"> | 
| A 406 m radius circle gives a area of 517585.04 m<sup>2</sup> or 0.51758 km<sup>2</sup> area. According to [Wikipedia](https://en.wikipedia.org/wiki/Reno,_Nevada), the population density of Reno is about 820 / km<sup>2</sup> or 425 people in our area of interest.  |  A 406 m radius circle gives a area of 517585.04 m<sup>2</sup> or 0.51758 km<sup>2</sup> area. According to [Wikipedia](https://en.wikipedia.org/wiki/Corpus_Christi,_Texas), the population density of Corpus Christi is about 710 / km<sup>2</sup> or 366 people in our area of interest. | 
| Assume that the urgent package delivery market with the following assumptions: 5% of the people are interested in urgent delivery (22 people in the area, they order urgent delivery twice a week (22 x 2 packages x 2 days) = **88 flights (back and forth)** | Assume that the urgent package delivery market with the following assumptions: 5% of the people are interested in urgent delivery (18 people in the area), they order urgent delivery twice a week (18 x 2 packages x 2 days) = **72 flights (back and forth)** | 
| Reno City has a population of 250,998 and a area of 274.2 km<sup>2</sup> (Source: [Wikipedia](https://en.wikipedia.org/wiki/Reno,_Nevada)). | Corpus Christi Metro Area has a population of 326,554 and a area of 1,304 km<sup>2</sup> (Source: [Wikipedia](https://en.wikipedia.org/wiki/Corpus_Christi,_Texas))|
| <img src="https://i.imgur.com/i8Cpz0C.png" height="400"> | <img src="https://i.imgur.com/886vL6s.png" height="400"> |
| For the entire Reno, NV area, we get the following: 5% of the people are interested in urgent delivery (12,550 people in the city), they order urgent delivery twice a week (12550 x 2 packages x 2 days) = 50,200 flights (back and forth). This means that every week there will be potentially **50,200 flights per week** in the area. For the sake of simplicity let us asssume that they will be during working hours and not on weekends: so 50,200 flights and 40 hours to fly them = **1255 flights per hour**  | For Corpus Christi, TX area, we get the following: 5% of the people are interested in urgent delivery (16328 people in the city), they order urgent delivery twice a week (16328 x 2 packages x 2 days) = 65310 flights (back and forth). This means that every week there will be potentially **65,310 flights per week** in the area. For the sake of simplicity let us asssume that they will be during working hours and not on weekends: so 65,310 flights and 40 hours to fly them = **1633 flights per hour** |

## Flight projections and network load

Assuming a 5% increase in demand in urgent deliveries, the right hand side chart shows the projected increase in the two city regions of interest <br> <img src="https://i.imgur.com/itZqIjO.png" width="400"> 

These are significant yearly flights in the region. We will now extrapolate the network load for brodcast and network remote ID per the published ASTM standard. The standard talks about broadcast ID over Bluetooth 4.0, 5.0 and WiFi and network Remote ID via the DSS.

### Broadcast Remote ID

In this section, we develop projections of broadcast Remote ID messages, the ASTM spec says that the UAS can use either Wifi or Bluetooth 4.0 or Bluetooth 5.0 to transmit the information as part of WiFi Aware for e.g. advertisement messages.

|Broadcast Remote ID |  |
| ------------- |-------------|
| Average flight return time (Assuming average speed of 35 km/hr and average distance of 10 km) | __34 mins__ |
| Number of broadcast Remote ID messages per flight  | __2040__ (1 per second)  |
| Minimum Mandatory fields (Basic ID Message + Location / Vector Message) | __50 bytes__ |
| Maximum data message size (uncompressed) if all fields used e.g. Authentication System Message and Operator ID | __150 bytes__ |

### Broadcast Remote ID bandwidth

Assuming a average flight time of 34 minutes, one flight will emit 2040 messages with a minimum of 2040 * 50 = **102,000 bytes** and maximum 2040 * 150 = **306,000 bytes** per return flight.

| Reno, Nevada | Corpus Christi, Texas|
| ------------- |-------------|
| Flight density from above: 1255 flights / hour and a average flight time of 34 minutes we can assume that almost half the flights are in the air at any given time. This leads to the following bandwidth calculations: Assuming 630 flights * 102,000 bytes = 64260000 bytes or **64.26 MB / second** minimum in the airspace and a maximum of 630 flights * 306,000 bytes = 192780000 bytes or **192.78 MB / second** throughout the entire region.   | Similarly, for Corpus Christi the 1633 flights / hour and a average flight time of 34 minutes we can assume that almost half the flights are in the air at any given time. This leads to the following bandwidth calculations: Assuming 820 flights * 102,000 bytes = 83640000 bytes or **83.64 MB / second** minimum in the airspace and a maximum of 820 flights * 306,000 bytes = 250920000 bytes or **250.78 MB / second** throughout the entire region. |

### WiFi Aware range

Typically the range of a WiFi signal is about 125-150 ft. or 38 - 45 meters. For the sake of simplicity we assume 40 meters. A drone flying at 35 km / hour (9.7 m/s) will cover 40 meters in rougly 4 seconds.

With almost 1255 flights / hour and almost half of them in the air at any time, at the most trafficed locations in the city (e.g. downtown) will have the most number of flights in the air. For the sake of simplicity we can assume that 3% of flights will be flying through downtown. This means that the receiver should be able to process **37 broadcast messages every second** in the Reno area.

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

## Acknowledgements

We are thankful to [Dr. Karthik Balakrishnan](https://www.linkedin.com/in/kbalakri) for his comments and review.

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.8 | 10-March-2020 | Dr. Hrishikesh Ballal | Updated with NASA TCL 4 Corpus Chirsti Data |
| 0.7 | 10-February-2020 | Dr. Hrishikesh Ballal | Updated with NASA TCL 4 information and extrapolated data  |
| 0.6 | 23-January-2020 | Dr. Hrishikesh Ballal | Added Key Observations in test results  |
| 0.5 | 16-December-2019 | Dr. Hrishikesh Ballal | Added results for tests C,D and E |
| 0.4 | 6-December-2019 | Dr. Hrishikesh Ballal | Added results section and first test |
| 0.3 | 4-December-2019 | Dr. Hrishikesh Ballal | Updated test details sections |
| 0.2 | 11-November-2019 | Dr. Hrishikesh Ballal | Added additional section about goals |
| 0.1 | 5-November-2019 | Dr. Hrishikesh Ballal | First draft |
