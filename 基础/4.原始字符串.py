r"""
python特殊写法
使用r''  r""  来避免转义,忽略字符串中的转移符号
raw_path = r'C:\Users\name\Documents'
"""
# 综合示例：使用多个转义字符
message = "使用多个转义字符   路径是：C:\\Users\\name\\Documents\n注意：\t不要忘记备份！"
print(message)
# 输出：
# 路径是：C:\Users\name\Documents
# 注意：	不要忘记备份！
# 提示：在字符串中使用反斜杠时，若不想转义，可使用原始字符串 r""
""" 如果转义字符太多，一个个加斜杠就很麻烦，所以可以直接r表示原始字符串 """
""" 下面为了打印双引号，所以前后就用单引号来包围字符串，而不用双引号来包围"""
raw_path = r'使用 r""避免转义  C:\Users\name\Documents'  # 使用 r"" 避免转义
print(raw_path)  # 输出: C:\Users\name\Documents
