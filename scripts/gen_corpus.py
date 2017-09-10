#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/word2vec-get-started/scripts/gen_corpus.py
# Author: Hai Liang Wang
# Date: 2017-09-10:12:21:08
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-09-10:12:21:08"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import gzip

def generate_category_raw_token_txt(en_zh_file, zh_tokenized_file, target):
    with gzip.open(en_zh_file, "r") as fin1, \
        open(zh_tokenized_file, "r") as fin2,\
        open(target, "w") as fout:
        for index,line in enumerate(zip(fin1, sorted(fin2, key=lambda x: int(x.split(" ++$++ ")[0])))):
            en_zh = line[0].split(" ++$++ ")
            zh_token = line[1].split(" ++$++ ")
            interest = [str(index), en_zh[1], en_zh[2], zh_token[1]]
            fout.write(" ++$++ ".join(interest))

if __name__ == '__main__':
    en_zh = ["valid.txt.gz", "test.txt.gz", "train.txt.gz"]
    zh_tokenized = ["iqa.questions.valid", "iqa.questions.test", "iqa.questions.train"]
    target = ["valid.questions.txt", "test.questions.txt", "train.questions.txt"]
    for x,y,z in zip(en_zh, zh_tokenized, target):
        # print(x, y, z)
        en_zh_file=os.path.join(curdir, "..", "tmp", x)
        zh_tokenized_file=os.path.join(curdir, "..", "corpus", y)
        target=os.path.join(curdir, "..", "tmp", z)
        generate_category_raw_token_txt(en_zh_file, zh_tokenized_file, target)
