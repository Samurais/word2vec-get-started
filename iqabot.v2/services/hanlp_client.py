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

import requests
import json
import re
from util import log
from config import HANLP_CONFIG

logger = log.getLogger(__file__)

def isNotEmpty(s):
    return bool(s and s.strip())

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Connection': 'close'
}


def polish(sentence):
    '''
    Delete chaos in sentence
    '''

    # remove [emoji]
    sentence = re.sub("\[(\w*)\]", '', sentence)

    # remove mention people
    sentence = re.sub("@(\w*)\s", '', sentence)
    sentence = re.sub("@(\w*)$", '', sentence)

    return sentence


def cut(sentence, type="crf"):
    api_url = '%s/tokenizer' % HANLP_CONFIG['url']
    body_data = dict({"type": type, "content": sentence})

    response = requests.post(api_url, headers=headers, data=json.dumps(
        body_data, ensure_ascii=False).encode('utf-8'))
    responseJSON = response.json()
    if 'data' in responseJSON.keys():
        return responseJSON
    else:
        raise Exception('Can not get data for %s' % sentence, responseJSON)


def pos(sentence, type="crf"):
    if sentence:
        response = cut(sentence, type=type)
        data = [x['word'] for x in response['data']]
        cleanData = ' '.join(data)
        if isNotEmpty(cleanData):
            return dict({
                'pos': response['data'],  # 词性标注
                'words': data,  # 单词数组
                'clean': cleanData  # 分词后成句
            })
        else: 
            raise Exception('Empty sentence for cleanData.')
    else:
        raise Exception('Empty sentence for pos.')


def polish_n_pos(sentence, type="crf"):
    return pos(polish(sentence), type="crf")


def main():
    response = pos(polish('@刘德华 和张学友@foo 创作了很多流行歌曲[汗][勒]@bar'))
    print(response)


if __name__ == '__main__':
    main()
