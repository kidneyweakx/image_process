# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:42:41 2019

@author: kidneyweakx
"""

import ffmpy
ff = ffmpy.FFmpeg(
	inputs = {"main.mp4" : None},
	outputs = {"cash.gif" : None})

ff.run()
