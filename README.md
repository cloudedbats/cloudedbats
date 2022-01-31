# CloudedBats - free software for bat monitoring

## Welcome to CloudedBats

CloudedBats is my hobby/spare-time project where I'm trying to develop a complete set of open and free software tools to be used when acoustically monitoring bats.
In the end it should cover the whole path from the ultrasonic microphone to well documented survey results that can be shared.

## The CloudedBats-WURB detector

To start monitor bats acoustically you need a bat detector.
In this project I have developed a Do-It-Yourself (DIY) bat detector based on the Raspberry Pi computer.

Check this GitHub repository if you want to build your own bat detector:
[The CloudedBats_WURB_2020 detector.](https://github.com/cloudedbats/cloudedbats_wurb_2020)

There is a user manual for basic usage:
[User manual.](https://github.com/cloudedbats/cloudedbats_wurb_2020/blob/master/docs/user_manual_basic.md)

## Website for non-technical users

One problem with this kind of software projects is that there are too many technical aspects that must be handled.
Therefore I have started to describe the overall project on a separate website powered by GitHub Pages.
That website will focus on "what" and "why", while this page also will contain the "how" part from a technical perspective.

The "what" and "why" website:
[cloudedbats.github.io](https://cloudedbats.github.io/)

## The next step

Since the CloudedBats-WURB detector is based on the Raspberry Pi computer running Linux there are nearly
no limitations in what you can do in terms of interactions with other computers on the internet.

When running the CloudedBats-WURB detector in the basic mode it is completely isolated from internet.
The detector creates its own WiFi network to which a client computer or mobile phone can connect,
and then access the detectors internal web server. In that case security is not a big issue.

But why should we stop here? We have a detector that can connect to internet via WiFi, Ethernet or
even 4G/LTE by using a USB modem. But then we must start to think about security.

### What can be done?

I think a lot of time can be save if detectors can be controlled and managed remotely.
And that can also make it easier to work together.

With a Raspberry Pi based detector it is possible to do this:

- Open it up for remote access. That means that the detectors user interface can be run remotely,
that recorded files can be downloaded directly from the detector, 
and that maintenance can be done by running terminal commands over ssh.

- The detector can automatically backup recorded files to a server or a cloud service.

- It is possible to setup a "read only" account to let your friends also download files
from your detector.

- Use the detector to run post processing activities. A Raspberry Pi 4 is really powerful
and why should the detector idle during daytime?

### Work in progress

At the moment I'm working on a setup with a number of detectors that are connected to a
central server. The hardware parts are:

- **The server**: It is a Raspberry Pi 4 computer with an external 4 TB disk attached.
The server is a part of my home network and since I have a public IP address it can be
accessed from internet. It is setup as a backup server, a web server and as a central
node for communication with the detectors described below.

- **Permanent detectors**. I have one permanent detector that is a part of my local home network.
It uses Ethernet with Power-over-Ethernet, PoE. WiFi should also be possible to use, but
the speed is better with Ethernet and PoE is handy.

- **Master detectors**. Master detectors are detectors that are using 4G/LTE modems for internet access.
They can be deployed anywhere where 4G/LTE is available and then they connects automatically to my home server.
They also share WiFi access that makes them usable for the next group; slave detectors.

- **Slave detectors**. These detectors are using WiFi and contains a list of predefined WiFi
networks they are trying to connect to. They will also connect automatically to my home server
when internet is available. The new Raspberry Pi Zero 2 should be a good candidate to run as
a slave detector.

### Security

TODO...

### Installation guides

TODO... (some work in progress here: [docs](https://github.com/cloudedbats/cloudedbats/tree/master/docs) )

## Contact

Arnold Andreasson, Sweden.

info@cloudedbats.org