#-*-coding:utf-8-*-
from django.shortcuts import render, redirect

import socket
import chardet
import urllib2
import json

def get_ip(request):
    # 服务端IP
    hostname = socket.gethostname()
    ip1 = socket.gethostbyname(hostname)

    # 客户端IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  #所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')    #这里获得代理ip

    ip_list={}
    ip_list['host_ip'] = ip1
    ip_list['client_ip'] = ip

    locate = get_location(ip)
    if locate :
        lct = locate['CN'] + '/' + locate['PN'] + '/' + locate['CITY']
    else:
        lct = '地理位置获取失败'
    return render(request, 'index.html', {'data': ip_list, 'lct1': lct})


def get_location(get_ip):
    ip = get_ip
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    content = urllib2.urlopen(apiurl).read()
    data = json.loads(content)['data']
    code = json.loads(content)['code']
    if code == 0:
        CN = data["country"].encode('utf-8')
        REGION = data["region"].encode('utf-8')
        CITY = data["city"].encode('utf-8')
        if CN == 'XX' :
            return False
        else:
            locate = {}
            locate['CN'] = CN
            locate['PN'] = REGION
            locate['CITY'] = CITY
            return locate
    else:
        return False
