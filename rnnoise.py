#Author Shoaib Omar
import ctypes,numpy,os
from ctypes import util

lib_path = util.find_library("rnnoise")
if (not("/" in lib_path)):
	lib_path = (os.popen('ldconfig -p | grep '+lib_path).read().split('\n')[0].strip().split(" ")[-1] or ("/usr/local/lib/"+lib_path))
	
lib = ctypes.cdll.LoadLibrary(lib_path)
lib.rnnoise_process_frame.argtypes = [ctypes.c_void_p,ctypes.POINTER(ctypes.c_float),ctypes.POINTER(ctypes.c_float)]
lib.rnnoise_process_frame.restype = ctypes.c_float
lib.rnnoise_create.argtypes = [ctypes.c_void_p]
lib.rnnoise_create.restype = ctypes.c_void_p
lib.rnnoise_destroy.argtypes = [ctypes.c_void_p]

class RNNoise(object):
	def __init__(self):
		self.obj = lib.rnnoise_create(None)
	def process_frame(self,inbuf):
		outbuf = numpy.ndarray((480,), 'h', inbuf).astype(ctypes.c_float)
		outbuf_ptr = outbuf.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
		VodProb =  lib.rnnoise_process_frame(self.obj,outbuf_ptr,outbuf_ptr)
		return (VodProb,outbuf.astype(ctypes.c_short).tobytes())

	def destroy(self):
		lib.rnnoise_destroy(self.obj)