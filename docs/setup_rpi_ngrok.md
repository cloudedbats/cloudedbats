## External access by using ngrok

The CloudedBats-WURB detector is developed as a Linux based web server. In the basic setup the detector is accessed over the detectors WiFi network and is then protected by a password for that WiFi network. If the detector should be opened for external access, then it must be connected to a network with a public IP address. That IP address can either be static or dynamic.

But many mobile 4G networks uses something called Carrier Grade NAT, CGNat, and they can't provide public IP addresses. One solution to this is to establish a connection from the detector, via communication tunnels, to a place where there are public IP addresses.

Ngrok is a company working with this kind of solutions. Ngrok have servers that the detector can connect to, and their client software must be installed and configured on each detector. For temporary use it can be free to use ngroks servers, but if we want to share our data more permanently, then we must use the paid alternatives.

When installed this solution is very easy to use. As soon as the detector is connected to internet, in any way, it tries to establish a connection to the ngrok servers. And as soon that connection is established, we can communicate with the detector from any computer or mobile device connected to internet, and we can run multiple tunnels simultaneously for HTTP/HTTPS and SSH/SFTP for each detector.

### Installation in summary 
Everything needed to connect a detector to the ngrok server will be placed in a directory called "/home/pi/ngrok". That includes the ngrok client software, the configuration file, a startup script and the log files. Then we need to call the startup script from /etc/rc.local to launch the ngrok client software each time the detector is started.

### First step
To connect the detector to ngrok you must have an account registered on "ngrok.com". There are both free and paid plans. When you have signed up you will get your personal token for authentication, the Authtoken. When logged in there is a Dashbord available at https://dashboard.ngrok.com/ that contains information about current status for connected tunnels.

### Second step
The software should be installed on the detector. To do this the detector must be connected to internet and a terminal session should be started. Download and install the ngrok client software, the Linux(ARM) version. You have to copy the correct link for the zip file instead of the one in the example below. 

    mkdir ngrok
    cd ngrok
    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
    unzip ngrok-stable-linux-arm.zip

    sudo nano /etc/rc.local

    # Add this line to rc.local before the "exit" row:
    sudo -u pi bash /home/pi/ngrok/ngrok_start.sh &

    nano ngrok_start.sh

    # Add this line to ngrok_start.sh:
    /home/pi/ngrok/ngrok start -config /home/pi/ngrok/ngrok.yml wurb ssh &

    nano ngrok.yml

    # Add this content to ngrok.yml (to be used as a template, as least xxxx should be replaced):
    
    authtoken: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    region: eu
    console_ui: false
    log: /home/pi/ngrok/ngrok.log
    tunnels:
      wurb:
        proto: http
        addr: 8000
        auth: xx:xx
        # hostname: wurb-1.example.org
        # addr: 127.0.0.1:8000
        inspect: false
      ssh:
        proto: tcp
        addr: 22
        # remote_addr: x.tcp.eu.ngrok.io:xxxxxx


### Third step

Restart the detector.

Go to the dashboard at https://dashboard.ngrok.com/ and check "Endpoints - Status". 

Then go to "Endpoints - Domains" and create a domain. Follow the instructions until you get something to setup in the CNAME field that is used to point from the subdomain "wurb-1.example.org" in the example above.

Do the same at "Endpoints - TCP addresses". This will not end up in a customised subdomain, only a ngrok subdomain with a static port number.

### Fourth step

Log in to your domain provider and create a subdomain "wurb-1" for the "example.com" domain. Use the CNAME value from the earlier step to point to the tunnel endpoint at ngrok.

### Fifth step

Log in to the detector and remove the commented lines in the configuration file "ngrok.yml". Then restart the detector.

### Usage example 1, TCP

URL: tcp://x.tcp.eu.ngrok.io:xxxxx

This can be used for SSH:

    ssh pi@x.tcp.eu.ngrok.io -p xxxxx

or for SFTP:

    protocol: SFTP
    host: x.tcp.eu.ngrok.io
    port: xxxxx
    user: pi
    password: xxxxxxxx

### Usage example 2, HTML

Just use the web address http://wurb-1.example.org to access the detectors web interface. 

### Notes about the config file

If the row "auth: xx:xx" in the config file is uncommented, then there will be a login page before the web page is available. 

The "subdomain" and remote_addr" rows in the configuration file are used for payed plans where the subdomains are not randomly generated each time the ngrok client is started. 
If you are using the free plan, then the web address https://xxxxxxxxx.eu.ngrok.io can be used to access the detectors web user interface. The web address will change after each restart of the ngrok client but can be found in the log file in the detector and on the ngrok dashboard when logged in to their web page.
