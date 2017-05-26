# CloudedBats - free software for bat monitoring

Welcome to CloudedBats. 
 
CloudedBats is a software project where I develop free and open source code for bat monitoring. The project's goal is to cover many aspects of bat monitoring; data capture, data management and analysis, cloud storage and publishing of data and results as open data.
 
CloudedBats consists of three main parts:
 
### - Recording units

The recording units are used for passive monitoring to record long sequences of ultrasonic sound in FS (Full Spectrum) or TE (Time Expanded) mode. The recording units can be used in standalone mode or connected to a web server. Since the software can run on most Linux systems the price can be relative low and clusters of recording units can be used.

Development status: Works well as standalone units. Web integration in progress.

Images below. Feature list, source code, etc.: https://github.com/cloudedbats/cloudedbats_wurb
 
### - Web page
The main purpose for the web page is to control a number of recording units and to visualise bat activities on different time scales. Modules for data management and surveys are planned.

Development status: Basic design finished and test server is running. Integration with recording units in progress. Other modules later.

Test server: http://test.cloudedbats.org 

Feature list, source code, etc.: https://github.com/cloudedbats/cloudedbats_web
 
### - Cloud storage and processing
Today, there are many interesting alternatives for storage and computation of large amounts of data in the cloud. When working with clusters of detectors, we will need that capacity.

Development status: Planning.

## WURB - Wireless Ultrasonic Recorder for Bats

All kind of software must be deployed on some hardware. For the recording unit the Raspberry Pi is a perfect choice since it is powerful, available everywhere and not very expensive. The ultrasonic microphone is the most important part in the setup and this is where you should spend your money. For professional use the sampling frequency of 384 kHz is enough for European bats and 500 kHz is needed for some other species. For backyard monitoring 192 kHz will work to detect peak frequencies for many bats. Choose a sensitive one with a good signal to noise ratio.

### First recording unit ###

![WURB-A001](images/WURB-A001-web.jpg?raw=true  "WURB - Wireless Ultrasonic Recorder for Bats")
Image: CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

The image above is my first WURB (from early 2016). The setup was as follows:
- [Raspberry Pi 3 B.](https://www.raspberrypi.org/products/raspberry-pi-3-model-b) This version includes WiFi and Bluetooth on the board.
- Microphone: [Pettersson M500-384 USB Ultrasound Microphone. 384 kHz at 16 bits.](http://batsound.com/?p=125)
- USB memory 32 GB for recorded sound files (wav-files). Enough for 10 hours of continuous recording.
- Powerbank. 2200 mAh, in/out: 5V, 1A. Enough for about 3 hours.
- Micro SD card with Linux (Raspbian Jessie Lite) and the CloudedBats software.
- Raspberry Pi Case and some Velcro to keep the microphone in place. 

This early version contained a web server for configuration and control from any device in the local network running a web browser. This solution was later replaced by more practical alternatives for configuration and control. 

### Devices for the bat season 2017 ###

![WURB-A001](images/CloudedBats_hw_2017.jpg?raw=true  "Recording devices for 2017")
Image: CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

For field tests during 2017, I will use three different recording units. The software used is the same for all three devices, but the hardware configuration differs to match three different usage cases.

**Left device:** The unit will be lent to friends and others who are interested in knowing more about what is flying in their garden and elsewhere. It must therefore be as easy as possible to handle.
Hardware configuration: Microphone Pettersson M500-384 (384 kHz), RaspberryPi2B, no WiFi, GPS (an old version), 32 GB USB Memory. Most power sources used for smart phones can be used.

Short usage description: Both switches in the middle position and connect power. GPS gives input to the scheduler to start at sunset and stop at sunrise. Recordings starts automatically when sound above 15 kHz are detected, including buffered sound before and after. All sound files are named with time and position. When done, move the RPi switch to 'Off' and disconnect power. Move the USB memory to a computer for analysis. (Personally I use the free software Sonic Visualiser (http://www.sonicvisualiser.org/) for analysis.)

**Center device:** Mobile unit for transects and overnight at places of interest.
Hardware configuration: Pettersson M500-384 (384 kHz), RaspberryPi3B, WiFi, GPS/Galileo, 64 GB USB memory, wireless mouse for remote control. Power bank for more than 12 hours of operation (11 Ah).

**Right device:** Stationary device for long term monitoring.
Hardware configuration: Pettersson M500 (500 kHz. M500 is normally for Windows only, but can be used here.), RaspberryPi3B, WiFi, no GPS (position via settings), 1 TB USB disc (enough for a whole season). Powered by 12 V car battery (note the battery protection device to protect the battery against deep discharge). The stationary device should continuously report bat activities to the web application (work in progress). It is also possible to access the unit via SSH and SFTP (for file transfer) from any computer in the local network, or remotely if the network is setup for external access.

## Resources

GitHub is used as a project platform and source code repository by many open source projects and by developers of open source libraries. CloudedBats is build as at thin layer on top of many of these libraries. The CloudedBats project is also stored on GitHub as a GitHub organisation. Link to the CloudedBats organisation: https://github.com/cloudedbats

The CloudedBats organisation is divided into a number of repositories for documentation and/or software code. These repositories can be seen as subprojects, and they are:

- **https://github.com/cloudedbats/cloudedbats**
This repository. Contains some info about the project. The web domain http://cloudedbats.org also points to this repository.

- **https://github.com/cloudedbats/cloudedbats_wurb** 
Contains software and documentation for the recording unit. The recording unit is called WURB - Wireless Ultrasonic Recorder for Bats.

- **https://github.com/cloudedbats/cloudedbats_web**
Contains software and documentation for the web page. 

- **https://github.com/cloudedbats/cloudedbats_dsp** 
DSP - Digital Signal Processing is important when sound should be automatically analysed. This repository will contain experimental code and software used to process Wave files. Results will later be implemented in the WURB, on the web and in the cloud.

- **https://github.com/cloudedbats/cloudedbats_cloud** 
The cloud will be used for storage and processing of recorded data. Future work.

- **https://github.com/cloudedbats/backyardbats** 
Contains Raspberry Pi related stuff. 
The web domain name http://backyardbats.org points here.
At the moment the software stored here is not needed to set up a CloudedBats system. 

## Timeline

#### Past
Year 2015: Visited two local bat nights in august 2015. Bought my first heterodyne detector and some books on the topic. Searched for a suitable more advanced detector, but there was no one with internet connection and processing capacity. Decided to build my own based on the Raspberry Pi platform. I was mainly inspired by this page 
http://www.afraidofsunlight.co.uk/weather/index.php?page=bat

Year 2016: Was thinking a lot about how to build an ultrasonic microphone (by using a 500 kHz ADC and the Raspberry Pi PCI interface). But I'm a software developer, not a hardware designer, and when the Pettersson M500-385 was released I bought one directly. Started to record in the beginning of the bat season and tried to learn more about bats and their sound. Species identification is harder than I earlier thought. Even in Sweden with a limited number of species a lot of them are nearly impossible to identify by analysing sound only.

#### In progress
During 2017 the plans are to develop a web application that can interact with a number of recording units. For test I will use three recording units, two running at 384 kHz and one at 500 kHz. A web server for test and development is already set up, running in a virtual cloud server. The different parts in the web application will be added when they are ready for test. The web application can be found here: http://test.cloudedbats.org

#### Future
A huge amount of data will be produced when using multiple recording units for many nights. Therefore, the natural next step is to develop systems for automatic processing of recorded data and tools for visualising the results. (I'm planning to develop something with scipy/numpy, scikit-learn and bokeh.)

## Licenses and my motivation

The CloudedBats software is released under the MIT license. This means that you are free to use it as you want, even in commercial applications. The only restrictions are that you are not allowed to remove or change the license if you use "substantial portions" of the code, and there is no warranty of any kind connected to the code.

I'm strongly believe in open and free software as well as free data. Therefore I encourage you to release your data under the Creative Commons licenses, CC0 or CC-BY. One of the largest collections of biological data, Gbif.org, have implemented CC0 or CC-BY as the default licenses during the last years. It makes a lot of things easier if you assign one of those licenses to your data as early as possible in the data flow.

My personal motivation for the project is learning by doing. I want to learn more about bats, but also about my favourite programming language Python, biological environmental monitoring in general and how to handle and share huge amounts of data.

## About the name *CloudedBats*

CloudedBats is not about [*clouds* of bats](https://www.google.se/search?q=clouds+of+bats), nor funny patterned animals like the cute 
[*clouded* leopard](https://en.wikipedia.org/wiki/Clouded_leopard). 

It's more about using *cloud* related technology to make bat monitoring more accessible. 

But all living species, including humans and bats, should in some sense be *clouded* since we are in the beginning of the new epoch of [Anthropocene](https://en.wikipedia.org/wiki/Anthropocene). 

## Contact

Arnold Andreasson, Sweden.

info@cloudedbats.org
