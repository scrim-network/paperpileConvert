#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 12 Jan 2018

@author: rsm5139
"""

import unittest
tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(tests)
