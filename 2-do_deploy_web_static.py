#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
using the function do_deploy

"""
import os
from fabric.api import env, local, put, run

env.hosts = ["35.153.17.38", "54.90.53.190"]
env.user = "ubuntu"


def do_pack():
    "create a compressed archive from web_static directory"
    local("mkdir -p versions")
    local(
        'tar -czvf versions/web_static_$(date +"%Y%m%d%H%M%S").tgz web_static'
    )


def do_deploy(archive_path):
    """
        Upload the archive to the /tmp/ directory
        And uncompress the archive

        Args:
            - archive_path - path to the archive

        Returns:
            False if the file at the path archive_path doesn’t exist

    """

    if not os.path.exists(archive_path):
        return False

    put(f"{archive_path}", "/tmp/")

    archive_name = archive_path.split("/")[1]
    archive_name = archive_name.split(".")[0]
    print(archive_name)

    uncompress_dir = "/data/web_static/releases/"
    run(f"sudo mkdir -p {uncompress_dir}/{archive_name}")

    destination = f"{uncompress_dir}/{archive_name}"
    run(
        f"sudo tar -xzf /tmp/{archive_name}.tgz -C {destination}"
    )

    run(f"sudo rm /tmp/{archive_name}.tgz")

    source = f"{uncompress_dir}/{archive_name}/web_static/*"
    destination = f"{uncompress_dir}{archive_name}"
    run(f"sudo mv {source} {destination}")
    run(
        f"sudo rm -rf {uncompress_dir}{archive_name}/web_static"
    )
    run("sudo rm -rf /data/web_static/current")

    source = f"{uncompress_dir}/{archive_name}"
    destination = f"/data/web_static/current"
    run(
        f"sudo ln -s {source} {destination}"
    )

    return True
