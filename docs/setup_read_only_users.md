# Setup a read-only-user

This is a step-by-step description to be used when setting up a
safe read-only user for SFTP use.

Please also check the corresponding document:
[About read-only-users](docs/about_read-only-users.md)

## Prerequisites

A WURB detector that has recorded sound files without an USB memory
stick attached. Then there will be two directories available:
- /home/pi/wurb_recordings
- /home/pi/wurb_logging

## Installation

Log in to either the WURB detector or the backup server depending
on what you want to share. The example below is for a WURB detector.

Add a group for read-only users.

    sudo groupadd sftp-read

Create a user that is only allowed to work inside /home/chroot via SFTP.

    sudo mkdir -p /home/chroot/wurb-read
    sudo useradd -d /wurb-read -s /bin/false -G sftp-read wurb-read
    sudo passwd wurb-read

Permissions and ownership.

    sudo chmod 711 /home/chroot
    sudo chmod 555 /home/chroot/wurb-read
    sudo chown wurb-read:sftp-read /home/chroot/wurb-read

Then edit /etc/fstab:

    sudo nano /etc/fstab
    # Add those lines.
    /home/pi/wurb_recordings /home/chroot/wurb-read/wurb_recordings none bind,ro
    /home/pi/wurb_logging /home/chroot/wurb-read/wurb_logging none bind,ro

Create and mount directories for the user.

    sudo mkdir /home/chroot/wurb-read/wurb_recordings
    sudo mkdir /home/chroot/wurb-read/wurb_logging
    sudo mount /home/chroot/wurb-read/wurb_recordings
    sudo mount /home/chroot/wurb-read/wurb_logging

Edit /etc/ssh/sshd_config:

    sudo nano /etc/ssh/sshd_config
    # Search for and replace the "Subsystem sftp ..." line with this line:
    Subsystem     sftp   internal-sftp
    
    # Connect the users call to "chroot" by adding this.
    Match Group sftp-read
        ChrootDirectory /home/chroot
        X11Forwarding no
        AllowTCPForwarding no
        ForceCommand internal-sftp

Restart the service.

    sudo service ssh restart

## Test it

Test it by connecting from an SFTP client like FileZilla or WinSCP.

- Protocol: SFTP
- Host: wurb1.example.org # Or IP address.
- Port: 22 # Or the externally used port before port forwarding.
- User: wurb-read
- Password: wurb-read
