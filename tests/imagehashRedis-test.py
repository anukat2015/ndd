#!/usr/bin/env python

'''
    imagehashRedis-test.py
    
    Test Imagehash class (w/ Redis backend)
'''

import sys
import ndd

orig1 = ndd.utils.load_img('./data/orig1.jpg')
orig2 = ndd.utils.load_img('./data/orig2.jpg')
orig3 = ndd.utils.load_img('./data/orig3.jpg')
dup1  = ndd.utils.load_img('./data/dup1.jpg')

# Test from scratch
nh = ndd.ImagehashRedis()
nh.add('orig1', orig1)
nh.add('orig3', orig3)

assert(nh.query(orig1).has_match) # Exact match
assert(~nh.query(orig2).has_match) # No match
assert(nh.query(dup1).has_match) # Near-duplicate