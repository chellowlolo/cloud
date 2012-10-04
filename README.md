cloud
=====

Python port of https://github.com/zeke/cloud.

A CLI for uploading files to CloudApp.

![http://cl.ly/image/2c1Z1Z1c1A2h](http://cl.ly/image/2c1Z1Z1c1A2h/content#.png)

Usage
-----

Run `cloud path/to/any/file.jpg` and get back a CloudApp URL in your clipboard.

Installation
------------

Add `CLOUDAPP_USERNAME` and `CLOUDAPP_PASWWORD` to your ENV, then:

```bash
  pip install -e git+git://github.com/originell/pycloudapp.git#egg=cloudapp
  curl -o /usr/local/bin/cloud https://raw.github.com/marksteve/cloud/master/cloud.py
  chmod +x /usr/local/bin/cloud
```