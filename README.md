# CloudedBats - free software for bat monitoring

## Latest news (2021-01-17)

There are some major updates in the CloudedBats-WURB-2020 detector (https://github.com/cloudedbats/cloudedbats_wurb_2020).

- A more intuitive layout of the user interface.
- User defined settings alternatives.
- Better support for alternative sound cards.
- Audio feedback via Headphones from the 3.5 mm jacket.

Testing and some more additions should be done before this ends up in the v0.9 release. Please report back, all kinds of feedback are welcome.

## Latest news (2020-07-12)

After a break I'm back with a completely rewritten software for the WURB detector. The new WURB version can be found here:
https://github.com/cloudedbats/cloudedbats_wurb_2020 

The repositories in the CloudedBats GitHub organization (https://github.com/cloudedbats) contains a lot of useful code snippets 
and some not finished applications. I will try to use what I have learned so far about bat sound and bat sound processing to develop
a new and better bat sound processing pipeline. The first part in that new pipeline is the "data capture" part, the new WURB detector.

The final goal is the same; to develop free and open source software for all parts from data capture to quality approved survey data
stored in the DarwinCore-Archive format. And both AI and the cloud should be used for a more efficient management of recorded sound files.

Another goal is to focus on bat species where reference recordings not are available. That means that AI with "supervised learning" is not 
an option. This repository contains software used to extract and store info about all bat species covered by the IUCN Redlist: 
https://github.com/cloudedbats/cloudedbats_species and the AI system must be able to support them all.



## ===== Old texts that may be updated, some day... =====

Welcome to CloudedBats.

Bats have became my new hobby. They are extremely fascinating mammals, and we need to know more about them. But it's hard to study bats without a lot of technical stuff. 

When searching for advanced bat detectors I realised that there are many alternatives, but all of them are really expensive and without the processing capacity I was looking for. Therefore, I decided to build my own system. I have been working as a software developer for many years and this is a great opportunity to upgrade my "personal toolbox" and include things like Raspberry Pi, digital signal processing, cloud computing and machine learning. 

I'm using the programming language Python for all software in the project and the code is divided into several GitHub repositories under the GitHub organisation https://github.com/cloudedbats 

The CloudedBats software is completely open and free and you can use it as you want, even as a part in a commercial product. Personally, I have no plans to put together "products" based on the software and sell for profit. But I will be happy if someone else does, or just use the CloudedBats software as an inspiration or as a template for other projects. Contact info at the end of this page.

## Bats

It all started at a local bat walk in the botanical garden in Gothenburg, Sweden. It was in August 2015. After that I started to read about bats and bought my first heterodyne detector to find out what's flying around our house at night. 

The most common bat species where I live is definitely the Northern bat, *Eptesicus nilssonii* (or at least the one that is easiest to detect). The nice little Brown long-eared bat, *Plecotus auritus*, is hibernating during winter in an underground storehouse 15 m from our house. One or two Myotis species lives nearby and a few other species are more or less regularly passing by.

![Plecotus auritus](images/Plecotus_auritus_sweden.jpg?raw=true  "*Plecotus auritus*")
*Plecotus auritus* hibernating near our house. Potatoes, bats and the spider *Meta menardi* are enjoying the same environment during winter. CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

After some years of reading, recording and analysing bat sounds, following the Swedish bat Facebook group, some meetings/workshops with Swedish bat enthusiasts, joining EBRS 2017 (the 14:th European Bat Research Symposium) and the following Bat detector workshop in Bidarray and a similar workshop in Norway I think I'm prepared to dive into the more cloudy part of the project.

## Main scenario and project requirements

When designing new software systems there are two main approaches. One is to take something existing and improve it step by step. Another way to do it is to set up a distant goal and try to get there without looking back too much. The basic idea for the CloudedBats project is to think like this: If someone ask me to build a completely new system for bat monitoring, based on techniques available today, what hardware/platforms and software libraries should I then use for it.

### Scenario

A fictitious, but realistic, scenario:

"We want to investigate bats in a tropical region with more than 100 known species. 100 passive detectors should be used during two years and they should be moved to new places each week following a predefined schema. We don't have reference sound recordings for the majority part of the species in the area. Therefore we need fast data analysis that gives us the possibility to go to a place some days after to catch bats, mark them and record new reference sound files. Locally there is a group of people working with environmental conservation and wildlife guiding as well as a small a group of technicians. Bat experts and researchers are spread over the world. Alternatives to air travel (for humans, not for bats) should always be considered. Collected data should be published for free to be used in many research projects, both during the survey and afterwards."

The total amount of data collected if all detectors are running 12 hours per night is 3153.6 TB or 876000 hours of ultrasonic sound. That's a huge amount of data. Calculation: 100 detectors * 365 days * 2 year * 12 hours per night * 3600 sec per hour * 500 kHz * 16 bits / 8 bits per byte.

### Requirements

From this scenario some basic requirements can be defined:

- The detectors used for passive monitoring must be easy to handle.
- Data must be processed more or less automatically.
- Results in a compressed format should be sent and shared over Internet.
- Metrics from recorded sound should be extracted automatically at different timescales.
- Similar sound must be grouped together to avoid too much space needed for long time storage. This is also used to reduce the amount of data needed to be sent over Internet.
- Extracted metrics must be stored in formats that makes it possible to apply extensive statistical analysis.
- High resolution wave files must be handled and stored for species identification activities.
- Metadata for the whole survey must be stored and published together with other results.
 
## CloudedBats - software parts

At the EBRS 2017 symposium I had a poster presenting the CloudedBats project. The poster provides an overview of the entire project: 
[EBRS 2017 Poster](doc/EBRS2017_CloudedBats_poster_FINAL.pdf).

The following subheadings are based on the 10 steps described in the poster, but with further and more updated information. 

### 1. Ultrasonic microphone

Bats are smart animals. Therefore, they adapt their sounds according to the prerequisites, and although there are some typical sound elements for many species, there are many sounds that overlaps between species. Another thing that makes it complicated is the fact that an audio image looks different depending on the distance to the microphone. There are a lot of other factors like temperature, humidity, and even the angle towards the microphone that can make identical sounds look different. Therefore, it is good to have high quality microphones that do not distort the signal further, and it is especially true if we want to make sound analysis automatically.

I have decided to use USB connected ultrasonic microphones and Pettersson M500-384 (running at 384 kHz) is the one that I use most of the time. Sometimes a sampling frequency of 500 kHz is needed, and Pettersson USB microphone M500 can handle that (with some low level coding since the M500 mic. is designed to run on Windows only and the recording unit I use is running Linux). 

### 2.  Detector for passive monitoring

I have used my own design of a detector for passive monitoring since 2016. 

A short presentation is included in this presentation from the norwegian workshop in 2018:
[Three inexpensive detectors](doc/EABDW3_Three_Inexpensive_Bat_Detectors.pdf).

The development of the detector (called WURB, Wireless Ultrasonic Recorder for Bats) is more or less finished for my own purposes and I regularly use three units myself as passive detectors.

![WURB-A001](images/WURB-A001-web.jpg?raw=true  "CloudedBats recording unit.")
The first WURB from 2016. CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

This is a short description of the hardware from the EBRS 2017 poster: 
"Microphone (350€+VAT), Raspberry Pi 3B computer (40€), case (10€), Micro-SD for software (15€), USB memory for sound files (15€), GPS (20€). Any power supply for smartphones can be used, for example a mobile phone charger or a powerbank (10-30€)."

More info here: https://github.com/cloudedbats/cloudedbats_wurb 

### 3.  DSP, Digital Signal Processing

DSP is about working with digitalised sound in both the time domain and in the frequency domain. In the frequency domain it is possible to extract, for example, start and end frequencies and other things that can be checked when looking at a spectrogram.

In CloudedBats we need DSP at different steps in the data flow. 

- In the recording unit there is a need to separate timeslots with sound and silent slots. 
- We also want to separate bat sound from other sounds like wind blowing in the leaves, rain, running water, insects, ultrasonic sound from electronic equipment, etc.
- There is a need for extracting metrics from both single sound pulses and sequences of pulses. 
- Another usage is to reduce the amount of data needed to be sent over Internet for visualisation purposes. You don't need to use the full frequency file just to display some points in a diagram to show the shape of the pulses in a sequence of pulses. Zero Crossing, ZC, is a good example of this.
- When working with Machine Learning an important part is called "feature engineering". In CloudedBats we have the possibility to put the feature engineering part in the recording unit and then run the machine learning algorithms in the cloud. 

More info here: https://github.com/cloudedbats/cloudedbats_dsp  

I'm planning to put the code for extracting sound components in this repository: https://github.com/cloudedbats/cloudedbats_sound

### 4.  Presentation and visualisation

One basic idea for CloudedBats is to not use installed applications on personal computers. Any device that can run a web browser should be enough. If someone must take the SD card and process it on their computer at home or at the office the data flow will be much slower.

More info here: https://github.com/cloudedbats/cloudedbats_web 

and here: https://github.com/cloudedbats/cloudedbats_web (future work)

and to some extent also here: https://github.com/cloudedbats/cloudedbats_pathfinder 

Updated 2018-03-18: I have completely failed in my ambitions to not include a desktop application in the CloudedBats setup, sorry for that. (I really want to develop a system that works for all those great people working with biology, but really hates to install software on desktop computers). The desktop application will run on Windows, MacOS, Linux (Ubuntu) as single file executables. 

I have started the development of the desktop application and the repository can be found here: https://github.com/cloudedbats/cloudedbats_desktop_app

### 5.  Species lists

A species list to be used as a taxonomic backbone is needed when working with species. CloudedBats uses the IUCN Red List of Threatened Species for this. One reason for this is that I think this is one of the best species list on a global level that is constantly maintained. Another reason is that there is a software API that can be programmatically called. 

More info here (including an Excel file that can be used directly): https://github.com/cloudedbats/cloudedbats_species

### 6.  Reference libraries for bat sound

It is not possible to train computers to identify bats without reference libraries of sound. They are difficult and expensive to develop and must probably be based on caught and marked bats. For the CloudedBats project I need high resolution wave file as reference files. 

There exists some databases containing extracted metrics only. They can't be used since modern algorithms can handle hundreds or thousands of parameters/features extracted from a sound file. After a careful feature engineering activity maybe the number of used features are reduced, but they will probably differ from the parameters stored in these databases.

Updated 2018-03-18: Maybe reference libraries will work for the limited amount of European bat species. When recording in other ecological regions we probably will need both FS recordings and an identification level before the species identification to group similar sound together. For example on a format of this type: "40 st.cFM" for some *Mineopterus* species in some region. Maybe it is possible to do this first step of classification automatically and the let the experts do the final step to species level. From my point of view this is some kind of "feature engineering" similar to what's needed for a future automatic classification based on more data than the sound itself.

### 7.  Species identification - Machine/Deep Learning

This seems to be nearly impossible for some species, even for the limited amount of species found in Europe. But the development of new machine learning algorithms takes place quickly.

But we can use Machine/Deep Learning to work with huge amounts of recorded data without the need for established reference libraries of sound. Instead of using reference libraries we can use the computers to group together similar sounds from a huge dataset and the bat specialist only have to check some of them.

Working with Machine/Deep Learning is a craftsmanship where you need to practice your skills. It's probably takes as long to get skilled in this area as it does to become a skilled bat worker. We still need a lot of HI, Human Intelligence, to use it in the right way, and garbage in will produce garbage out, as always.

Book: "Hands-On Machine Learning with Scikit-Learn and TensorFlow" by Aurelien Geron.

Courses: There are many available at https://www.coursera.org/ (but so far I have only followed the shorter ones embedded in "gcp-data-machine-learning" mentioned below.)

### 8.  Storage and processing in the cloud

In the CloudedBats project I'm trying to eliminate the time-consuming work of moving memory cards from detectors to personal computers for analysis. Instead, the recording unit should be smart enough to automatically feed a dataflow into the cloud. Wave files (Time Expanded or Full Scan) are still stored on the USB memory connected to the recording unit, but a user should know in advance which files are of interest based on metrics already sent to the cloud. High resolution wave files of interest should be possible to order from the 	recording unit for upload to the cloud and later download for deeper analysis.

This kind of data flow could then be used for different purposes. For the case in the main scenario to handle large amounts of data during an ongoing survey, but also to build systems presenting graphics for bat activities from detectors placed at places of public interest. For example in a botanical garden or a city park near water.

The cloud system for CloudedBats will be based on the "Google Cloud Platform". Components to be used are "Cloud Storage", "Cloud Pub/Sub", "Cloud DataFlow", "BigQuery" and "Cloud Machine Learning", etc.

More info here: https://github.com/cloudedbats/cloudedbats_cloud 

### 9.  Survey results, reporting formats

Inventory reports, scientific articles and data papers contain a lot of important data that has better impact if it is spread. CloudedBats will have support for the exchange data format DarwinCore-Archive, DwC-A. 

I have done some work using DarwinCore-Archive for marine biological monitoring data and I think this is the most promising format today for data exchange regarding biological monitoring data.

CloudedBats source code, etc.: https://github.com/cloudedbats/cloudedbats_darwincore 

### 10.  Storage for future generations

Natural History Museums have collected and stored specimens of flowers, insects and birds for centuries. Recently, the museums also have started to store digital information, such as images and DNA sequences. Therefore, I think the Natural History Museums are well adapted for managing reference recordings of bat sounds. 

National GBIF (Global Biodiversity Information Facility) nodes use the DarwinCore-Archive format for data exchange and there is an existing infrastructure to handle and indexing results from surveys, etc. 

### Final project goal

The CloudedBats software project is finished when I have developed software for the complete data flow from the ultrasonic microphone to quality approved results stored at GBIF.org (https://www.gbif.org/occurrence/search?taxon_key=734).

When this is done I probably need a new, and less demanding, hobby...

# Software design 

The requirements from the main scenario above forces the software to be designed to handle a data flow that is some magnitudes higher than what a single human can handle. Therefore I have to use powerful software tools. Most of them are new to me, but I want to learn more about them, and this project is a good way to do that. And since there is no deadline for the project I can take the time needed to do that. 

## System overview

The CloudedBats organisation at GitHub is divided into a number of repositories. They are related to each other as described in this overview:

![System overview](doc/CloudedBats-system-overview.png?raw=true  "System overview")
Software repositories for CloudedBats. CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

## Python and R

The programming language Python is used for all software developed in the CloudedBats project. The reason is that it is open and free, runs on Linux, Windows and macOS, and it is a great language for scientific use with a huge amount of really good libraries. Another really good language is R that I recommend for people working mainly with data, statistics and visualisation of data. Python and R have a lot in common and it is easy to combine them. For example, let R take care of the final step in a data flow that is mainly handled by Python.

CloudedBats is build on top of modern software libraries, and most of the best software developed in, for example, C and C++ have a corresponding wrapper that makes it accessible from Python. When looking for libraries to use I always starts to look at libraries at NumFOCUS (https://numfocus.org) and PyData (https://pydata.org/downloads/) since many of them are founded by numFOCUS. Together these libraries is a good stack of tools to use when working with scientific data.

## GitHub repositories

### WURB, Wireless Ultrasonic Recorder for Bats

This is the main unit for data capture, i.e. to record sound from bats. I use a high quality ultrasonic microphone and inexpensive standard hardware like the Raspberry Pi computer.
It is mainly designed for passive monitoring, but can also be used for transects, etc. 

Status: Stable version including a short user documentation.

Repository: https://github.com/cloudedbats/cloudedbats_wurb


## Pathfinder

Pathfinder is a complement to the previous detected and it is should be used as a handheld detector. The Design goal for the pathfinder is to make it as simple as possible to operate. Basically the same hardware as the WURB, but a user can run it from a web browser by connecting to the WiFi connection shared by the Pathfinder.

Status: Work in progress. A preliminary plan is to have a working unit before the 2019 bat season.  

Repository: https://github.com/cloudedbats/cloudedbats_pathfinder

## Web

The purpose of the web application is to serve a cluster of WURB detectors. 

Status: Work in progress. A prototype for the user interface was developed some years ago, but nothing more after that. 

Repository: https://github.com/cloudedbats/cloudedbats_web

## Desktop app

This is a traditional application for desktop computers. Will cover all levels from project/survey to automatic processing of recorded files.

![Desktop app](https://github.com/cloudedbats/cloudedbats_desktop_app/blob/master/images/CloudedBats-DesktopApp_2019-03-30.jpg?raw=true  "Desktop app")
Desktop application. Items inside brackets indicates work in progress or future work. CloudedBats.org / [CC-BY](https://creativecommons.org/licenses/by/3.0/)

Status: Work in progress. The framework for the user interface (Qt5) and file storage (HDF5) is finished. It is possible to build single file executables for Windows, macOS and Linux.

Repository: https://github.com/cloudedbats/cloudedbats_desktop_app

## Cloud

Google offers a very rich, powerful and cost effective infrastructure that can be used later in this project.  

Status: For future work. Will be used to store data and for demanding calculations when clusters of processors are needed. Maybe also for streaming of real-time data from many detectors by using the Google Cloud infrastructure. 

Repository: https://github.com/cloudedbats/cloudedbats_cloud

## Libraries:

### dsp4bats

Library for basic sound processing. 

Status: Working both in the time and the frequency domains.
Repository: https://github.com/cloudedbats/cloudedbats_dsp

### sound4bats

Library to be used to extracting sound components from sound files.

Status: Future work.
Repository: https://github.com/cloudedbats/cloudedbats_sound

### ml4bats

Library for machine and deep learning.

Status: Future work.
Repository: https://github.com/cloudedbats/cloudedbats_ml (not available)

### species4bats

Library for taxonomic information regarding all Chiroptera species.

Status: Working for all Chiroptera species in the IUCN Redlist database.
Repository: https://github.com/cloudedbats/cloudedbats_species

### analysis4bats

For analysis of extracted bat sound components.

Status: Future work.
Repository: https://github.com/cloudedbats/cloudedbats_analysis

### hdf54bats

Library for data structures stored on disk based on HDF5. This is a better solution than running everything in memory, or to use a relational database.

Status: Work in progress. I need it for the desktop application.
Repository: https://github.com/cloudedbats/cloudedbats_hdf5

### metadata4bats

Library for all kinds of metadata. Metadata for projects, surveys, recording events, recordings, analyses, etc.

Status: Work in progress. I need it for the desktop application.
Repository: https://github.com/cloudedbats/cloudedbats_metadata

### darwincore4bats

Library for handling the DarwinCore-Archive format. This is a format for data exchange developed for biological data. 

Status: Future work.
Repository: https://github.com/cloudedbats/cloudedbats_darwincore

## About the name *CloudedBats*

CloudedBats is not about [*clouds* of bats](https://www.google.se/search?q=clouds+of+bats), nor funny patterned animals like the cute 
[*clouded* leopard](https://en.wikipedia.org/wiki/Clouded_leopard). 

It's more about using *cloud* related technology to make bat monitoring more accessible. 

But all living species, including humans and bats, should in some sense be *clouded* since we are in the beginning of the new epoch of [Anthropocene](https://en.wikipedia.org/wiki/Anthropocene). 

## Contact

Arnold Andreasson, Sweden.

info@cloudedbats.org

<br/>
<p align="center">
  <img src="images/logo/cloudedbats_logo_original-text_gimp.png" align="center" width="150">
</p>
