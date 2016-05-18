name = input("name:")
age=int(input("age:"))
#下行出错 age是数字型，不能与字符串相加
#print("Information of Name "+name+" \nName:"+name+"\nAge:"+age)
print("Information of Name %s \nName:%s\nAge:%s" %(name,name,age))
msg = '''
Information of Name %s
Name:%s
Age:%d
''' %(name,name,age)
print(msg)
msg = '''
Information of Name %s
Name:%s
Age:%d
''' % (name.strip(), name.strip(), age)

print("Strip 去前后字符，默认空格：%s" %msg)