# About reverse ssh

Reverse ssh can be used to access computers that are not made public
in the same was as a servers with an public IP address.

It works for computers running behind firewalls, for computers inside local
networks, for computers connected to internet via public Wifi networks, and
for connections over 4G/LTE modems where public IP addresses not is an option
since they operates inside a Carrier Grade NAT, CGNat, where the used
IP addresses are not unique.

Reverse ssh is a tunneling technique where the initiative must come from the
remote end, not from the server end. The client makes a "call back home" to
the server and establish an ssh tunnel that the server can use to call back to
the client. Both ways should be user/password protected, preferably by the use
of ssh keys.

## Alternatives

- **Ngrok** have a commercial implementation of it without the need for your
to have your own server.
More about it here: [About reverse_ssh](./about_reverse_ssh.md)
and here [Setup reverse_ssh](./setup_reverse_ssh.md).

## Next step

There is a step-by-step description here:
[Setup reverse ssh](./setup_reverse_ssh.md)
