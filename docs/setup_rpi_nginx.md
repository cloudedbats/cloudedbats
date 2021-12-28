# Nginx

## Install software packages

    sudo apt update
    sudo apt upgrade
    sudo apt install nginx
    sudo apt install apache2-utils

## Useful commands

    # Start and stop.
    sudo systemctl start nginx
    sudo systemctl stop nginx
    # Gracefully and forced restart.
    sudo systemctl reload nginx
    sudo systemctl restart nginx
    # Launch on boot.
    sudo systemctl enable nginx
    sudo systemctl disable nginx
    # Check.
    sudo systemctl status nginx

## Username/password

    sudo htpasswd -c /etc/nginx/.htpasswd arnold
    # # Next time when .htpasswd is created.
    # sudo htpasswd /etc/nginx/.htpasswd another_user

## Basic Nginx config

Edit the Nginx configuration file.

    sudo nano /etc/nginx/nginx.conf

Uncomment these lines in "/etc/nginx/nginx.conf":

    server_names_hash_bucket_size 64;
    server_name_in_redirect off;

Remove the link to the default configuration.

    sudo rm /etc/nginx/sites-enabled/default

## Example

This is an example with one web page and one public 
WURB detector connected to the local network.

Two sub domains are set up to point to the public and 
static IP address for the network. 
Both port 80 and 22 is then routed by using 
"port forwarding" to the Raspberry Pi computer in the 
local network.

Sub domains for the example are:

- server1.cloudedbats.org
- wurb04.cloudedbats.org

Password for the detector should be defined.

        sudo htpasswd -c /etc/nginx/.htpasswd arnold

### Example web site

Download an example website. In this case we use the
https://cloudedbats.github.io web page.

    sudo apt install git
    git clone https://github.com/cloudedbats/cloudedbats.github.io.git

### Create the Nginx configuration file

Edit the configuratione file.

    sudo nano /etc/nginx/sites-enabled/cloudedbats_server1.conf

Add these rows, and modify them to fit your needs:

    # The servers web page.
    upstream server1 {
        server localhost:8081;
    }
    # WURB detector.
    upstream wurb04 {
        # Connected to the local network.
        server wurb04.local:8000;
    }

    # Public call to web page.
    server {
        listen 80;
        server_name server1.cloudedbats.org;

        location / {
            proxy_pass http://server1/;
            proxy_set_header Host $host;
        }
    }
    # Internal call to web page.
    server {
        listen 8081;
        server_name localhost;

        location / {
            root /home/pi/cloudedbats.github.io;
        }
    }

    # Public call to WURB detector, password protected.
    server {
        listen 80;
        server_name wurb04.cloudedbats.org;

        # WURB detector.
        location / {
            proxy_pass http://wurb04/;
            proxy_set_header Host $host;
            # Login needed.
            auth_basic "Restricted Content";
            auth_basic_user_file /etc/nginx/.htpasswd;
        }
        # WebSocket communication.
        location /ws {
            proxy_pass http://wurb04/ws;
            proxy_http_version 1.1;
            proxy_set_header Upgrade "websocket";
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
        }
    }

    # Disable other subdomains linked to this server.
    server {
        listen 80;
        server_name wurb.cloudedbats.org 
                    wurb01.cloudedbats.org 
                    wurb02.cloudedbats.org 
                    wurb03.cloudedbats.org;

        location / {
            return 444;
        }
    }

### Testing

Connect to http://server1.cloudedbats.org and 
"http://wurb04.cloudedbats.org" to checkif it 
works as expected.
