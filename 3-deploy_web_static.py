#!/usr/bin/python3                                                                                                                                                      
"""                                                                                                                                                                     
Deploys tgz file to web servers                                                                                 
"""
import os
from datetime import datetime
from fabric import operations
from fabric.api import env, run, hosts


env.hosts = ['54.175.3.213', '34.228.64.127']


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



def do_deploy(archive_path):
    """puts tgx archive ont o webservers"""
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.split('/')[-1]
    archive_dir = archive_name.replace('.tgz', '')
    remote_path = '/tmp/' + archive_name
    if operations.put(archive_path, remote_path).failed:
        return False
    run('mkdir -p /data/web_static/releases/{}/'.format(archive_dir))
    run('tar -xzf {} -C /data/web_static/releases/{}/'.
        format(remote_path, archive_dir))
    run('rm {}'.format(remote_path))
    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}/'.
        format(archive_dir, archive_dir))
    run('rm -rf /data/web_static/releases/{}/web_static/'.format(archive_dir))
    run('rm -rf /data/web_static/current')
    run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.
        format(archive_dir))
    return True


def deploy():
    '''
    set up full deployment
    '''
    path = do_pack()
    if path is None:
        return False
    value = do_deploy(path)
    return value
