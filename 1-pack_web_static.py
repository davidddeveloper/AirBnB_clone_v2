#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static directory
using the function do_pack

"""

from fabric.api import local


def do_pack():
    "create a compressed archive from web_static directory"
    local("mkdir -p versions")
    local(
        'tar -czvf versions/web_static_$(date +"%Y%m%d%H%M%S").tgz web_static'
    )
