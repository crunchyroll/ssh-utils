SSH utilities for managing SSH agent sessions.

`make rpm` to build RPM.

Motivation
==========
One uses SSH key pairs to log into various servers.  All of us will have
a personal key, and many of us also have shared keys for various
resources.  Best practice is to protect keys with a password.  But
should you be re-entering your password each time you need to use the
key?  No!  Use SSH Agent.

The main idea is that you start an SSH Agent daemon on the host using
the command `ssh-agent`.  You will then add private keys to the agent
daemon with the `ssh-add` command.  You enter your password once per key
per agent lifetime, and the agent keeps the decrypted key in memory,
making it usable to `ssh` via a socket (which is itself protected with
Unix user permissions).  `ssh` knows to use the SSH authentication
socket by looking for the `SSH_AUTH_SOCK` environment variable.

Mac OS X
--------
If you are on a Mac, this is mostly handled for you, although there are
still some potential use cases that might call for these utilities.
`SSH_AUTH_SOCK` is set automatically when you launch a new
`Terminal.app` window, but it’s not automatically made available in the
following two cases.

- When Cron jobs are executed.
- When you ssh into your Mac.

So you may not need to think about this if you're using a Mac.

Usage
=====
Add the following line to your bash profile, zshenv, etc.

    eval `ssh-reconnect-agent-session`

Run `ssh-init-agent-session` interactively once every time the host is
rebooted, and then don’t worry about it otherwise.  You can just log in
and then passwordless-ly log in to other hosts.  Note that
`ssh-reconnect-agent-session` is noisy on failure--it prints to standard
error and exits uncleanly.  This way, if you have other automated
scripts that log into a host and depend on the agent session, they will
themselves fail noisily if the agent session reconnection fails.

Utilities
=========

- `ssh-check-private-keys`

  Find private keys in user's home `.ssh` directory.  Besides the
  default key names used by ssh-add, also look for keys ending in
  `_ssh_key`.  For keys that are found, ensure they are encrypted.  If
  any are not encrypted, print message to standard error and exit with
  status 1.  Otherwise, print paths to standard out on a single line.
  (Ideal for passing as arguments to `ssh-add`.)  If relevant
  directories or keys are not found, print message to standard error and
  exit with status 127.

- `ssh-find-auth-sock`

  Find SSH authorization socket for `$USER` and print its path to
  standard out.  If not found, return exit status 1.

- `ssh-init-agent-session`

  Start and connect to ssh-agent and add user's private keys found by
  `ssh-check-private-keys`.

- `ssh-reconnect-agent-session`

  Look for existing `ssh-agent` session.  If found, print to standard
  out shell command for setting environment variable to reconnect to the
  found session.  Else, print message to standard error and exit with
  status 1.
