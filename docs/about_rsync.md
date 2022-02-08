# About rsync

Rsync is a tool that can be used to synchronize directories and files
between computers.

When running WURB bat detectors rsync can be used to backup recorded
files to a server in near-real-time, and the files can then be checked
immediately from that server. They can also be shared if the server is
publicly available.

## Client and server setup

In this installation rsync is running in daemon mode on the server.
The main reason is because in daemon mode rsync does not have to rebuild
the lists that are used for an effective synchronization for each access 
from a client.

On the client side, the WURB detector in this case, the backup is
initiated as a crontab job an runs based on what is specified there.

## Next step

There is a step-by-step description here:
[Setup rsync](docs/setup_rsync.md)
