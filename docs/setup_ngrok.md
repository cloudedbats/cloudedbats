# Setup ngrok

This is a step-by-step description to be used when you want access to a
detector or server for http, ssh and sftp without the need of port
forwarding, or similar techniques, for direct access.

Please also check the corresponding document:
[About ngrok](docs/about_ngrok.md)

## Prerequisites

You must have an account registered at ngrok and obtained the
authorization token, the so called "Authtoken".

## Installation

The ngrok software must be installed on the detector. To do this the detector must be
connected to internet and a terminal session should be started. Download and install
the ngrok client software, use the Linux(ARM) version.
You have to copy the correct link for the zip file instead of the one in the example below.

    # Create the ngrok directory.
    mkdir ngrok
    cd ngrok

    # Download the software.
    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
    unzip ngrok-stable-linux-arm.zip

    # Edit the /etc/rc.local file for automatic launch at startup.
    sudo nano /etc/rc.local
    # Add this line to rc.local before the "exit" row:
    sudo -u pi bash /home/pi/ngrok/ngrok_start.sh &

    # Create the startup script.
    nano ngrok_start.sh
    # Add this line to ngrok_start.sh:
    /home/pi/ngrok/ngrok start -config /home/pi/ngrok/ngrok.yml wurb ssh &

    # Edit the ngrok configuration file.
    nano ngrok.yml
    # Add this content to ngrok.yml (to be used as a template, 
    # as least xxxx should be replaced, maybe also the region):
    
    authtoken: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    region: eu
    console_ui: false
    log: /home/pi/ngrok/ngrok.log
    tunnels:
      wurb:
        proto: http
        addr: 8000
        # auth: xx:xx
        # hostname: wurb1.example.org
        # addr: 127.0.0.1:8000
        inspect: false
      ssh:
        proto: tcp
        addr: 22
        # remote_addr: x.tcp.eu.ngrok.io:xxxxxx

If you want the detectors user interface to be password protected, then change "# auth: xx:xx"
to "auth: your-user-name:your-password" (this name/password is no connected to your login, 
choose what you want).

## Running the free plan

Restart the detector.

Go to the dashboard at [https://dashboard.ngrok.com/](https://dashboard.ngrok.com/)
and check "Endpoints - Status".

Then use the links to access your detector or server.

## Running the paid plan

Go to the dashboard at ngrok.
Then go to "Endpoints - Domains" and create a domain. Follow the instructions until you get 
something to setup in the CNAME field that is used to point from the subdomain "wurb1.example.org" 
in the example above.

Do the same at "Endpoints - TCP addresses". 
This will not end up in a customised subdomain, only a ngrok subdomain with a static port
number, but it will at least not change after each restart.

Log in to your domain provider and create a subdomain "wurb1" for the "example.com" domain. 
Use the CNAME value from the earlier step to point to the tunnel endpoint at ngrok.

And finally, log in to the detector and remove the commented lines for "hostname" and "addr"
in the configuration file "ngrok.yml". Then restart the detector.

## Usage example 1, TCP

URL: tcp://x.tcp.eu.ngrok.io:xxxxx

This can be used for SSH:

    ssh pi@x.tcp.eu.ngrok.io -p xxxxx

or for SFTP:

    protocol: SFTP
    host: x.tcp.eu.ngrok.io
    port: xxxxx
    user: pi
    password: xxxxxxxx

## Usage example 2, HTML

Just use the web address [http://wurb1.example.org](http://wurb1.example.org) to access
the detectors web interfaceif you run the paid plan.
Otherwise you have to use the ngrok generated web address from the dashboard.
