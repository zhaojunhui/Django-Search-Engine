import re
import urllib2
import cookielib
import mmap
from file import*

# head_title = "http://news.tsinghua.edu.cn"
# root_node = "/publish/thunews/index.html"
# num = 0
#
# url_saved = set()
# tag_saved = set()
# url_saved.add(root_node)
# url_unchecked = [root_node]
# #dic = {0:root_node}
#
# while(True):
#     if len(url_unchecked) != 0:
#         req = urllib2.Request(head_title + url_unchecked[0])
#         try:
#             page = urllib2.urlopen(head_title + url_unchecked[0])
#         except urllib2.HTTPError, e:
#             print e.code
#             del url_unchecked[0]
#         except urllib2.URLError, e:
#             print e.reason
#             del url_unchecked[0]
#         except:
#             print "Unknown Error"
#             del url_unchecked[0]
#         else:
#             html = page.read()
#             #print html
#             if len(url_unchecked[0]) >= 60:
#                 if url_unchecked[0][-29:-6] == url_unchecked[0][-53:-30]:
#                     #print url_unchecked[0][-29:-6]
#                     if url_unchecked[0][-29:] not in tag_saved:
#                         tag_saved.add(url_unchecked[0][-29:])
#                         ftxt = open("./html/" + str(num) + ".html", "w")
#                         ftxt.write(html)
#                         #dic[num] = url_unchecked[0]
#                         num += 1
#                         print num
#             url =  r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
#             L = re.findall(url, html, re.I|re.S|re.M)
#             #print L
#             for i in range(0, len(L)):
#                 if len(L[i]) <= 20:
#                     continue
#                 elif L[i][-5:] != '.html':
#                     continue
#                 elif L[i][0:17] != '/publish/thunews/':
#                     continue
#                 if L[i] not in url_saved:
#                     #print L[i]
#                     url_saved.add(L[i])
#                     url_unchecked.append(L[i])
#                     #print url_unchecked
#             #print url_unchecked
#             del url_unchecked[0]
#     else:
#         break
save_in_file(39051)