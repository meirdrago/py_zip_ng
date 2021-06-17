import os
import subprocess

def print_background_lib():
    dir = os.path.dirname(os.path.realpath(__file__))
    out = subprocess.getoutput('ldd {}/py_zip_ng*.so | grep zlib | grep -v grep'.format(dir))
    out = out.replace(dir, '')
    if out == '':
        out = 'system zlib'
        print("\033[91m[py_zip_ng background library: {}]\033[0m".format(out))
    else:
        out = out[2: ].strip()
        print("\033[92m[py_zip_ng background library: {}]\033[0m".format(out))


def set_libz_ng_env_param():
    dir = os.path.dirname(os.path.realpath(__file__))
    for i in os.listdir(dir):
        if 'libz' in i:
            os.environ['LD_PRELOAD'] = "{}/{}".format(dir, i)
            return


set_libz_ng_env_param()

from .py_zip_ng import *
