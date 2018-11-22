#!/usr/bin/python
#coding=utf-8

import cgi,cgitb

form = cgi.FieldStorage()

site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>W3Cschool教程 CGI测试</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")
