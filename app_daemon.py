from time import sleep
from daemonize import Daemonize
import argparse
import os

pid = "/tmp/this_app.pid"

def main():
    if not os.path.exists('{}/folder'.format(os.getcwd())):
        os.system('mkdir {}/folder'.format(os.getcwd()))

    # Set global variables from argparse
    t, path  = set_global(args)

    # Start index    
    idx = 0
    
    while True:
        sleep(t)
        os.system('touch {}/folder/{}'.format(path, idx))
        idx += 1

def set_global(args):
    
    return args['t'], args['path']

if __name__ == '__main__':
    
    # Arguments
    parser = argparse.ArgumentParser(description='Dump files in a given directory for in a given time')
    parser.add_argument('--t', default=1, type=float)
    parser.add_argument('--path', default=os.getcwd(), type=str)
    args = vars(parser.parse_args()) 

    # Start the app_daemon.py as service in UNIX

    daemon = Daemonize(app="app_daemon", pid=pid, action=main)
    daemon.start()
    