import re
import js2py
import codecs
import jsbeautifier
import array
import base64
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def Detonation2(oMatch):
	context = js2py.EvalJs({'python_sum': sum})  
	str1='function ulrich(t, y, u)\r\n{\r\n\treturn u[\'len\' + \'gth\'];\r\n};var b='+oMatch.group(1)+'; \nvar a=(b);'
	context.execute(str1)
	return '\"'+str(context.a)+'\"'

def UnicodeExcape(oMatch):
	c=oMatch.group(1)
	c=re.sub(r"[\s\t\n]",'',c)
	c=c.decode('unicode-escape')
	return c

def Decode(data):
		d=data
		d=re.sub(r"(\(function\s[a-zA-Z\d]+\(\)[\r\n\s\t]+\{[\r\n\s\t]+[\w\s\=\,\'\;\{\}\(\)\r\n\:A-Z\[\]]+return[\r\n\s\t]+String\[\"fromCharCode\"\]\([A-Za-z\d]+\s\-\sulrich\(1\,\s\'[a-zA-Z\d]+\'\,\sarguments\)\)\;[\r\n\s\t]+\}\)\([\'a-zA-Z\d\'\,\s]+\))",Detonation2,d)
		d=re.sub(r"\"\s\+\s\"","",d)
		d=re.sub(r"([a-z]{3,10})\s*\\\s*u([\da-f]+)","\\1 \\u\\2",d,flags=re.MULTILINE)
		d=re.sub(r"\\[\s\r\t\n]+(u[\da-f]{4})","\\\\\\1",d)
		d=re.sub(r"(\\u[\da-f]{4})", UnicodeExcape, d)

		
		return d