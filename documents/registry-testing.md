# Comprehensive Registry Testing

The registry, identity and authentication associated with it are a series of complex interconnected technologies and processes that need comprehensive testing at different levels of the stack. The aim of this document is to develop use cases and the associated testing criteria for a operational, interoperable registry. This is a living document and additiional tests will be added over time. All testing code is available in the `tests` folder of the repository.

## Background
It is understood that Civil Aviation Agencies (CAAs) will be building and aircraft and drone registries. At some point they will have to "bring this registry online". This means that automated queries will have to be made to the registry, from outside [interested parties](https://github.com/openskies-sh/aircraftregistry/blob/master/documents/registration-white-paper.md#interested-parties) to read data from it. Eventually, we forsee a situation where in addition to reading data from a registry, there will be automated operations to write data in it as well. We also foresee a situation where federated calls to the registry will have to be made where multiple registries have to be queried simultaneously. At this time (November 2019) the focus of the document is to develop tests and scenarios for reading data from the registry. 

Conceptually, there are three types of tests that can be undertaken in a registry: 
 - *Stress tests*: This type of testing is about the fault tolerance of the system, understanding the redundancies in place and the scenarios where for e.g. the registry will return a HTTP 408 request time out response. It will broadly describe the limitations of the system. In the context of manned aviation it is the loss of communication between the ATC and the pilot, at which point a set of lost communication procedures will be needed to be followed. In the context of the registry 
 - *Performance tests*: This test validates that the registry performs properly for the performance standard. This is a demonstration that the system meets the requirements of performance for 
 - *Load tests*: The primary goal of these tests is to find software bugs e.g. memory leaks, latency / congestion, buffer overflows etc.). This type of test checks the oeprating capacity of the registry system. This also tests multiple requests to the registry with different scopes requesting different type of information. 

## Building a simulation 
To conduct comprehensive testing we create a software simulation to depict a number of drones and aerial vehicles flying in the sky. 

## Test details
| T | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.1 | 5-November-2019 | Dr. Hrishikesh Ballal | First draft |


## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.1 | 5-November-2019 | Dr. Hrishikesh Ballal | First draft |
