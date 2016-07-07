#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ROTはシーザー暗号の一種であり、指定された文字数をずらすだけの処理を行う。
# 大文字、小文字の関係は維持される。
# アスキー表をみるとA-Zは0x41(65)-0x5A(90), # a-zは0x61(97)-0x7A(122)として表現される。

# 参考文献
# https://ja.wikipedia.org/wiki/ROT13
# http://docs.python.jp/3/howto/argparse.html
# http://qiita.com/dodo5522/items/6ec2b6d83287add6c185
# http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html

import argparse
import sys
parser = argparse.ArgumentParser(description='ROTate string')
parser.add_argument("num", help="rotate number", type=int)
parser.add_argument("file", help="target file")
args = parser.parse_args()

def rot(n,c):
   codepoint = ord(c)
   if (65 <= codepoint <= 90):
       codepoint += n 
       if codepoint > 90: codepoint -= 26
       return chr(codepoint)
   elif (97 <= codepoint <= 122):
       codepoint += n 
       if codepoint > 122: codepoint -= 26
       return chr(codepoint)
   else:
       return c

strings = open(args.file).read()
char_list = list(strings)
for elm in char_list:
    sys.stdout.write(rot(args.num, elm))

