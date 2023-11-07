---
created: 2023-10-16
tags:
  - computer-science
  - internet-of-things
bibliography: C. Vennila, K. Chandraprabha, M. Vijayaraj, S. Kavitha, S. Vimalnath, K. Kalaichelvi (2021). Traffic controlling and monitoring using IoT. Journal of physics, 2027(1), 012017. https://doi.org/10.1088/1742-6596/2027/1/012017.
Type: article
Author: C. Vennila, K. Chandraprabha, M. Vijayaraj, S. Kavitha, S. Vimalnath, K. Kalaichelvi
Journal: Journal of physics
Month: 9
Number: 1
Pages: 12016
Publisher: IOP Publishing
Title: Traffic controlling and monitoring using IoT
Volume: 2027
Year: 2021
DOI: 10.1088/1742-6596/2027/1/012017
Url: https://doi.org/10.1088/1742-6596/2027/1/012017
---

**Main goal**: To assess length of vehicle road occupancy using magnetic sensor nodes, with test resulting in 100% accuracy in vehicle detection, 97% high speed and length rates, and relatively low error rate estimate in road usage

# Review of Related Literature

Advantages of Magnet Sensor

1. Easy to install on the side of road
2. Reduces detection error
3. No climate influence

## Possible Magnet Sensor Nodes

- Pressure Reference System Sensors
  - Estimated speed sensor and portable vehicle detection, scanning, classification
  - Two sensors installed in HMC2003 PCB Board
  - Uses XBee module for wireless communication
  - 99% vehicle detection, with 2.5% maximum error rate
- LCTS
  - Additional low-speed traffic node, connected to one magnetic sensor lane
  - Has sound sensor, four infrared sensors, and magnetic sensor (HMC5883L)
  - 99.05% and 93.66% accuracy
- iVCCS
  - Smart node and classification sensor with different temperature sensors, accelerometers, sensors, GPS
  - A small portable 6-axis magnetic and battery node accelerometer (FXOS8700)
  - Uses Zigbee for wireless communication
  - 99.98%, 97%, and 97.11% accurate at estimated speeds
- CPIUS
  - Classifies vehicles and estimating speed
  - Used from passive infrared sensors and ultrasound sensors
  - 99% vehicle detection accuracy, and average absolute speed estimate error is 5.87km/h
  - Multi-controller with different components, SD card joined by two sets of 5 passive infrastructural sensors (Melexis MLX 90614) with electric power tracks

# Project Architecture

![[Pasted image 20231017043833.png]]
