#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/elasticsearch-get-started/tools/config.py
# Author: Hai Liang Wang
# Date: 2017-09-10:21:54:17
#
#===============================================================================

"""
Config   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-09-10:21:54:17"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

ROOT_PATH = os.path.realpath(os.path.join(curdir, os.pardir))

CONFIG = dict({
    "log_level": "INFO",
    "log_path": "./logs"
})

CORPUS_CONFIG = dict({
    "test": os.path.join(ROOT_PATH, "corpus", "insuranceqa", "elasticsearch", "test.questions.txt"),
    "train": os.path.join(ROOT_PATH, "corpus", "insuranceqa", "elasticsearch", "train.questions.txt"),
    "valid": os.path.join(ROOT_PATH, "corpus", "insuranceqa", "elasticsearch", "valid.questions.txt")
})

W2V_CONFIG = dict({
    "model": os.path.join(ROOT_PATH, "corpus", "wikidata", "zhwiki-latest-pages-articles", "chs.normalized.wordseg.w2v")
})

HANLP_CONFIG = dict({
    'url': 'http://localhost:3007'
})

# ElasticSearch Options
# https://elasticsearch-py.readthedocs.io/en/master/api.html#global-options
ELASTICSEARCH_CONFIG = dict({
    'enable': True,
    'url': 'http://localhost:9200/',
    'user': None,
    'pass': None
})
