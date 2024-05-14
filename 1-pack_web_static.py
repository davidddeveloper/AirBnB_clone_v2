#!/usr/bin/env bash
# a Fabric script that generates a .tgz archive from the contents of the web_static
# using the function do_pack
from fabric.api import local


def do_pack():
    "creating an archive"
    local("mkdir -p versions")
    local('tar -czvf versions/web_static_$(date +"%Y%m%d%H%M%S").tgz web_static')
