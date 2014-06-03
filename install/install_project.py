#!/usr/bin/env python

import subprocess


def main():
    # Setup the virtualenv
    subprocess.call(["virtualenv", "env", "--no-site-packages"])


if __name__ == '__main__':
    main()
