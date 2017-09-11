#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved
#
#   Calcualte similarity with word2vec model.
#   http://code.google.com/p/word2vec/
#
# File: iqabot.v2/services/similarity.py
# Author: Hai Liang Wang
# Date: 2017-07-29:14:09:27
#
#===============================================================================

from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2017-09-11:14:09:27"

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.pardir))

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import numpy as np
from config import W2V_CONFIG
from util import log

# logger
logger = log.getLogger(__file__)

def load_model(model_file = W2V_CONFIG["model"], binary=False):
    '''
    Load model with C format word2vec file.
    '''
    if not os.path.exists(model_file):
        raise Exception("Model file does not exist.")
    from gensim.models.keyedvectors import KeyedVectors
    return KeyedVectors.load_word2vec_format(model_file, binary=binary, unicode_errors='ignore')

def resolve_embedding_size(text_format_w2v_model):
    '''
    Get word2vec embedding size with text format model
    '''
    size = 0
    with open(text_format_w2v_model, "r") as fin:
        for x in fin:
            _, size = x.split()
            break
    if size == 0:
        raise Exception("Error with word2vec model.")
    return int(size)

# lambdas for cos similarity
sim_molecule = lambda x: np.sum(x, axis=0) # 分子
sim_denominator = lambda x: np.sqrt(np.sum(np.square(x)))  # 分母 

def _distance(sentence1, sentence2, V, embedding_size):
    '''
    compute cosine similarity of v1 to v2:
        (v1 dot v2)/{||v1||*||v2||)
    '''
    def _vector(sentence):
        '''
        get vector for a word
        '''
        vectors = []
        for x,y in enumerate(sentence.split()):
            try:
                y = y.decode('utf-8', errors='ignore').strip()
                logger.debug("get vector %s", y)
                if y: # discard word if empty
                    v =  V.wv[y]
                    vectors.append(v)
                else:
                    logger.debug("ignore word %s", y)
            except KeyError, error:
                logger.debug("out of vocabulary %s", y)
                vectors.append(np.zeros(embedding_size, dtype=float))
        return vectors

    a = sim_molecule(_vector(sentence1))
    b = sim_molecule(_vector(sentence2))
    A = sim_denominator(a)
    B = sim_denominator(b)

    similarity = np.dot(a, b) / (A * B)
    return float("%.3f" % similarity)

W2V_DIM_SZIE = resolve_embedding_size(W2V_CONFIG["model"])
W2V_MODEL = load_model(model_file=W2V_CONFIG["model"], binary=False)
logger.info("word2vec model loaded.")

def distance(s1, s2):
    '''
    Compute similarity for two given sentences
    '''
    return _distance(s1, s2, V=W2V_MODEL, embedding_size=W2V_DIM_SZIE)

def test_distance():
    # txts = ["一直 登录 不 上去 怎么办 ", "扫码 一直 不 能 成功 怎么办"]
    # txts = ["银行", "如果 我们 银行 要 变更 付款 方式 要 准备 什么"]
    txts = ["面试 前 会 有人 通知 我", "没有 收到 面试 也 没 听说 身边 朋友 收到 今年 面试 已经 结束"]
    print('loaded.')
    print(distance(txts[0], txts[1]))

if __name__ == '__main__':
    test_distance()