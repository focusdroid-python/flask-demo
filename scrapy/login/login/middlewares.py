# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        ua = random.choice(spider.settings.get("USER_AGENTS_LISTS"))
        request.headers["User-Agent"] = ua


class CheckUserAgent:
    def process_response(self, request, response, spider):
        # print(dir(response.request))
        print(request.headers["User-Agent"])
        return response
