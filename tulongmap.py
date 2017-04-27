#!/usr/bin/env python
#coding:utf-8
#author: Frank
#version: v1.0
#date: 20170426
#log analysis mapper
import sys
import re
# input comes from STDIN (standard input) 
def main(): 
  for line in sys.stdin:
    # remove leading and trailing whitespace  
    line = line.strip()
    # split the line into words  
    words = line.split()
    if len(words) >= 6:
      RequestUrl = words[6]
      #define vars
      ClientIP = words[0]
      FromAPI = "/api/"
      FromYY = "/yy/login"
      Frompps = "/pps/"
      From37 = "/37/"
      Fromsogou = "/sogou/"
      From4399 = "/4399/login"
      Fromxunlei = "/xunlei/"
      #Catch 
      if re.match(r"%s" %FromAPI,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          if len(list) >=6:
            try:
              uid = list[0]
              platform = list[1]
              UID = (re.split('=',uid))[1]
              Platform = (re.split('=',platform))[1]
	      print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass 
      if re.match(r"%s" % FromYY,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          if len(list) >=6:
            try:
              uid = list[0]
              UID = (re.split('=',uid))[1]
              Platform = 'yy'
              print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
            except:
              pass
        except:
	  pass
      if re.match(r"%s" % Frompps,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
	  if len(list) >=6:
            try:
              uid = list[0]
              UID = (re.split('=',uid))[1]
              Platform = 'pps'
              print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass
      if re.match(r"%s" % From37,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          if len(list) >=6:
	    try:
              uid = list[0]
              UID = (re.split('=',uid))[1]
              Platform = '37'
	      print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass
      if re.match(r"%s" % Fromsogou,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          if len(list) >= 7:
            try:
              uid = list[2]
              UID = (re.split('=',uid))[1]
              Platform = 'sogo'
	      print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
            except:
              pass
        except:
	  pass
      if re.match(r"%s" % From4399,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
	  try:
            uid = list[0]
            UID = (re.split('=',uid))[1]
            Platform = '4399'
	    print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
          except:
	    pass
        except:
	  pass
      if re.match(r"%s" % Fromxunlei,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
	  try:
            uid = list[0]
            UID = (re.split('=',uid))[1]
            Platform = 'xunlei'
            print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
          except:
	    pass
        except:
          pass
    else:
      pass

if __name__ == '__main__':
  main()
