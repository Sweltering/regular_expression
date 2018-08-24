# 正则表达式中常用的函数
import re

# 1、match函数
# 从头开始匹配，如果匹配不到，就返回None


# 2、search函数
# 从全局进行匹配，如果匹配不到返回None


# 3、group函数
# ()    分组匹配
# phone = 'apple price is $299, oppo price id $199'
# ret = re.search('.*(\$\d+).*(\$\d+)', phone)
# print(ret.group())  # apple price is $299, oppo price id $199
# print(ret.group(1))  # $299
# print(ret.group(2))  # $199
# print(ret.group(1, 2))  # ('$299', '$199')
# print(ret.groups())  # ('$299', '$199')


# 4、findall函数
# 找出所有满足条件的，返回一个列表
# phone = 'apple price is $299, oppo price id $199'
# ret = re.findall('\$\d+', phone)
# print(ret)  # ['$299', '$199']


# 5、sub函数
# 替换字符串，将匹配到的字符串替换为其他字符串
# phone = 'apple price is $299, oppo price id $199'
# ret = re.sub('\$\d+', '0', phone)
# print(ret)  # apple price is 0, oppo price id 0

# 获取拉钩网中的职位文本信息
# html = """
# <div>
#         职位职责：
# <br>1、负责今日头条商业变现产品后台服务的设计、开发、优化等研发工作，保证产品的质量和开发进度；
# <br>2、负责客户增长相关技术的设计与实现；
# <br>3、研究新兴技术，对产品进行持续优化。
# <br>
# <br>职位要求：
# <br>1、本科及以上学历，计算机相关专业，基础知识扎实；
# <br>2、聪明，学习能力强，有独立解决问题的能力；
# <br>3、熟悉面向对象编程，掌握java/c++/python/php中的至少一门语言；
# <br>4、良好的编程习惯，追求极致的代码品质，熟悉常用设计模式和一般项目的开发流程；
# <br>5、开朗上进，积极沟通，善于团队协作。
#         </div>
# """
# ret = re.sub('<.+?>', "", html)
# print(ret)


# 6、spilt函数
# 使用正则表达式来分割字符串，返回一个列表
# text = 'hello&word ni hao'
# # ret = re.split(' |&', text)
# ret = re.split('[^a-zA-Z]', text)
# print(ret)


# compile函数
# 对于一些经常要用到的正则，可以使用compile进行编译，后期使用的时候，直接拿过来用，执行效率会更快
text = 'the number is 20.50'
# r = re.compile('\d+\.?\d*')
r = re.compile(r"""
    \d+  # 小数点前面的数字，至少一位
    \.?  # 小数点本身，非贪婪
    \d*  # 小数点后面的数字，可以没有
""", re.VERBOSE)
ret = re.search(r, text)
print(ret.group())
