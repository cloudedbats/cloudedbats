# About Raspberry Pi security

When running a CloudedBats-WURB detector as a stand alone
unit, with a mobile phone connected to the WiFi network shared
by the detector, then you don't have to think that much about security.
If the detector is connected to your local network, and not exposed for
access from outside that network, then you also can feel relatively safe.

As soon as the WURB detector is setup for access over internet,
then security is important to think about and you have to take some actions.
The same is valid if you use a server for file backup, web pages or
remote control of the WURB detectors.

## The Raspberry Pi OS

The operating system Raspberry Pi OS is based on the Linux distribution
Debian. A huge number of web servers around the world are also based on
Debian, and the same software packages other uses to make their servers
secure can also be used to make a WURB detector secure.

This is a good start to learn more about both Linux and the Raspberry Pi OS:
<https://www.raspberrypi.com/documentation/>

## Basic rule - the pi user account

The most important thing is to replace the password for the pi user with a
strong password. If an external user can log in to the pi account that have
sudo permissions (which is the same as root privileges) then they have
full control over that computer.

- The length of a password is more important than adding strange characters.
- Even better is to use SSH keys to log in. It is not that complicates and
is really safe. Then you don't have to type that long password each time.
- When using SSH keys it is possible to disable the possibility to
log in using the normal password.

## Next rule - keep the operating system packages up-to-date

A lot of servers are set up once and then continues to run for years without
any routines for implementing upgrades. That is a security risk since
there are many threats that are addressed with the help of an updated software.

- The recommended solution here is to implement a routine that updates the
software automatically. The package for this is called "unattended-upgrades".

## Don't expose all ports

These ports may be used for bat detectors or server computers:

- 22: For SSH.
- 80: For HTTP.
- 443: For HTTPS.
- 873: For Rsync.

If other ports should be used it is good to use the free ports.

- 0 - 1023 are the well-known ports or system ports.
- Ports 1024 - 49151 are called registered ports.
- Ports 49152 – 65535 are free to use.
- More info: <https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers>

When using "port forwarding" only the needed ports should be forwarded.
With port forwarding it is possible to redirect from one external port to another internal port.
For example, the port 52222 can be used externally and then
redirected to port 22 internally.
That will reduce the risk for an external user to find the used SSH port in your
system.
How port forwarding should be setup depends on what system you use to connect
to internet. With modern home networks it is relatively simple.

Then it is also recommended to add a firewall to lock out ports not used.
The recommended firewall here is UFW, the Uncomplicated FireWall.

For protection for incoming traffic via these ports it is then
recommended to use:

- Port 22: Strong login protection like SSH keys.
- Port 80 and 443: A web server/proxy like the Apache HTTP Server, nginx or caddy.
- Port 873: Will be password protected by the rsync system.

## Next step

There is a step-by-step description here:
[Setup Raspberry Pi security](docs/setup_security.md)
