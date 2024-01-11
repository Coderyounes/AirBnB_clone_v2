#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
from os import makedirs, path

def do_pack():
    try:
        if not path.exists('/web_static/versions'):
            makedirs('/web_static/versions')
        
        date = datetime.now()
        formatting = date.strftime("%Y%m%d%H%M%S")
        archive_path = "web_static/versions/web_static_{}.tgz".format(formatting)

        tar_result = local("tar -cvzf {} web_static/".format(archive_path))

        if tar_result.failed:
            return None
        else:
            return archive_path
    except:
        return None
