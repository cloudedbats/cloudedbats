
# Raspberry Pi security

When running a CloudedBats-WURB detector as a stand alone
unit with a mobile phone only connected to the WiFi network shared 
by the detector, then you don't have to think that much about security. 
If the detector is connected to your local network and not exposed for 
access from outside that network then you can also feel relatively safe.

As soon as the WURB detector is setup for access over internet, 
then security is important to think about and you have to take some actions.

The operating system Raspberry Pi OS is based on the Linux distribution 
Debian. A huge number of web servers are also based on Debian and 
the same software packages other uses to make their servers more secure 
can also be used to make a WURB detector more secure.

The same is also valid if you set up, for example, a backup server for 
recorded files that is accessible over internet.

This instruction focus on these basic steps:

- A server should always be updated when new version of standard packages are released.
- Only needed ports should be exposed. In this case port 80 and 22.
- For port 80 an established web server/proxy, like Nginx, should be used.

For security reasons a server that i available over internet it is 
important that it always is updated with the latest set of software packages.
The package unattended-upgrades can do that automatically.


## Update and upgrade.

Before installing software the computer should be updated/upgraded 
to the latest software packages at the moment.

    sudo apt update
    sudo apt upgrade

## Activate automatic update/upgrade

If you don't want to update/upgrade manually on a regular basis, 
then it can be done automatically:

    sudo apt install unattended-upgrades
    sudo dpkg-reconfigure --priority=low unattended-upgrades

Answer YES in the configuration application that is activated by the command.

## Firewall, the UncomplicatedFirewall (UFW)

In most cases the ports 80 (for http) and 22 (for ssh) are needed for 
incoming traffic and all other ports can be blocked.
Port 80 should be handled by Nginx.
Port 22 will always ask for username and password.

**Warning: If UFW is activated and port 22 is not allowed, then is 
is impossible to continue with access over ssh. 
It that happens the only way is to use an HDMI-monitor and a keyboard
to to a correct UFW configuration.**

    # Install the package.
    sudo apt install ufw

    # Allow ports.
    sudo ufw allow 22
    sudo ufw allow 80

    # Example of a more reduced strategy.
    ## sudo ufw allow from 192.168.1.100 port 22

    # Useful commands.
    sudo ufw show added
    sudo ufw status verbose

    # Enable/disable UFW.
    sudo ufw enable
    sudo ufw disable

## Security for port 80, http.

How to set up Nginx in front of a web application is
described here:

- docs/setup_rpi_nginx.md 

With Nginx it is possible to password protect your
WURB detector when controlling it over internet.
This is covered in the description mentioned above.
