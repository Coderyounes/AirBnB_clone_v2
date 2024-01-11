#!/usr/bin/python3

from fabric.api import task, local
from pack_web_static import do_pack

@task
def pack():
    result = do_pack()
    if result:
        print(f"Archive created successfully: {result}")
    else:
        print("Failed to create archive.")


