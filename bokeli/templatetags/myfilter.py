# -*- coding:utf-8 -*-
from  django import template
register = template.Library()


# 定义一个将日期中的月份转化为大写的过滤器，入8 转换为八
# @register.filter(name='bbb')
def month_to_upper(key):
    print(key)
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month-1]

# 书册过滤器

register.filter('mo nth_to_upper', month_to_upper)