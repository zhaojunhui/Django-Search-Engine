#coding=utf-8

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb
import jieba
import jieba.posseg as pseg
import re
import urllib2
import time

conn = MySQLdb.connect(host = 'localhost', port = 6668, user = 'root', passwd = 'xzw13607011526',db = 'news_thu', charset='utf8')
cur = conn.cursor()


cur.execute('select * from index1')
rows = cur.fetchall()
cur_time = time.localtime()
#print cur_time
cur_year = cur_time.tm_year
cur_month = cur_time.tm_mon
cur_week = cur_time.tm_mday
#print cur_year
#f = open('./contain/0.txt')
#title = f.readline()
#contain = f.read()
#print title
#print contain
#print rows[0][1]
# cur.execute('select html_num from N0')
# html_nums = cur.fetchall()
# print html_nums

def index(request):

    input_get = ''
    words = []
    ideal_nums = []
    info_list = []
    info_list_num = 0

    if request.method == 'GET':
        if request.GET.has_key('input'):
            input_get = request.GET['input']
            wordstmp = pseg.cut(input_get)
            for word in wordstmp:
                #print word.word
                words.append(word.word)
            #print words[0]
        if request.GET.has_key('search'):
            if input_get == '':
                return render(request, 'notfound.html')
            else:
                for word in words:
                    word = word.replace("\n","")
                    for r in rows:
                        if word == r[1][0:-1]:
                            ideal_nums.append(r[0])
                       
                #print ideal_num        
                if len(ideal_nums) == 0:
                    return render(request, 'notfound.html')
                for ideal_num in ideal_nums:
                    cur.execute('select html_num from N' + str(ideal_num))
                    html_nums = cur.fetchall()
                    #print html_nums
                    for h in html_nums:
                        #print h[0]
                        fcontain = open('./Search/contain/' + str(h[0]) + '.txt')
                        title = fcontain.readline()
                        #print title
                        bl = fcontain.readline()
                        ff = fcontain.read()
                        ff = ff.decode("utf-8")
                        if len(ff) < 400:
                            contain = ff
                        else:
                            contain = ff[0:401]
                        for word in words:
                            word = word.replace(" ","")
                            if word == "":
                                continue
                            tmp_word = "<font color='red'>" + word + "</font>"
                            #word = word.decode("utf-8")
                            #tmp_word = tmp_word.decode("utf-8")
                            contain = contain.replace(word, tmp_word)
                            #print contain
                        ftime = open('./Search/time/' + str(h[0]) + '.txt')
                        time = ftime.read()
                        time = time.decode("utf-8")
                        if request.GET.has_key('year'):
                            #print 'ahha'
                            if time[0:4] != str(cur_year):
                                #print time[0:4], cur_year
                                continue
                            elif request.GET.has_key('month'):
                                tmp_month = ""
                                if cur_month <= 9:
                                    tmp_month = "0" + str(cur_month)
                                else:
                                    tmp_month = str(cur_month)
                                if time[5:7] != tmp_month:
                                    #print time[5:7], tmp_month
                                    continue
                                elif request.GET.has_key('week'):
                                    tmp_week = ""
                                    if time[8] == "0":
                                        tmp_week = time[9]
                                    else:
                                        tmp_week = time[8:10]
                                    if cur_week - int(tmp_week) > 7:
                                        print cur_week, tmp_week
                                        continue
                        info_list.append({'title':title,'contain':contain,'time':time,'url_num': str(h[0])})
                        info_list_num += 1
                return render(request, 'index.html', {'info_list':info_list,'info_list_num':info_list_num})
    return render(request, 'home.html')
    


# Create your views here.
