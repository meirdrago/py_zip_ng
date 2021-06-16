#![allow(unused)]

use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::wrap_pyfunction;
use pyo3::exceptions::PyException;

use log::{warn, debug, info};
use pyo3_log::{Caching, Logger};
use flate2::write::{ZlibDecoder, ZlibEncoder};
use flate2::Compression;
use std::io;
use std::io::prelude::*;


fn zlib_compress(bytes: Vec<u8>) -> io::Result<Vec<u8>> {
    let mut e = ZlibEncoder::new(Vec::new(), Compression::default());
    e.write_all(&bytes[..])?;
    let res = e.finish()?;
    Ok(res)
}

fn zlib_decompress(bytes: Vec<u8>) -> io::Result<Vec<u8>> {
    let mut writer = Vec::new();
    let mut z = ZlibDecoder::new(writer);
    z.write_all(&bytes[..])?;
    writer = z.finish()?;
    Ok(writer)
}



#[pyfunction]
#[text_signature = "(bytes, /)"]
fn decompress(ppy: Python, bytes: Vec<u8>) -> PyResult<PyObject> {
    match zlib_decompress(bytes){
        Ok(res) => {
            let py_bytearray = PyBytes::new_with(ppy, res.len(), |bts: &mut [u8]| {
                bts.copy_from_slice(&res);
                Ok(())
            });
            match py_bytearray{
                Ok(pybytes) => Ok(pybytes.to_object(ppy)),
                Err(e) => {
                    Err(PyException::new_err("py-zip-ng ERROR decompress"))
                }
            }
        },
        Err(e)  => {
            Err(PyException::new_err("py-zip-ng ERROR decompress"))
        }
    }
}


#[pyfunction]
#[text_signature = "(bytes, /)"]
fn compress(ppy: Python, bytes: Vec<u8>) -> PyResult<PyObject> {
    match zlib_compress(bytes){
        Ok(res) => {
            let py_bytearray = PyBytes::new_with(ppy, res.len(), |bts: &mut [u8]| {
                bts.copy_from_slice(&res);
                Ok(())
            });
            match py_bytearray{
                Ok(pybytes) => Ok(pybytes.to_object(ppy)),
                Err(e) => {
                    Err(PyException::new_err("py-zip-ng ERROR compress"))
                }
            }
        },
        Err(e)  => {
            Err(PyException::new_err("py-zip-ng ERROR compress"))
        }
    }
}


#[pymodule]
fn py_zip_ng(py: Python, m: &PyModule) -> PyResult<()> {
    Logger::new(py, Caching::LoggersAndLevels)?
                                        .install();

    m.add("MAX_WBITS", 15_i64).unwrap();
    m.add_function(wrap_pyfunction!(compress, m)?).unwrap();
    m.add_function(wrap_pyfunction!(decompress, m)?).unwrap();
    //m.add_class::<FcmClient>()?;
    Ok(())
}
