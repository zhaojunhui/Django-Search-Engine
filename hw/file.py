#coding=utf-8

import re
import urllib2
import jieba
import jieba.posseg as pseg


def save_in_file(s):
    for i in range(0,s):
        try:
            f = open("./html/%d.html" % (i),"r")
            html = f.read()
            fcontain = open("./contain/%d.txt"%(i),"w")
            fwords = open("./words/%d.txt"%(i),"w")
            ftime = open("./time/%d.txt"%(i),"w")
        except:
            print "fail to open file"
        else:
            con_zz = r'(?<=<title>).+?(?=</title>)'
            L =  re.findall(con_zz, html, re.I|re.S|re.M)
            #print L
            for t in L:
                tar = r'<[^>]+>'
                t = re.sub(tar,'',t)
                fcontain.write(t + '\n')

                words = pseg.cut(t)
                for w in words:
                    if 'n' in w.flag:
                        fwords.write(w.word.encode('utf8') + '\n')

                break

            con_zz = r"(?<=<article class=\"article\">).+?(?=<div class=\"articletimewrapper\">)"
            L =  re.findall(con_zz, html, re.I|re.S|re.M)
            for t in L:
                tar = r'<[^>]+>'
                t = re.sub(tar,'',t)
                tar_2 = r'&[^;]+;'
                t = re.sub(tar_2,'',t)
                fcontain.write(t + '\n')
                words = pseg.cut(t)
                for w in words:
                    if 'n' in w.flag:
                        fwords.write(w.word.encode('utf8') + '\n')

                break

            con_zz = r'(?<=<div class=\"articletime\"><i class=\"thunews-clock-o\"></i>).+?(?=　　清华新闻网</div>)'
            L = re.findall(con_zz, html, re.I|re.S|re.M)
            #print L

            for t in L:
                ftime.write(t + '\n')
                break;

            fcontain.close()
            fwords.close()
            ftime.close()
