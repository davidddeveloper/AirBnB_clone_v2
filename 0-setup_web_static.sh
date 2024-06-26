#!/usr/bin/env bash
# install nginx and configures it to serve web static content

# Instal nginx
sudo apt-get update
sudo apt-get -y install nginx

# directories and files creation
file="/data/web_static/releases/test/index.html"
file_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
# sudo mkdir -p /data/web_static/current
echo "$file_html" | sudo tee "$file" > /dev/null
# echo "$file_html" | sudo tee "/data/web_static/current/index.html" > /dev/null

# create a symbolic link (current --> test)
sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current

# change ownership of data
sudo chown -R ubuntu:ubuntu /data/

# configure nginx
config_file="/etc/nginx/sites-available/default"
echo "" | sudo tee "$config_file" > /dev/null
config_block="server {
        location /hbnb_static {
                alias /data/web_static/current/;
        }
}"
echo "$config_block" | sudo tee "$config_file" > /dev/null

# start nginx
sudo service nginx stop
sudo service nginx start
