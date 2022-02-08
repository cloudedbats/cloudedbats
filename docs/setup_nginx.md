# Setup nginx

This is a step-by-step description to be used when setting up
the web and proxy server nginx.

Please also check the corresponding document:
[About nginx](docs/about_nginx.md)

## Prerequisites

- A permanent external IP address for the actual network.
- Some subdomains that points to that IP address.
- Port forwarding activated to route the used ports to the
Raspberry Pi computer.

In the following examples we assume that there exists:

- A public IP address: 123.123.123.123, or access via
RaspAP and IP 10.3.141.1.
- A subdomain for the detector: wurb1.example.org.

The subdomain should be setup with port forwarding if the public
IP address is used.

### If RaspAP is used

RaspAP is sometimes used to set up a WURB detector as an WiFi
access point. The administration page for RaspAP uses port 80
by default. In the example below we want to use port 80 to access
the detectors web based user interface.
To do that we first have to change the port used by RaspAP.

Open the RaspAP administration page, select the "System" menu
and change the port to, for example, 8080.

RaspAP: System - Advanced - Web server port: 8080

## Install software packages

    sudo apt update
    sudo apt upgrade

    sudo apt install nginx
    sudo apt install apache2-utils

## Useful commands

    # Start and stop.
    sudo systemctl start nginx
    sudo systemctl stop nginx

    # Gracefully reload and forced restart.
    sudo systemctl reload nginx
    sudo systemctl restart nginx

    # Launch on boot.
    sudo systemctl enable nginx
    sudo systemctl disable nginx

    # Check.
    sudo systemctl status nginx

## Username/password

Use this if you want the WURBs web user interface to be
password protected.

    sudo htpasswd -c /etc/nginx/.htpasswd first-user-name
    # Next time when .htpasswd is created.
    sudo htpasswd /etc/nginx/.htpasswd another-user-name

## Basic Nginx config

Edit the Nginx configuration file.

    sudo nano /etc/nginx/nginx.conf

Uncomment these lines in "/etc/nginx/nginx.conf":

    server_names_hash_bucket_size 64;
    server_name_in_redirect off;

Remove the link to the default configuration.

    sudo rm /etc/nginx/sites-enabled/default

## Create the Nginx configuration file

Edit the configuration file.

    sudo nano /etc/nginx/sites-enabled/wurb_nginx.conf

    # Add these rows, and modify them to fit your needs:

    # Upstream for the WURB detector.
    upstream upstream-wurb1 {
        # Connected to the local network.
        server localhost:8000;
    }

    # Public call to the WURB detector.
    # Not password protected if call through the RaspAP WiFi network.
    server {
        listen 80;
        server_name 10.3.141.1;

        # The WURB detector.
        location / {
            proxy_pass http://upstream-wurb1/;
            proxy_set_header Host $host;
        }
        # For WebSocket communication.
        location /ws {
            proxy_pass http://upstream-wurb1/ws;
            proxy_http_version 1.1;
            proxy_set_header Upgrade "websocket";
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
        }
    }

    # Public call to the WURB detector, password protected.
    server {
        listen 80;
        server_name wurb1.example.org 123.123.123.123;

        # The WURB detector.
        location / {
            proxy_pass http://upstream-wurb1/;
            proxy_set_header Host $host;
            # Login needed.
            auth_basic "Restricted Content";
            auth_basic_user_file /etc/nginx/.htpasswd;
        }
        # For WebSocket communication.
        location /ws {
            proxy_pass http://upstream-wurb1/ws;
            proxy_http_version 1.1;
            proxy_set_header Upgrade "websocket";
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
        }
    }

## Testing

Connect to [http://wurb1.example.org](http://wurb1.example.org) or
through RaspAP [http://10.3.141.1](http://10.3.141.1)
