#!/usr/bin/env bash
"""
script that generates a .tgz archive from the contents 
"""
from fabric.api import *
from datetime import datetime

def do_pack():
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%m%s")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    
    if result.succeeded:
        return filename
    else:
        return None
