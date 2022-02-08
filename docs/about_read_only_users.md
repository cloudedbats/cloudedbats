# About read-only-users

If a detector is connected to internet and set up as an SFTP server, then it
 is good to have the possibility to share the recorded files with others in
 a safe manner. This instruction describes how to configure a user that only
 have read access to some specific directories and only access over SFTP.

## Installation in summary

- Create a user who can't log in via SSH, only via SFTP.
- Use "chroot" to restrict that users access to files in the system.
- Mount some external dictionaries in that users home directory. This is the
only way to give access to files to a user that is "jailed" by "chroot".
- Set up the SFTP server to connect to "chroot" for that user, or the group
the user belongs to.

There are two directories in a WURB detector that are useful for the read-only user:

- /home/pi/wurb_recordings
- /home/pi/wurb_logging

For a central backup server some folders on an external drive can be shared
in the same way.

## How to connect, example

Use an SFTP client, for example FileZilla or WinSCP. Connect with:

- Protocol: SFTP
- Host: wurb1.example.org
- Port: 22
- User: wurb-read
- Password: wurb-read

The host can be replaced with an IP number if DNS is not used.

## Next step

There is a step-by-step description here:
[Setup read-only-users](./setup_read_only_users.md)
