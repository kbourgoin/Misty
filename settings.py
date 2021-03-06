#!/usr/bin/env python
# Copyright (C) 2011 Michael Ranieri <michael.d.ranieri at gmail.com>

# This file has the settings for Misty Bot.
# Duplicate this file and rename it as settings_local.py with your changed settings.
# DATABASE must be postgreSQL due to asynchronous calls and the use of pyPgSQL library

# Name of database
DATABASE_NAME = "Misty"

# user who owns database
DATABASE_USER = "postgres"

# password to access database
DATABASE_PASSWORD = "some_password"

# URL to access database at
DATABASE_URL = "localhost:5432"

# nickname for Misty in IRC
NICKNAME = "Misty"

# IRC server to connect to
SERVER = "irc.someserver.com"

# Port to connect through
PORT = 6667

# Password for IRC Server
PASSWORD = "some_irc_password"

# Channel to join once connected
CHANNEL = "#somechannel"

# Path to isles folder (absolute)
PATH_TO_ISLES = "/Users/SomeUser/Misty/isles/"