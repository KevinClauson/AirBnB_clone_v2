#!/usr/bin/python3
'''
Deploy archive
'''
import os
from fabric.operations import put
from fabric.api import env, run, hosts


env.hosts = ['54.175.3.213', '34.228.64.127']


def do_deploy(archive_path):
    ''' deploy to web servers 
    '''
    if not os.path.isfile(archive_path):
        return False
    archive_name = archive_path.split("/")[1]
    remote_name = '/tmp/' + archive_name
    upload = put(archive_path, remote_name)
    if upload.failed:
        return False
    archive_dir = archive_name.split(".")[0]
    run('mkdir -p /data/web_static/releases/{}/'.format(archive_dir))


    r = run('tar -xzf {} -C /data/web_static/releases/{}/'.format(remote_name, archive_dir))
    if r.failed:
        return False
    r = run('rm {}'.format(remote_name))
    if r.failed:
        return False
    run("cp -rp /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(archive_name, archive_name))
    run('rm -rf /data/web_static/releases/{}/web_static/'.format(archive_name))
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(archive_name))
    return True
