#!/usr/bin/python3
""" Generale DOcumentation """
from fabric.api import env, put, run
from pathlib import Path

env.hosts = ['54.89.194.187', '54.157.141.63']

def do_deploy(archive_path):
    """ Documentation """
    file_path = Path(archive_path)
    if not file_path.is_file():
        return False
    try:
    	name = archive_path.split("/").split(".")[0]
    	put(archive_path, "/tmp/")
    	run("tar -xzf {} -C /data/web_static/releases/{}".format(archive_path, name))
    	run("rm /tmp/{}".format(archive_path))
    	run("")
    	run("")
    	run("")
    	return True
    except Exception:
    	return False
    # Step this script should Take :
    #   -> Upload the archive to the /tmp/ 
    #   -> Uncompress to /data/web_static/releases/<archive filename without extension>
    #   -> Delete the archive from the web server
    #   -> Delete the symbolic Link /data/web_static/current
    #   ->  Create new smbolic link to /data/web_static/releases/<archive filename without extension>
