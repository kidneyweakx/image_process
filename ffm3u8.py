# -*- coding: utf-8 -*-
# Created on 2018/07/26
import os
import requests
import ffmpy
for i in range(87,88):
    uri = "" # want 
    ff = ffmpy.FFmpeg(
	    inputs = { uri : None},
	    outputs = {"cash"+str(i)+".mp4" : None})
    ff.run()
