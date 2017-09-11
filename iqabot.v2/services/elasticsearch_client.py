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
'''
ElasticSearch Proxy
https://elasticsearch-py.readthedocs.io/en/master/
https://elasticsearch-py.readthedocs.io/en/master/api.html
'''
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-09-10:21:54:17"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(curdir, os.pardir))

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

from datetime import datetime
from config import ELASTICSEARCH_CONFIG
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

esclient = Elasticsearch([ELASTICSEARCH_CONFIG['url']]) if ELASTICSEARCH_CONFIG['user'] is None else \
    Elasticsearch([ELASTICSEARCH_CONFIG['url']], \
        http_auth=(ELASTICSEARCH_CONFIG['user'], ELASTICSEARCH_CONFIG['pass']))

class ESImportChecker(object):
    def __call__(self, f):
        def wrapper(self, *args, **kwargs):
            if ELASTICSEARCH_CONFIG['enable']:
                return f(self, *args, **kwargs)
            else:
                # ignore the request
                pass
        return wrapper


@ESImportChecker()
def index(message_id, message_body, index="insuranceqa", doc_type="zh_CN"):
    '''
    Create or Update message
    '''
    return esclient.index(index=index, doc_type=doc_type, id=message_id, body=message_body)


def flush(index):
    '''
    flush index
    '''
    esclient.flush(index=index, force=True, wait_if_ongoing=True)

def search(index, terms, explain=False):
    '''
    query by terms
    http://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html
    '''
    should = []
    for o in terms:
        should.append(Q("match", terms=o))
    q = Q('bool', should=should)

    response = esclient.search(index=index, body = dict({
        "query": q.to_dict()
    }), explain=explain)
    return response

if __name__ == '__main__':
    # put_message('1111', dict({
    #     'foo': 'bar',
    #     'timestamp': datetime.now()
    # }))
    query = ["残疾", "保险"]
    response = search('insuranceqa', query)
    if response["hits"]["total"] > 0 and len(response["hits"]["hits"]) > 0:
        print("query:", "".join(query))
        for o in response["hits"]["hits"]:
            print("hit %s : %s score: %s" % (o["_source"]["id"], o["_source"]["post"], o["_score"]))