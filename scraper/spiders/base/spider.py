# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider

from .. import api


# Module API

class Spider(CrawlSpider, api.Spider):

    # Public

    pass
