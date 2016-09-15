#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: Kevien
# Date: 2016.01.01

import urllib2
import re
import sys
import os

url = "http://www.360kb.com/kb/2_122.html"
req = urllib2.Request(url)
html = urllib2.urlopen(req).read()
text =html.split("#google hosts")[1]	

head = '''127.0.0.1	localhost
127.0.1.1	unix
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
#优酷
127.0.0.1 atm.youku.com
127.0.0.1 Fvid.atm.youku.com
127.0.0.1 html.atm.youku.com
127.0.0.1 valb.atm.youku.com
127.0.0.1 valf.atm.youku.com
127.0.0.1 valo.atm.youku.com
127.0.0.1 valp.atm.youku.com
127.0.0.1 lstat.youku.com
127.0.0.1 speed.lstat.youku.com
127.0.0.1 urchin.lstat.youku.com
127.0.0.1 stat.youku.com
127.0.0.1 static.lstat.youku.com
127.0.0.1 valc.atm.youku.com
127.0.0.1 vid.atm.youku.com
127.0.0.1 walp.atm.youku.com
#百度：
127.0.0.1 a.baidu.com
127.0.0.1 baidutv.baidu.com
127.0.0.1 bar.baidu.com
127.0.0.1 c.baidu.com
127.0.0.1 cjhq.baidu.com
127.0.0.1 cpro.baidu.com
127.0.0.1 drmcmm.baidu.com
127.0.0.1 e.baidu.com
127.0.0.1 eiv.baidu.com
127.0.0.1 hc.baidu.com
127.0.0.1 hm.baidu.com
127.0.0.1 ma.baidu.com
127.0.0.1 nsclick.baidu.com
127.0.0.1 spcode.baidu.com
127.0.0.1 tk.baidu.com
127.0.0.1 union.baidu.com
127.0.0.1 ucstat.baidu.com
127.0.0.1 utility.baidu.com
127.0.0.1 utk.baidu.com
127.0.0.1 focusbaiduafp.allyes.com
#奇艺
127.0.0.1 afp.qiyi.com
127.0.0.1 focusbaiduafp.allyes.com
#CNTV
127.0.0.1 a.cctv.com
127.0.0.1 a.cntv.cn
127.0.0.1 ad.cctv.com
127.0.0.1 d.cntv.cn
127.0.0.1 adguanggao.eee114.com
127.0.0.1 cctv.adsunion.com
#新浪视频
127.0.0.1 dcads.sina.com.cn
#pptv
127.0.0.1 pp2.pptv.com
#乐视
127.0.0.1 pro.letv.com
#搜狐高清
127.0.0.1 images.sohu.com
@HostsX 国内站点广告/视频类网站
#CNTV
127.0.0.1 a.cctv.com
127.0.0.1 a.cntv.cn
127.0.0.1 ad.cctv.com
127.0.0.1 d.cntv.cn
127.0.0.1 adguanggao.eee114.com
127.0.0.1 cctv.adsunion.com
#我乐网
127.0.0.1 acs.56.com
127.0.0.1 acs.agent.56.com
127.0.0.1 acs.agent.v-56.com
127.0.0.1 bill.agent.56.com
127.0.0.1 bill.agent.v-56.com
127.0.0.1 stat.56.com
127.0.0.1 stat2.corp.56.com
127.0.0.1 union.56.com
127.0.0.1 uvimage.56.com
127.0.0.1 v16.56.com
#6间房
127.0.0.1 pole.6rooms.com
127.0.0.1 shrek.6.cn
127.0.0.1 simba.6.cn
127.0.0.1 union.6.cn
#土豆网
127.0.0.1 adextensioncontrol.tudou.com
127.0.0.1 iwstat.tudou.com
127.0.0.1 nstat.tudou.com
127.0.0.1 stats.tudou.com
127.0.0.1 *.p2v.tudou.com*
127.0.0.1 at-img1.tdimg.com
127.0.0.1 at-img2.tdimg.com
127.0.0.1 at-img3.tdimg.com
127.0.0.1 adplay.tudou.com
127.0.0.1 adcontrol.tudou.com
127.0.0.1 stat.tudou.com
#酷6网
127.0.0.1 1.allyes.com.cn
127.0.0.1 analytics.ku6.com
127.0.0.1 gug.ku6cdn.com
127.0.0.1 ku6.allyes.com
127.0.0.1 ku6afp.allyes.com
127.0.0.1 pq.stat.ku6.com
127.0.0.1 st.vq.ku6.cn
127.0.0.1 stat0.888.ku6.com
127.0.0.1 stat1.888.ku6.com
127.0.0.1 stat2.888.ku6.com
127.0.0.1 stat3.888.ku6.com
127.0.0.1 static.ku6.com
127.0.0.1 v0.stat.ku6.com
127.0.0.1 v1.stat.ku6.com
127.0.0.1 v2.stat.ku6.com
127.0.0.1 v3.stat.ku6.com
#激动网
127.0.0.1 86file.megajoy.com
127.0.0.1 86get.joy.cn
127.0.0.1 86log.joy.cn
#天线视频
127.0.0.1 casting.openv.com
127.0.0.1 m.openv.tv
127.0.0.1 uniclick.openv.com
#迅雷看看屏蔽：
127.0.0.1 mcfg.sandai.net
127.0.0.1 biz5.sandai.net
127.0.0.1 server1.adpolestar.net
127.0.0.1 advstat.xunlei.com
127.0.0.1 mpv.sandai.net
#google自动更新列表
#google hosts '''

hosts = open ('/tmp/hosts','w')
hosts.write(head+text)
hosts.close()

os.system('mv /tmp/hosts /etc/hosts')




