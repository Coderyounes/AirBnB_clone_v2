#!/usr/bin/python3

from invoke import task

@task
def test_fabric(c):
    print("Fabric is working!")


