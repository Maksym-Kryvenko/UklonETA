# UklonETA
Estimated Time of Arrival (ETA)

## Team KryMor:
- Oleg Morhaliuk
- Maksym Kryvenko

## Competition results:
- 3rd place of 17 teams
- Model - Gradient Boosting Regressor
- Final model score - 148.29894

## Introduction
Calculating the Estimated Time of Arrival (ETA) is one of the important services of the ride-hailing platform. User opens an application, orders the exact class of car, and just after submitting the order, can see the ETA. ETA is a predicted time of arriving at the destination point.

## Goal
It is required to forecast the time which is required to get to the destination point. Historical data with arrival time provided for this assignment.

## Data
An example of data from Odessa.
### File orders.csv contains data:
- Id – a unique identifier of an order (order created by passenger).
- running_time – date and time of beginning a ride.
- completed_time – date and time when a ride was completed.
- route_distance_km – distance in kilometers from the starting to the end point of a ride.
- delta_time – an actual time, a duration of a ride.

### File nodes.csv** contains data:
- Id – a unique identifier of an order (order created by passenger).
- node_start – starting node.*
- node_finish – ending node.*
- distance – distance between nodes in meters.
- speed  – an average velocity of other cars between the nodes based on previous orders.

\* Node – one of the essential elements of the OpenStreetMap database. Node consists of the single point in a space which defines the longitude, and latitude, and node id (unique node identifier).
