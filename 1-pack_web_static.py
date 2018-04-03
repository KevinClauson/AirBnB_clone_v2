#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""
from datetime import datetime
from fabric import operations


def do_pack():
    """creates a .tgz file returns rel path or None """
    time_now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time_now)
    err = ''
    err += operations.local("mkdir -p ./versions")
    err += operations.local("tar -czvf {} ./web_static".format(file_name))
    if err == '':
        return file_name
    return None
