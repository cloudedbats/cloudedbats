# Setup Raspberry Pi security

This is a step-by-step description to be used when setting up a
Raspberry Pi based detector, or server, that is exposed for incoming
calls from the internet.

Please also check the corresponding document:
[About Raspberry Pi security](docs/about_security.md)

## Prerequisites

You need a Raspberry Pi computer with the latest version of
the Raspberry Pi OS Lite installed. The "Lite" version is the
one without the Desktop parts installed.

It should be setup with SSH enabled. All commands below are done
through a terminal window.

**Hint**: When using the Raspberry Pi Imager there is a hidden
command "ctrl + shift + X" that makes it easier to name the device,
to activate SSH, and also to configure for WiFi access.

From here on we assume that there is a detector named "wurb1" connected
to the local network.

## The pi user account

Change the password to a longer and more secure one.

    # Log in as pi. 
    ssh pi@wurb1.local

    # Run the command
    passwd

    # Logout from the Raspberry Pi to continue with the SSH keys.
    exit

Generate SSH keys. This is valid for Linux and macOS, may differ on Windows.
The "ssh-keygen" will ask for a password. You can just press return to skip that
password, or type in a short one, or a longer one that you store in some kind
of keychain on your client computer.

    # Generate both keys to the computer you want to log in from:
    ssh-keygen

    # Check the keys: id_rsa (private) and id_rsa.pub (public).
    # Important: Don't share the private key, keep it tight.
    ls ~/.ssh
    cat ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub

Send the public key to the detector.

    ssh-copy-id pi@wwurb1.localhost

    # Then login to the Raspberry Pi detector for test. 
    # You may enter the ssh-key password.
    ssh pi@wurb1.local

    # Check if your public key is in the list of authorized keys.
    cat ~/.ssh/authorized_keys

Disable password login. This is an extra level of security to avoid SSH
login from not registered clients. 

    # Log in to the Raspberry Pi detector. Edit this file.
    sudo nano /etc/ssh/sshd_config

    # Modify the "PasswordAuthentication" row. It should be:
    PasswordAuthentication no

## Update and upgrade

This is about how to always keep the operating system packages up-to-date.

    # Run this first, as always before the installation of packages.
    sudo apt update
    sudo apt upgrade

    # Install and configure. Answer yes to the question during configuration.
    sudo apt install unattended-upgrades
    sudo dpkg-reconfigure --priority=low unattended-upgrades

## Firewall, the UncomplicatedFirewall (UFW)

The firewall is here used to restrict incoming access to only the used ports.

**Warning**: If UFW is activated and port 22 is not allowed, then is
is impossible to continue with access over ssh.
It that happens the only way is to use an HDMI-monitor and a keyboard
connected to the Raspberry Pi to fix the error, or reinstall from scratch.

    # Install the package.
    sudo apt install ufw

    # Allow ports. Select the ones you are planning to use.
    sudo ufw allow 22 # For SSH.
    sudo ufw allow 80 # For HTTP.
    sudo ufw allow 443 # For HTTPS.
    sudo ufw allow 873 # For Rsync.

    # Example of a more reduced strategy.
    # sudo ufw allow from 192.168.1.100 port 22

    # Enable/disable UFW. Enable means directly, as well as
    # after next reboot or restart.
    sudo ufw enable
    sudo ufw disable

    # Useful commands to check status.
    sudo ufw show added
    sudo ufw status verbose
