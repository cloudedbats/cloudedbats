# Setup rsync

This is a step-by-step description to be used when setting up a
automatic backup of recorded files from a detector to a server.

Please also check the corresponding document:
[About rsync](./about_rsync.md)

## Prerequisites

The example below is for a WURB detector named "wurb1".
Replace "wurb1", the rsync user "rsync-wurb1" and the corresponding
password "password-for-wurb1" to match your setup.

The server and the wurb are parts of the same network, but it is possible
to access remote servers. The server is named "server1" and can be
accessed by using the address "server1.local".
An external disk is mounted to the server and the files will be stored
in a directory called "/mnt/usb4tb/rec2022/wurb1".

If the server uses a firewall, then TCP port 873 must be open.
If port forward is used, then port 873 must be forwarded to the server.

## Installation

If rsync in not already installed it can be installed
with this install command.

    sudo apt update
    sudo apt upgrade
    sudo apt install rsync

## Configure - server side

The rsync daemon is configured in /etc/rsyncd.conf

    sudo nano /etc/rsyncd.conf

Add the following content:

    motd file = /etc/rsyncd.motd
    log file = /var/log/rsyncd.log
    pid file = /var/run/rsyncd.pid
    lock file = /var/run/rsync.lock

    [wurb1]
    path = /mnt/usb4tb/rec2022/wurb1
    comment = Backup for WURB1.
    uid = pi
    gid = pi
    read only = no
    list = yes
    auth users = rsync-wurb1
    secrets file = /etc/rsyncd.secrets

A file with a valid users and passwords is needed.

    sudo nano /etc/rsyncd.secrets

Add this row for the WURB1 user. Replace the
password for something more secure.

    rsync-wurb1:password-for-wurb1

Then the "/etc/rsyncd.secrets" file should be protected.

    sudo chmod 0640 /etc/rsyncd.secrets

Finally, perform a trial run from the client, the WURB detector.

    rsync -rt --dry-run rsync://rsync-wurb1@server1.local

## Commands

These commands are used to control the rsync daemon running on the
server.

    # Start and stop.
    sudo systemctl start rsync
    sudo systemctl stop rsync

    # Used to activate/deactivate at startup.
    sudo systemctl enable rsync
    sudo systemctl disable rsync

    # Check status.
    sudo systemctl status rsync    

## Client side

Command to run a backup manually.

    rsync -avzP /home/pi/wurb_recordings/* rsync-wurb04@server1.local::wurb04

## Client side, with crontab

Create a specific directory for the rsync parts.

    mkdir /home/pi/backup_rsync
    cd /home/pi/backup_rsync
    nano rsync.secrets

Enter the password "password-for-wurb1" in rsync.secrets.
Then change the access rights for it.

    chmod 600 rsync.secrets

Create a script that should be called from crontab.

    nano /home/pi/backup_rsync/run_rsync.sh

Then enter this content.

    #!/bin/bash

    now=$(date)
    # Check if this script is running.
    if ps ax | grep $0 | grep -v $$ | grep bash | grep -v grep
    then
        echo "$now - Rsync not started, the script is already running."
        exit 1
    fi

    echo "$now - Rsync started."
    rsync -avz --password-file=/home/pi/backup_rsync/rsync.secrets /home/pi/wurb_recordings/* rsync-wurb04@server1.local::wurb04
    now=$(date)
    echo "$now - Rsync finished."
    exit 0

Finally make it possible to execute the script.

    chmod +x /home/pi/backup_rsync/run_rsync.sh 

## Crontab

Edit crontab.

    crontab -e

Add this row at the end to run the script 10 times each hour.

    */10 * * * * /home/pi/backup_rsync/autosync.sh > /home/pi/backup_rsync/backup_log.txt 2>>&1

## Check

This is a way to check whats happening when you are logged in to the 
WURB detector.

    tail -f /home/pi/backup_rsync/backup_log.txt
