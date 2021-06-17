import os
import platform

if platform.system().lower() != "windows":
    import py_zip_ng
else:
    import zlib as py_zip_ng

import zlib

if os.path.exists(os.environ.get('LD_PRELOAD', '')):
    print("\033[92m[py_zip_ng background library:\033[0m   {}]".format(os.environ.get('LD_PRELOAD', '')))


assert py_zip_ng.MAX_WBITS == zlib.MAX_WBITS

s = b"barracuda 123"

zlib_ng_comp = py_zip_ng.compress(s)
zlib_comp = zlib.compress(s)
assert zlib_ng_comp == zlib_comp

zlib_ng_decomp = py_zip_ng.decompress(zlib_ng_comp)
zlib_decomp = zlib.decompress(zlib_comp)

assert zlib_ng_decomp == zlib_decomp

# errors
try:
    py_zip_ng.decompress(s)
    assert False
except Exception as e:
    assert True

try:
    zlib.decompress(s)
    assert False
except Exception as e:
    assert True

print("OK")

