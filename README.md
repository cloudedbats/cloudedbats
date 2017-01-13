# CloudedBats - free software for bat monitoring

CloudedBats is a hobby project where I want to find out if it is possible, on a spare time basis, to develop some code that covers the whole chain from recording bat sounds to publishing the bat monitoring results in the cloud for free download.

I'm working on both a recording unit and a web application that can communicate with a number of recording units. The design goal for the recording units hardware is to use standard components only, and it should be possible to put it together with as little soldering as possible. It should support continuous full spectrum recordings at high frequency sampling rate. It should also contain a post-processing step that reduces the file sizes by removing silent slots. 

The web application should have functionality for:

- Configuration and control of a number of recording units.
- Graphical presentations of bat activity in near real time. For disconnected units the results should appear next time the unit is connected to internet.
- Upload, download and visualisation of selected wave files. 
- Support for publishing survey results in the DarwinCore format. 
- Species lists, and maybe other useful information.

The web application is under development and the latest public version for test can be found here: http://test.cloudedbats.org

When finished, and if the project succeeds, I think it could be a useful and affordable set up for bat workers, groups of bat enthusiasts or research teams. Maybe parts of it can inspire others to make their systems better suited for data sharing and collaboration.  

But it's just a spare time project and I will continue as long as I learn a lot and think it's fun. After that, or when you think my progress is too slow, you are free to fork the code and continue the work since it's all open and free...

## WURB - Wireless Ultrasonic Recorder for Bats

All kind of software must be deployed on some hardware. For the recording unit the Raspberry Pi is a perfect choice since it is powerful, available everywhere and not very expensive. The ultrasonic microphone is the most important part in the setup and this is where you should spend your money. For professional use the sampling frequency should be above 300 kHz, but for backyard monitoring 192 kHz will work for most of the bats. Choose one with a good signal to noise ratio.

![WURB-A001](images/WURB-A001-web.jpg?raw=true  "WURB - Wireless Ultrasonic Recorder for Bats")
Image: CloudedBats.org / [CC-BY] (https://creativecommons.org/licenses/by/3.0/)

The image above is my first WURB. The setup is as follows:
- [Raspberry Pi 3 B.] (https://www.raspberrypi.org/products/raspberry-pi-3-model-b) This version includes WiFi and Bluetooth on the board.
- Microphone: [Pettersson M500-384 USB Ultrasound Microphone. 384 kHz at 16 bits.] (http://batsound.se/?p=125)
- Powerbank. 2200 mAh, in/out: 5V, 1A.
- USB memory 32 GB for recorded sound files (wav-files). Enough for 10 hours of continuous  recording.
- Micro SD card with Raspbian Jessie Lite and the CloudedBats software.
- Raspberry Pi Case and some Velcro to keep the microphone in place. 

Power consumption is less than 5 W (1 A at 5 V). The powerbank mentioned above can run it for nearly 3 hours and I use a 11000 mAh powerbank when recording during a full night. 

## Resources

#### [http://cloudedbats.org] (http://cloudedbats.org)
Points to this location, which is the main GitHub repository under [CloudedBats] (https://github.com/cloudedbats/cloudedbats). Documentation and the software for the web application will be stored here. 

The programming language Python is used for all code. Python 2.7 was used for earlier work, and new code is written in Python 3. I’m using Ubuntu 16.04 both for local development and deployment on the web server. I use the same environment when developing the recording unit, but Raspbian Jessie Light is used for deployment on the Raspberry Pi. This means that you don't have to buy a Raspberry Pi to start recording. It will probably work on any computer running Linux, Windows or Mac (but I have not tested it myself yet). Eclipse and PyDev is used as IDE. 

#### [http://backyardbats.org] (http://backyardbats.org)
Points to a GitHub repository under CloudedBats. This is where I put the code for the recording unit and other Raspberry Pi related stuff. 

#### [https://github.com/arnoldandreasson/cloudedbats] (https://github.com/arnoldandreasson/cloudedbats)
This is a repository on my personal GitHub account. I will use it for experimental code during development. 

## Timeline

#### Past
Year 2015: Visited two local bat nights in august 2015. Bought my first heterodyne detector and some books on the topic. Searched for a suitable more advanced detector, but there was no one with internet connection. Decided to build my own based on the Raspberry Pi platform. I was mainly inspired by this page 
http://www.afraidofsunlight.co.uk/weather/index.php?page=bat

Year 2016: Was thinking a lot about how to build an ultrasonic microphone (by using a 500 kHz ADC and the Raspberry Pi PCI interface). But I'm a software developer, not a hardware designer, and when the Pettersson M500-385 was released I bought one directly. Started to record in the beginning of the bat season and tried to learn more about bats and their sound. Species identification is harder than I earlier thought. Even in Sweden with a limited number of species a lot of them are impossible to identify by analysing sound only.

#### In progress
During 2017 the plans are to develop a web application that can interact with a number of recording units. For test I will use three recordings units, two running at 384 kHz and one at 500 kHz. A web server for test and development is already set up, running in a virtual cloud server. The different parts in the web application will be added when they are ready for test. The web application can be found here: http://test.cloudedbats.org

#### Future
A huge amount of data will be produced when using multiple recording units for many nights. Therefore, the natural next step is to develop systems for automatic processing of recorded data and tools for visualising the results. (I'm planning to develop something with scipy/numpy, scikit-learn and bokeh.)

## Licenses and my motivation

The CloudedBats software is released under the MIT license. This means that you are free to use it as you want, even in commercial applications. The only restrictions are that you are not allowed to remove or change the license if you use "substantial portions" of the code, and there is no warranty of any kind connected to the code.

I'm strongly believe in open and free software as well as free data. Therefore I encourage you to release your data under the Creative Commons licenses, CC0 or CC-BY. One of the largest collections of biological data, Gbif.org, have implemented CC0 or CC-BY as the default licenses during the last years. It makes a lot of things easier if you assign one of those licenses to your data as early as possible in the data flow.

My personal motivation for the project is learning by doing. I want to learn more about bats, but also about my favourite programming language Python, biological environmental monitoring in general and how to handle and share huge amounts of data.

## About the name *CloudedBats*

CloudedBats is not about [*clouds* of bats] (https://www.google.se/search?q=clouds+of+bats), nor funny patterned animals like the cute 
[*clouded* leopard] (https://en.wikipedia.org/wiki/Clouded_leopard). 

It's more about using *cloud* related technology to make bat monitoring more accessible. 

But all living species, including humans and bats, should in some sense be *clouded* since we are in the beginning of the new epoch of [Anthropocene] (https://en.wikipedia.org/wiki/Anthropocene). 

## Contact

info@cloudedbats.org
