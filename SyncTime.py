# -*- coding: utf-8 -*-
import os
import time
import ntplib
def SyncTime(ntpserv):
    try:
        c = ntplib.NTPClient()
        print 'Synctime from %s ' % ntpserv
        response = c.request(ntpserv)
        ts = response.tx_time
    except ntplib.NTPException,e:
        print 'Synctime Failed,',e
        return False
    else:
        _date = time.strftime('%Y-%m-%d',time.localtime(ts))
        _time = time.strftime('%X',time.localtime(ts))
        os.system('date {} && time {}'.format(_date,_time))
        print 'Synctime Success!'
        return True

if __name__ == '__main__':
    with open('ntpserv.ini') as f:
        for eachline in f:
            ntpserv = eachline.strip('\n\r')
            if SyncTime(ntpserv):
                break