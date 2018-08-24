# 正则表达式常用匹配规则
# 以下匹配都是匹配多个字符
import re

# 1、*   匹配0个或者任意多的字符，没有匹配空白
# text = '12ab'
# ret = re.match('\d*', text)
# print(ret.group())


# 2、+   匹配1个或者任意多的字符，没有返回None，
# text = '12ab'
# # ret = re.match('\d+', text)
# # print(ret.group())


# 3、?   匹配1个或者0个
# text = '12ab'
# ret = re.match('\d?', text)
# print(ret.group())


# 4、{m} 匹配m个字符
# text = '123a3b'
# ret = re.match('\d{3}', text)
# print(ret.group())


# 5、{m,n}  匹配m-n个字符
# text = '12a3b'
# ret = re.match('\d{1,5}', text)
# print(ret.group())


# 6、\   转义字符
# text = 'apple price is $399'
# ret = re.search('\$\d+', text)
# print(ret.group())


# 7、原生字符串
text1 = '\\n'
text2 = r'\n'
print(text1)
print(text2)
