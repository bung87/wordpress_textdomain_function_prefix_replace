#!/usr/bin/python
import os
import sys
import re


if len(sys.argv)==1:
	sys.stdout.write('Type '+sys.argv[0]+' --help for help about this script')
	sys.exit()

info="""
 This program replace a wordpress theme textdomain,function prefix and make up a new theme folder
 Usually a theme folder name is same as textdomain and function prefix.
           Usage:
           ./wordpress_textdomain_replace.py <source directory> <your textdomain>
           Options:
           --version : Prints the version number
           --help    : Display this help
"""
def main(dn,td):
	dd=os.path.join(os.getcwd(),td)
	os.mkdir(dd,755)
	pa = re.compile("(_[_e]\([^']*'[^']+',[^']*)'([\w]+)'")
	p = os.path.join(os.getcwd(),dn)
	l = os.listdir(p)
	pl = list(filter((lambda f:os.path.join(p,f).endswith('.php')),l))
	for x in pl:
		fp = os.path.join(p,x)
	
		fr=open(fp,"r")
		try:
			t=fr.read()
		finally:
			fr.close()
		rt=pa.sub(lambda m:m.group(1)+"'"+td+"'",t)
		rt=rt.replace(dn+'_',td+'_')
		dp=os.path.join(dd,x)
		fw=open(dp,"w")
		try:
			fw.write(rt)
		finally:
			fw.close()

if sys.argv[1].startswith('--'):
   option = sys.argv[1][2:]

   if option == 'version':
      sys.stdout.write('Version 1.0') 
   elif option == 'help':
      sys.stdout.write(info)
          
   else:
       sys.stdout.write('Unknown option.')
       sys.exit()
else:

	main(sys.argv[1],sys.argv[2])