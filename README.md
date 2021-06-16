# py_zip_ng


Thin wrapper over [zlib-ng](https://github.com/zlib-ng/zlib-ng) library. 

python bindings to fast zlib implementation. 

For further explanation about zlib-ng please reffer to [zlib-ng](https://github.com/zlib-ng/zlib-ng)


## Usage

```python
import py_zip_ng
import zlib

s = b"Some binary data ..."

zlib_ng_comp = py_zip_ng.compress(s)
zlib_comp = zlib.compress(s)
assert zlib_ng_comp == zlib_comp

zlib_ng_decomp = py_zip_ng.decompress(zlib_ng_comp)
zlib_decomp = zlib.decompress(zlib_comp)

assert zlib_ng_decomp == zlib_decomp

```



## build instructions

**Requirements:**

-   rust-toolchain (i.e cargo, rustc)
-   python3-dev or python3-devel

**building and installing**
```
pip install setuptools-rust setuptools wheel
python3 setup.py install --user
```

**zlib-ng dependency**

This package comes with pre compile zlib-ng library compiled on x86-64 Linux Ubuntu with Intel AVX instructions.
if recompilation needed please follow next steps:

```
git clone https://github.com/zlib-ng/zlib-ng.git && cd zlib-ng

cmake -DZLIB_COMPAT=ON -DZLIB_ENABLE_TESTS=OFF .
cmake --build . --config Release

```

Please note that in order to run with zlib-ng library instead of system zlib
one need to export environment variable:

```
export LD_PRELOAD=path/to/libz.so.1.2.11.zlib-ng
```







 

