---
created: 2023-10-16
tags:
  - computer-science
  - internet-of-things
bibliography: Zhao, Y., Jiali, T., Huang, H., Wang, Z., Chen, T., Chiang, C., & Chiang, P. (2020). Development of IoT technologiesfor air pollution prevention and improvement. Aerosol and Air Quality Research, 20(12), 2874–2888. https://doi.org/10.4209/aaqr.2020.05.0255
Type: article
Author: Zhao, Yu-Lin and Jiali, Tang and Huang, Han‐Pang and Wang, Ze and Chen, Tse-Lun and Chiang, Chih-Wei and Chiang, Pen‐Chi
Journal: Aerosol and Air Quality Research
Month: 1
Number: 12
Pages: 2874--2888
Publisher: Taiwan Association for Aerosol Research
Title: Development of IoT technologies for air pollution prevention and improvement
Volume: 20
Year: 2020
Doi: 10.4209/aaqr.2020.05.0255
Url: https://doi.org/10.4209/aaqr.2020.05.0255
---
# Description
**Main Problem**: Ambient air pollution as potential air pollutants
**Solution**: Development of instruments measurements and monitoring system for ambient air quality
#
## Air Pollutants
- Particulate Matter
	- PM<sub>2.5</sub>
	- PM<sub>10</sub>
 - Sulfur Oxide (SO<sub>x</sub>)
 - Nitrogen Oxide (NO<sub>x</sub>)
 - Ozone (O<sub>x</sub>)
 - Carbon Monoxide (CO)
 - Volatile Organic Compounds (VOCs)

## Systematic monitoring by industrial proven PM technologies
Aerosols and dusts can be monitored by:
- Gravimetric Sampling
- Light Scanning
- Inertial Weighing Tapered Element Oscillating Microbalance (TEOM)

# Internet of Things Layers
- Perception Layer
- Network Layer
- Application Layer

#
### Perception Layer
Perception layer includes diverse sensor nodes and gateways, such as various sensors, electronic tags, read/write devices, cameras, and GPS, whose main function is to identify, collect and transmit information of objects.
### Network Layer
Network layer is composed of various internet, wireless communication networks, mobile air networks (3G/4G/5G), private networks, network management systems, cloud computing platforms, etc. Its main role is to carry out real-time transmission and fast various data information obtained by the perception layer.
### Application Layer
Application layer provides a convenient information interaction system for IoT and users according to the actual needs of users.

## Figure 1. Three layers of IoT
![[Pasted image 20231018000357.png]]

## IoT Framework under axial application development
![[Pasted image 20231018073510.png]]
## IoT Framework
composed of a loop of real-time:
- sensing data
- calculating data
- transmitting data
- presenting data

## IoT Applications
![[Pasted image 20231023220329.png]]

## Fundamentals of IoT
Three key technologies of IoT:
1. RFID
2. M2M
3. Sensor Network

## RFID
- uses radio frequency signals
- consists of
	- tags
	- readers
	- antennas

## Working Principle Chart of RFID
![[Pasted image 20231023220905.png]]

## M2M
- communication between machines and equipment applications with host information systems
- establish wireless connection between:
	- systems
	- remote devices
	- individuals in real time
- m2m domain:
	- machine to machine
	- man to machine
	- machine to man
	- machine to mobile
	- mobile to machine
- product's included:
	- wireless terminal
	- transmission channel
	- industry application center

## Structure of M2M System
![[Pasted image 20231023222841.png]]

## Sensor Network
- combine information sensors (e.g. infrared, gps, laser scanners) with the internet
- basic feature: dynamically self-organizational
- main types of nodes:
	- sensor nodes
	- aggregation nodes
	- management nodes

composition of network nodes:
1. sensing mechanism
2. processing mechanism
3. communication mechanism
4. power supply

functional elements:
1. positioning system
2. motion system
3. power generation system

main methods of topology control:
1. hierarchical technology
2. power-type technology

## Structure of hierarchical topology control
![[Pasted image 20231023224305.png]]

## Development of IoT Platform for Air Quality Management
This IoT system uses:
- Javacript
- integrated Arduino Ethernet
- jQuery UI
- Node Package Manager
- Express framework

Monitoring Pollution Concentration in real time using:
- Open-path Fourier Transform Infrared (OP-FTIR)
- Miscellaneous Gas Sensors (MGS)
- Light Detection and Ranging (LiDAR)
- Miniature Continuous Emission Monitoring System (Mini-CEMS)
- Anemometers

**Communication Method**: NarrowBand Internet of Things (NB-IoT) and Wi-Fi terminals

## IoT Platform of Ambient Air Pollution
When air pollution concentration is over the ambient standard, **LiDAR** is used then monitored by the **Mini-CEMS**.

This environmental air pollution IoT monitoring system (shown in Fig. 1) is a network of multiple scientific instruments (LiDAR, OP-FTIR, mini-CEMSs, MGSs, anemometers) and a web connected by the NarrowBand Internet of Things wireless communication technology.

The monitoring system is composed of 3 layers of sensors, data transmission, and software application.

The system software mainly includes two parts: 
- embedded software
- server-side web application (MySQL)

## Air pollution monitoring platform of Internet of Things
![[Pasted image 20231024141301.png]]

## Environmental Air Monitoring Sensors
- The **gas sensor** is a device that **converts a specific gas concentration into an appropriate electronic signal**, such as voltage, current, or resistance.

## Networked Device
The internal network of IoT platform includes:
- LiDAR
- OP-FTIR
- mini-CEMSs
- MGSs
- anemometers

## Internal Network
### LiDAR System
- a self-made air pollution optical telemetry instrument
- consists of a laser transmitter and a telescope as a receiver

### OP-FTIR
- volatile pollutants in the air are monitored, and the average concentration of the gas sample in the measurement path is obtained by spectral analysis

### Mini-CEMS
- uses an automatic start-up device to dilute the standard air to a measurable range according to the concentration of VOCs extracted from the emission outlet of the blowdown 

### Miscellaneous Gas Sensor (MGS)
- hybrid gas sensors use metal oxide semiconductors to detect polluted gases and optical scattering to detect suspended particles (PM)

## Network Devices Image
![[Pasted image 20231024142949.png]]