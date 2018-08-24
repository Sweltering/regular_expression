import re

# 1、验证手机号码，以1开头，第二位可以是34587，后面那9位随意
# phone1 = '12345678901'
# phone2 = '13993683111'
#
# # ret = re.match('1[34587]\d{9}', phone1)
# ret = re.match('1[34587]\d{9}', phone2)
# print(ret.group())


# 2、验证邮箱
# email1 = 'w779060694@163.com'
# email2 = 'ssd323@.com'
#
# # ret = re.match('\w+@[a-z0-9]+\.[a-z]+', email2)
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+', email1)
# print(ret.group())


# 3、验证url
# url = 'https://blog.csdn.net/qq_39530821/article/details/79829024'
# ret = re.match('(http|https|ftp)://[^\s]+', url)
# print(ret.group())


# 4、验证身份证
# id_card = '62220119960305271x'
# ret = re.match('\d{17}[xX0-9]', id_card)
# print(ret.group())


# 5、匹配0-100之间的数字
text1 = '009'
text2 = '34'
text3 = '100'
text4 = '1000'

# ret = re.match('[1-9]\d?$|100$', text1)
# ret = re.match('[1-9]\d?$|100$', text2)
ret = re.match('[1-9]\d?$|100$', text3)
# ret = re.match('[1-9]\d?$|100$', text4)
print(ret.group())