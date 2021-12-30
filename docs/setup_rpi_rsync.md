# Rsync

Rsync is a tool that can be used to synchronise directories and files 
between computers.

When running WURB bat detectors rsync can be used to backup recorded 
files to a server in near-real-time, and the files can then be checked 
immediately from that server. They can also be shared if the server is 
publicly available. 

In this installation rsync is running in daemon mode on the server. 
The main reason is because in daemon mode rsync does not have to rebuild
the lists that are used for an effective syncronisation.

On the client side, the WURB detector in this case, the backup is 
initiated as a crontab job an runs based on what is specified there.

The example below is for a WURB detector named "wurb04". 
Replace "wurb04", the rsync user "rsync-wurb04" and the corresponding 
password "password-for-wurb04" to match your setup.
The server and the wurb are parts of the same network, but it is possible 
to access remote servers. The server is named "server1" and can be 
accessed by using the address "server1.local".
An external disk is mounted to the server and the files will be stored 
in a directory called "/mnt/usb4tb/rec2021/wurb04".

If the server uses a firewall, then TCP port 873 must be open.

## Installation

If rsync in not already installed it can be installed 
with this command.

    sudo apt install rsync

## Configure - server side

The rsync daemon is configured in /etc/rsyncd.conf

    sudo nano /etc/rsyncd.conf

Add the following content:

    motd file = /etc/rsyncd.motd
    log file = /var/log/rsyncd.log
    pid file = /var/run/rsyncd.pid
    lock file = /var/run/rsync.lock

    [wurb04]
    path = /mnt/usb4tb/rec2021/wurb04
    comment = Backup for WURB04.
    uid = pi
    gid = pi
    read only = no
    list = yes
    auth users = rsync-wurb04
    secrets file = /etc/rsyncd.secrets

A file with valid users and passwords is needed.

    sudo nano /etc/rsyncd.secrets

Add this row for the WURB04 user.

    rsync-wurb04:password-for-wurb04

Then the "/etc/rsyncd.secrets" file should be protected.

    sudo chmod 0640 /etc/rsyncd.secrets

Finally, perform a trial run.

    rsync -rt --dry-run rsync://rsync-wurb04@server1.local

## Commands

These commands are used to control the rsync daemon.

    # Start and stop.
    sudo systemctl start rsync
    sudo systemctl stop rsync
    # Check status.
    sudo systemctl status rsync
    # Used to activate/deactivate at startup.
    sudo systemctl enable rsync
    sudo systemctl disable rsync

## Client side

Command to run a backup manually.

    rsync -avzP /home/pi/wurb_recordings/* rsync-wurb04@server1.local::wurb04

## Client side, with crontab

Create a specific directory for the rsync parts.

    mkdir /home/pi/backup_rsync
    cd /home/pi/backup_rsync
    nano rsync.secrets

Enter the password "password-for-wurb04" in rsync.secrets.
Then change the access rights for it.

    chmod 600 rsync.secrets

Create a script that should be called from crontab.

    nano /home/pi/backup_rsync/run_rsync.sh

And enter this content.

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

Then make it possible to execute the script.

    chmod +x /home/pi/backup_rsync/run_rsync.sh 

## Crontab

Edit crontab.

    crontab -e

Add this row at the end to run the script 10 times each hour.

    */10 * * * * /home/pi/backup_rsync/autosync.sh > /home/pi/backup_rsync/backup_log.txt 2>>&1

## Check

This is a way to check whats happening.

    tail -f /home/pi/backup_rsync/backup_log.txt
