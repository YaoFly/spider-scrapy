#!/usr/bin/python

from scrapy import cmdline
cmdline.execute("scrapy crawl sczx -o swfurl-wedding.json".split())