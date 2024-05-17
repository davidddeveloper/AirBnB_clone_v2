""" a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
using the function do_deploy

"""
import os
from fab.api import local, put, run

env.hosts = [54.144.251.105, 54.90.53.190]
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

    if not os.exists(archive_path):
        return False

    put(f"{archive_path} /tmp/")

    archive_name = archive_path.split("/")[1]
    archive_name = archive_name.split(".")[0]

    uncompress_dir = "/data/web_static/releases/"
    run(f"sudo mkdir -p {uncompress_dir}/{archive_name}")
    run(
        f"sudo tar -xzf /tmp/{archive_name}.tgz -C {uncompress_dir}/{archive_name}"
    )

    run(f"sudo rm -rf /tmp/{archive_path}")
    run("sudo rm -r /data/web_static/current")

    spread = f"/{uncompress_dir}/{archive_name} /data/web_static/current"
    run(
        "sudo ln -f -s {spread}"
    )

    return True
