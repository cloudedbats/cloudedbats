# CloudedBats - free software for bat monitoring

CloudedBats is a hobby project where I want to find out if it is possible, on a spare time basis, to develop some code that covers the whole chain from recording bat sounds to publishing the bat monitoring results in the cloud for free download.

So far I have learned some Raspberry Pi basics and can use a high quality ultrasonic microphone to record bat sounds. The recording unit is placed outside and can be controlled from any unit (computers, smartphones, etc.) connected to my local wireless network. Next step is to learn more about DSP, Digital Signal Processing, to remove empty parts from the sound files and to store them in a more compact way. 

I'm also interested in figuring out what kind of surveys can be done if you can set up 10 - 30 autonomous recording units connected via the internet and record data for the whole season. Computers can not replace a human equipped with a heterodyne in the same way that binoculars still are the birdwatchers best tool, but computers can do some boring and time consuming tasks to help the bat workers and researchers. 

But it's just a spare time project and I will continue as long as I learn a lot and think it's fun. After that, or when you think my progress is too slow, you are free to fork the code and continue the work since it's all open and free...

## WURB - Wireless Ultrasonic Recorder for Bats

All kind of software must be deployed on some hardware. In this case the Raspberry Pi is a perfect choice since it is powerful, available everywhere and not very expensive. The ultrasonic microphone is the most important part in the setup and this is where you should spend your money. For professional use the sampling frequency should be above 300 kHz, but for backyard monitoring 192 kHz will work for most of the bats.

![WURB-A001](images/WURB-A001-web.jpg?raw=true  "WURB - Wireless Ultrasonic Recorder for Bats")
Image: CloudedBats.org / [CC-BY] (https://creativecommons.org/licenses/by/3.0/)

The image above is my first WURB. The setup is as follows:
- [Raspberry Pi 3 B.] (https://www.raspberrypi.org/products/raspberry-pi-3-model-b) This version includes WiFi and Bluetooth on the board.
- Microphone: [Pettersson M500-384 USB Ultrasound Microphone. 384 kHz at 16 bits.] (http://batsound.se/?p=125)
- Powerbank. 2200 mAh, in/out: 5V, 1A.
- USB memory 32 GB for recorded sound files (wav-files).
- Micro SD card with Raspbian Jessie Lite and the CloudedBats software.
- Raspberry Pi Case and some Velcro to keep the microphone in place. 

The WURB contains a web server and is connected to a local network via WiFi. The WURB can be controlled from any device in the local network containing a web browser. For security reasons it is not recommended to open up the local network for external access to the WURB, but it is possible to do that if you can handle the security parts. FileZilla, for example, can be used to access the recorded sound files via the Internet.

#### Power consumption and disk space needed. Empirical test.

With the setup above the WURB is able to operate for about 2.5 hours. A rough estimate gives 5 W (1 A at 5 V) in average. A little bit more power is needed  during startup.

Continuous full spectrum recordings at 384 kHz - 16 bits - mono results in files of this size:
- 10 sec: 7.7 MB
- 1 min: 46.1 MB
- 1 hour: 2.76 GB

#### Issues 
There are some issues when recording sound files. 
Sometimes the signal became completely silent, and this is related to when the computer is busy. Mobile chargers may produce some high frequency signals when they are used instead of the PowerBank. The WiFi module may produce disturbing noise if the microphone is put directly on top of the on the Raspberry Pi as shown in the picture. 
Check the issue tracker for [CloudedBats] (http://cloudedbats.org) for more information. 

## Resouces

#### [http://cloudedbats.org] (http://cloudedbats.org)
This is the software project placed on GitHub where I publish stable versions and documentation for the software. The code is based on Python 2.7 and the web framework [Django](https://www.djangoproject.com). At the moment I’m using Ubuntu for development and Raspbian for deployment, but the code should be possible to run on Windows and Mac too.
I'm planning for some Wiki-pages that describes the software design and how to set up the development environment.

#### [https://github.com/arnoldandreasson/cloudedbats] (https://github.com/arnoldandreasson/cloudedbats)
This is where you can find the latest development version of the software. Versions found here are definitely not stable versions. 

#### [http://backyardbats.org] (http://backyardbats.org)
Points to a GitHub repository under CloudedBats. This is where I put Raspberry Pi related stuff used to set up a WURB, Wireless Ultrasonic Recorder for Bats, unit. 

## About the name *CloudedBats*

CloudedBats is not about [*clouds* of bats] (https://www.google.se/search?q=clouds+of+bats), nor funny patterned animals like the cute 
[*clouded* leopard] (https://en.wikipedia.org/wiki/Clouded_leopard). 

It's more about using *cloud* related technology to make bat monitoring more accessible. 

But all living species, including humans and bats, should in some sense be *clouded* since we are in the beginning of the new epoch of [Anthropocene] (https://en.wikipedia.org/wiki/Anthropocene). 

## Contact

info@cloudedbats.org
