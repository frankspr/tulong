#!/usr/bin/env python
import sys
import re
# input comes from STDIN (standard input)  
for line in sys.stdin:
    # remove leading and trailing whitespace  
    line = line.strip()
    # split the line into words  
    words = line.split()
    #print words
    #print "========================"
    if len(words) >= 6:
      RequestUrl = words[6]
      ClientIP = words[0]
      FromAPI = "/api/"
      FromYY = "/yy/login"
      Frompps = "/pps/"
      From37 = "/37/"
      Fromsogou = "/sogou/"
      From4399 = "/4399/login"
      Fromxunlei = "/xunlei/"
      if re.match(r"%s" %FromAPI,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          print list
          uid = list[0]
          platform = list[1]
          UID = (re.split('=',uid))[1]
          Platform = (re.split('=',platform))[1]
        except:
          pass
        print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1) 
      if re.match(r"%s" % FromYY,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          uid = list[0]
          UID = (re.split('=',uid))[1]
          Platform = 'yy'
        except:
	  pass
        print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
      if re.match(r"%s" % Frompps,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          uid = list[0]
          UID = (re.split('=',uid))[1]
          Platform = 'pps'
        except:
          pass
	print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
      if re.match(r"%s" % From37,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          uid = list[0]
          UID = (re.split('=',uid))[1]
          Platform = '37'
        except:
          pass
	print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
      if re.match(r"%s" % Fromsogou,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          if len(list) >= 7:
            uid = list[2]
            UID = (re.split('=',uid))[1]
            Platform = 'sogou'
        except:
	  pass
	print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
      if re.match(r"%s" % From4399,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          uid = list[0]
          UID = (re.split('=',uid))[1]
          Platform = '4399'
        except:
	  pass
	print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
      if re.match(r"%s" % Fromxunlei,RequestUrl):
        try:
          list = re.split('&',RequestUrl)
          uid = list[0]
          UID = (re.split('=',uid))[1]
          Platform = 'xunlei'
        except:
          pass
	print '%s\t%s\t%s\t%s' % (ClientIP ,UID , Platform,1)
    else:
      pass
