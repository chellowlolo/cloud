#!/usr/bin/env python

import os
import subprocess
import sys

from cloudapp.cloud import Cloud


def main():
    c = Cloud()
    c.auth(os.environ['CLOUDAPP_USERNAME'], os.environ['CLOUDAPP_PASSWORD'])
    drop = c.upload_file(sys.argv[1])
    subprocess.Popen('echo %s | pbcopy' % drop['url'], shell=True)
    print drop['url']
    print drop['content_url']
    print


if __name__ == '__main__':
    main()
