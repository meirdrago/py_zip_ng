from setuptools import setup
from setuptools_rust import Binding, RustExtension
import subprocess
import os

subprocess.run("curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y", shell=True)
os.environ['PATH'] = os.environ.get("HOME", "") + '/.cargo/bin:' + os.environ.get("PATH", "")


setup(
    name="py_zip_ng",
    version="0.1.0",
    rust_extensions=[RustExtension("py_zip_ng.py_zip_ng", binding=Binding.PyO3)],
    packages=["py_zip_ng"],
    include_package_data=True,
    package_dir={'py_zip_ng': '.'},
    package_data={'py_zip_ng': ['libz.so.1.2.11.zlib-ng']},
    zip_safe=False,
)
