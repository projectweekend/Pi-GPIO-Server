#!/usr/bin/env python

import subprocess


def main():
    # Install system dependencies
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])
    subprocess.call(["apt-get", "-y", "install", "avahi-daemon"])

    #subprocess.call("echo Yes, do as I say! | sudo apt-get -y --force-yes install upstart", shell=True)

    # Copy Upstart script
    #subprocess.call(["cp", "./install/gpio-server.conf", "/etc/init"])

    # Copy systemd configuration
    subprocess.call(["cp", "./install/gpio-server.service", "/lib/systemd/system/"])
    subprocess.call(["chmod", "644", "/lib/systemd/system/gpio-server.service"])

if __name__ == '__main__':
    main()
