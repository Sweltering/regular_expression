# 正则表达式常用匹配规则
# 以下匹配都是匹配单个字符
import re

# 1、匹配某个字符串
# text = 'ahello'
# ret = re.match('he', text)  # 返回None, 从头开始匹配
# ret = re.search('he', text)  # 全局匹配
# ret = re.match('ah', text)
# print(ret.group())


# 2、.  匹配任意字符，只匹配一个字符，匹配不到换行符
# text = 'hello'
# ret = re.match('.', text)
# text = '\nhello'
# # ret = re.match('.', text)  # 返回None
# print(ret.group())


# 3、\d或者[0-9]  匹配任意的数字（0-9）,只匹配一个
# text = '123'
# # ret = re.match('\d', text)
# # print(ret.group())


# 4、\D或者[^0-9]  匹配任意的非数字, 只匹配一个
# text = '+abc+'
# ret = re.match('\D', text)
# print(ret.group())


# 5、\s  匹配任意的空白字符(\n, \t, \r, 空格)
# text = ' \r'
# ret = re.match('\s', text)
# print(ret.group())


# 6、\w或者[0-9a-zA-Z_]  匹配的是a-z、A-Z、数字、下划线
# text = 'SA'
# ret = re.match('\w', text)
# print(ret.group())


# 7、\W或者[^0-9a-zA-Z_]]  与\w相反
# text = '++'
# ret = re.match('\W', text)
# print(ret.group())


# 8、[]  组合的方式，满足中括号中的任意字符，就可以匹配
# text = '0936-43242342342abcd'
# ret = re.match('[\d-]', text)
# print(ret.group())


# 9、^   表示以...开始
# text = 'hello'
# ret = re.search('^h', text)
# print(ret.group())


# 10、$  表示以...结尾
# text = 'xxx@163.com'
# ret = re.match('\w+@163.com$', text)
# print(ret.group())


# 11、|  匹配多个字符串或者表达式
# text = 'httpsdsds'
# ret = re.match('^(ftp|http|https)', text)
# print(ret.group())


# 12、贪婪模式
# text = '231232131'
# ret = re.match('\d+', text)
# print(ret.group())

# 13、?  非贪婪模式
# text = '231232131'
# ret = re.match('\d+?', text)
# print(ret.group())

text = '<h1>标题<h1>'
ret = re.match('<.+?>', text)
print(ret.group())
