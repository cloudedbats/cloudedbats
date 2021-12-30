# Read only user

## SFTP read-only user

If a detector is connected to internet and set up as an SFTP server, then it is nice to have the possibility to share the recorded files with others in a safe manner. This instruction describes how to configure a user that only can access some specific directories and only via SFTP. 

The same procedure can be followed to share files from a server.

The main steps to do this are:
- Create a user who can't log in via SSH, only via SFTP.
- Use "chroot" to restrict that users access to files in the system.
- Mount some external dictionaries in that users home directory. This is the only way to give access to files to a user that is "jailed" by "chroot".
- Set up the SFTP server to connect to "chroot" for that user, or the group the user belongs to.

There are two directories in the detector that are useful for the read-only user:
- /home/pi/wurb_recordings
- /home/pi/wurb_logging

### How to connect

Use an SFTP client, for example FileZilla. Connect with:
- Protocol: SFTP
- Host: "IP-address-or-domain/subdomain-name"
- Port: "the-port-that-is-externally-used-for-ssh-and-sftp"
- User: wurb-read
- Password: "password-for-wurb-read"

### Installation

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

Edit /etc/fstab:

    # Add those lines.
    /home/pi/wurb_recordings /home/chroot/wurb-read/wurb_recordings none bind,ro
    /home/pi/wurb_logging /home/chroot/wurb-read/wurb_logging none bind,ro

Create and mount directories for the user.

    sudo mkdir /home/chroot/wurb-read/wurb_recordings
    sudo mkdir /home/chroot/wurb-read/wurb_logging
    sudo mount /home/chroot/wurb-read/wurb_recordings
    sudo mount /home/chroot/wurb-read/wurb_logging

Edit /etc/ssh/sshd_config:

    # Search for and replace the "Subsystem sftp ..." line with this line:
    Subsystem     sftp   internal-sftp
    
    # Connect the users call to "chroot" by adding this.
    Match Group sftp-read
        ChrootDirectory /home/chroot
 	    X11Forwarding no
 	    AllowTCPForwarding no
 	    ForceCommand internal-sftp

Restart the service and test it by connecting from an SFTP client.

    sudo service ssh restart

