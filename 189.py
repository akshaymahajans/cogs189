#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 19:27:20 2018

@author: akshaymahajan
"""

import numpy as np
import pandas as pd
import io

df = pd.read_fwf('../cogs189/akshay_base1.txt',header=None)
text = df[2]
text = [str(s).replace(',','') for s in text]
text = pd.Series(text)
df[2] = text
print(df[2])