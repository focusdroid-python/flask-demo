# -*- coding:utf-8 -*-

import re
from parse_url import parse_url


url = "http://36kr.com"

html_str = parse_url(url)

ret = re.findall("<script>var props=(.*?)</script>", html_str)

print(ret)
