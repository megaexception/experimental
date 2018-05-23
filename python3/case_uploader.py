#!/usr/bin/env python3
# -*- coding: utf-8 *-
"""
upload directory to sftp.juniper.net
"""
import os
import re
import sys

import paramiko.client

# credentials for secure upload
SERVER = {
    "hostname": "sftp.juniper.net",
    "port": 22,
    "username": "anonymous",
    "password": "anonymous"
}

# Read cmdline parameters, and find files, case.
if not sys.argv:
    raise Exception("No directory specified!")

local_dir = os.path.expanduser(sys.argv[1])
if not os.path.exists(local_dir):
    raise Exception(f"Error: {local_dir} is not a directory to be uploaded on secure upload!!")

case_name = os.path.basename(local_dir)
if not re.search("^[0-9]{4}-[0-9]{4}-[0-9]{4}$", case_name):
    raise Exception(f"Directory name '{case_name}'is not Juniper case name!")

files_to_transfer = os.listdir(local_dir)
if not files_to_transfer:
    raise Exception(f"No files to transfer via secure upload in {local_dir}")

client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
client.connect(**SERVER)

sftp = client.open_sftp()
try:
    sftp.mkdir(f"/pub/incoming/{case_name}")
    sftp.chdir(f"/pub/incoming/{case_name}")
except Exception as e:
    print(f"error creating directory {case_name}: {e}!!!")

for filename in files_to_transfer:
    print(f"sftp.copy {filename} to {case_name}")
    sftp.put(f"{local_dir}/{filename}", f"/pub/incoming/{case_name}/{filename}")
