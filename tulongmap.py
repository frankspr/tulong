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
      FromAPI = "/api/login.php"
      FromYY = "/yy/"
      Frompps = "/pps/"
      From37 = "/37/login.php"
#      Fromsogou = "/sogou/"
      From4399 = "/4399/login.php"
      Fromxunlei = "/xunlei/login.php"
      #define platform uid vars
      apiUid = 'uid'
      yyUid = 'account'
      ppsUid = 'user_id'
      sqUid = 'user_name'
      ssjjUid = 'username'
      xunleiUid = 'username'
      #Catch 
      if re.match(r"%s" %FromAPI,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
          if len(lst) >=6:
            try:
              for k in lst:
                if re.search(r'%s' % apiUid,k):
                  UID = (re.split('=',k))[1]
                if  re.search(r'platform',k):
                  Platform = (re.split('=',k))[1]
              print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass 
      if re.match(r"%s" % FromYY,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
          if len(lst) >=6:
            try:
              for uid in lst:
                if re.search(r'%s' % yyUid,uid):
		  UID = (re.split('=',uid))[1] 
                  Platform = 'yy'
                  print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
                else:
                  pass
            except:
              pass
        except:
	  pass
      if re.match(r"%s" % Frompps,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
	  if len(lst) >=6:
            try:
              for uid in lst:
                if re.search(r'%s' % ppsUid,uid):
                  UID = (re.split('=',uid))[1]
                  Platform = 'pps'
                  print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
                else:
                  pass

#              uid = lst[0]
#              UID = (re.split('=',uid))[1]
#              Platform = 'pps'
#              print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass
      if re.match(r"%s" % From37,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
          if len(lst) >=6:
	    try:
              for uid in lst:
                if re.search(r'%s' % sqUid,uid):
                  UID = (re.split('=',uid))[1]
                  Platform = '37'
                  print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
                else:
                  pass

#              uid = lst[0]
#              UID = (re.split('=',uid))[1]
#              Platform = '37'
#	      print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
	    except:
	      pass
        except:
          pass
#      if re.match(r"%s" % Fromsogou,RequestUrl):
#        try:
#          lst = re.split('&',RequestUrl)
#          if len(lst) >= 7:
#            try:
#              uid = lst[2]
#              UID = (re.split('=',uid))[1]
#              Platform = 'sogo'
#	      print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
#            except:
#              pass
#        except:
#	  pass
      if re.match(r"%s" % From4399,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
	  try:
              for uid in lst:
                if re.search(r'%s' % ssjjUid,uid):
                  UID = (re.split('=',uid))[1]
                  Platform = '4399'
                  print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
          except:
	    pass
        except:
	  pass
      if re.match(r"%s" % Fromxunlei,RequestUrl):
        try:
          lst = re.split('&',RequestUrl)
	  try:
              for uid in lst:
                if re.search(r'%s' % xunleiUid,uid):
                  UID = (re.split('=',uid))[1]
                  Platform = 'xunlei'
                  print '%s\t%s\t%s' % (ClientIP ,UID , Platform)
                else:
                  pass
          except:
	    pass
        except:
          pass
    else:
      pass

if __name__ == '__main__':
  main()
