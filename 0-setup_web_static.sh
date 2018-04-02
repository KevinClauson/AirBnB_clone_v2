#!/usr/bin/env bash
# sets up your web servers: install Nginx creates folters
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<p>Hello World<p>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sed -i "38i\ \tlocation \/hbnb_static {\\n\\t\\talias \/data\/web_static\/current\/;\\n\\t}" \ 
    /etc/nginx/sites-available/default
service nginx restart
