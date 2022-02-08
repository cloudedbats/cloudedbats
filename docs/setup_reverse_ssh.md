# Setup reverse ssh

This is a step-by-step description to be used when connecting
a remote computer to establish a reverse ssh tunnel.

Please also check the corresponding document:
[About reverse ssh](docs/about_reverse_ssh.md)

# Create a user on the server

Log in to the server and create a new user.
This user should not have sudo/root privileges.

    sudo adduser reverse-ssh-user

If login via normal passwords is disabled, then enable that
temporarily.

Move over to the detector.
Copy the public key from the detector to the server

    # Create an ssh key pair, if it is not done earlier.
    ssh-keygen

    # And then copy the public key to the server.
    # Use the user account without sudo/root privileges.
    ssh-copy-id reverse-ssh-user@server1.example.org

Now you can disable normal password login again.

## Set up the service

To make the connection from the detector to the server always
available it is recommended to run it as a service.

    sudo nano /etc/systemd/system/wurb_reverse_ssh.service 

    # Add the following to wurb_reverse_ssh.service.

    [Unit]
    Description=Reverse ssh to server1.example.org 
    After=network.target

    [Service]
    Restart=always
    RestartSec=30
    User=pi
    ExecStart=/bin/ssh \
        -NT \
        -o ServerAliveInterval=60 \
        -o ServerAliveCountMax=10 \
        -o ExitOnForwardFailure=yes \
        -R 51022:localhost:22 \
        -R 51080:localhost:80 \
        -R 51443:localhost:442 \
        # Special user without sudo permissions.
        reverse-ssh-user@server1.example.org

    [Install]
    WantedBy=multi-user.target

If more than one detector is connected to the same server, then the
ports 51022, 51080 and 51443 must have other numbers.

Then reload and enable the service.

    sudo systemctl daemon-reload
    sudo systemctl enable wurb_reverse_ssh.service

## Useful commands

    sudo systemctl daemon-reload

    sudo systemctl start wurb_reverse_ssh.service
    sudo systemctl stop wurb_reverse_ssh.service
    
    sudo systemctl enable wurb_reverse_ssh.service
    sudo systemctl disable wurb_reverse_ssh.service

    sudo systemctl status wurb_reverse_ssh.service

## Test, login from server

    ssh -l pi -p 51022 localhost
