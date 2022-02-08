# About ngrok

[Ngrok](http://ngrok.com) is a company that makes it possible to connect to
computers that are not set up as ordinary servers with public IP addresses.

It works for computers running behind firewalls, for computers inside local
networks, for computers connected to internet via public Wifi networks, and
for connections over 4G/LTE modems where public IP addresses not is an option
since they operates inside a Carrier Grade NAT, CGNat, where the used
IP addresses are not unique.

Ngrok uses a tunneling technique and each unit that is using ngroks services
must be connected to one of their servers.
Then ngrok provides public IP addresses. There is a free plan where the IP
addresses changes at each startup of the computer, and for stable IP addresses
you have to pay, but then you can connect domain/subdomain names to them.

## Alternatives

- If you are running your own server with a public IP address, then you can
set up a similar functionality yourself. It will work both for normal physical
servers and for virtual servers running in the cloud.
Descriptions can be found here: [About reverse_ssh](docs/about_reverse_ssh.md)
and here [Setup reverse_ssh](docs/setup_reverse_ssh.md).

- Some internet providers offers a similar functionality for their customers, sometimes without an extra fee.

## Account at ngrok

To connect the detector to ngrok you must have an account registered at
[Ngrok](http://ngrok.com). It free for one unit.
When you have signed up you will get your personal token for authentication,
the "Authtoken".
When logged in there is a Dashbord available at
[ngroks dashboard](https://dashboard.ngrok.com/).
That dashboard contains information about current status for connected tunnels
and the links to access them.

## Installation in summary

Everything needed to connect a detector/server to the ngrok server will be placed
in a directory called "/home/pi/ngrok". That includes the ngrok client software,
the configuration file, a startup script and the log files.
Then we need to call the startup script from /etc/rc.local to launch the ngrok
client software each time the detector/server is started.

## Next step

There is a step-by-step description here:
[Setup ngrok](docs/setup_ngrok.md)
