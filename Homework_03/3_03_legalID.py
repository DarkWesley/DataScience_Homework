import re
def is_legal(id_str):
    pattern = '(^\d{15}$)|(^\d{17}([0-9]|x)$)'
    match = re.match(pattern, id_str)
    return match
ID = input("请输入身份证号：")
if is_legal(ID):
    print("身份证号码格式正确！")
else:
    print("身份证号码格式错误！")
