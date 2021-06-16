import py_zip_ng
import zlib


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
except Exception as e:
    print(e)

try:
    zlib.decompress(s)
except Exception as e:
    print(e)

