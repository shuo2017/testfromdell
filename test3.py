#!/usr/bin/env python

import os, sys
import json

def _createLUNbyArray(size):

    """

    :param size: LUN的大小
    :return: 创建成功返回LUNID， 失败返回None
    """
    return lunid

def _rollbackCreateLUN(lunids):
    pass

def createLUN(size, number):
    """

    :param size: LUN的大小
    :param number: 需创建LUN的个数
    :return: code 200 表示创建成功， code 500 表示创建失败
    """
    code = 0  # 500 Server internal error, 200 create success

    luns = []
    if number >= 1:
        for i in range(number):
            lunid = _createLUNbyArray(size)
            if lunid:
                luns.append(lunid)
                code = 200
            else:
                # 有一个LUN创建不成功就将之前的撤销
                _rollbackCreateLUN(luns)
                code = 500
                break
    if code == 200:

        
        return json.dumps({'code': 200, 'LUNS': luns})
    else:
        return json.dumps({'code': 500, 'message': 'Server internal error'})


def _doResizeLUN(lunid, size):
    code = 200
    return code

def resizeLUN(lunid, size):
    """

    :param lunid:
    :param size:
    :return: code 200 表示resize成功并返回size
    """
    code = _doResizeLUN(lunid, size)
    if code == 200:
        return json.dumps({'code': 200, 'size': size})
    else:
        return json.dumps({'code': 500, 'message': 'Server internal error'})

def _doRemoveLUN(lunid):
    code = 200
    return code

def removeLun(lunid):
    code = _doRemoveLUN(lunid)
    if code == 200:
        return json.dumps({'code': 200})
    else:
        return json.dumps({'code': 500, 'message': 'Server internal error'})


def _doRetrieveLUN(lunid):
    info = {'size': '10G', 'reserved': 1}
    return info

def retrieveLUN(lunid):
    info = _doRetrieveLUN(lunid)
    if info:
        return json.dumps({'code': 200, 'info': info})
    else:
        return json.dumps({'code': 500, 'message': 'Server internal error'})



# 本程序只着重演示接口参数和json 返回数据，4，5 两个接口没有实现

def main():
    apiname = sys.argv[1]
    if apiname == 'createLUN':
        createLUN()

    if apiname == 'resizeLUN':
        resizeLUN()

    if apiname == 'removeLun':
        removeLun()

    if apiname == 'retrieveLUN':
        retrieveLUN()
