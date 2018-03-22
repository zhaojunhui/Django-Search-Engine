#coding=utf-8
import MySQLdb
import re
import urllib2

def init_db(s):

    word_checked = set()

    num = 0

    dic = {}

    try:
        conn = MySQLdb.connect(host = "localhost", port = 6668, user = "root", \
                           passwd = "xzw13607011526", db = "news_thu" ,charset="utf8");
    except:
        print "hah"
    else:
        cur = conn.cursor()
        cur.execute("create table index1(cnt int, name varchar(40))")
        for i in range(0, s):
            f = open('./words/%d.txt'%(i),"r")
            word_in_this = set()
            for line in f:
                print line
                if line not in word_checked:
                    word_checked.add(line)
                    value = [num, line]
                    cur.execute('insert into index1 values(%s, %s)',value)
                    dic[line] = num
                    cur.execute('create table N' + str(num) + '(cnt int, html_num int)')
                    value = [num, i]
                    cur.execute('insert into N' + str(num) + ' values(%s, %s)',value)
                    word_in_this.add(line)
                    num += 1
                elif line not in word_in_this:
                    word_in_this.add(line)
                    value = [dic[line], i]
                    cur.execute('insert into N' + str(dic[line]) + ' values(%s, %s)',value)


        cur.close()
        conn.commit()
        conn.close()

init_db(39051)