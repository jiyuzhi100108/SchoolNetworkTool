import os
print("欢迎使用校园网调试工具")
print("Yuzhi Ji @ github.com ")   
print("Allowed M.I.T. Opensource Licenses")
print("")
print("")
print("请按照以下提示进行调试：")
print("")
print("1.系统信息")
print("2.IP查询")
print("3.主机扫描")
print("4.校园网连通性测试")
print("5.磁盘检查")
print("6.帮助")
print("")
a=int(input("请输入数字1~6进行选择："))
if a==1:
    one=os.popen('systeminfo')
    print("one.read():{}\n".format(one.read()))
elif a==2 :
    two=os.popen('ipconfig')
    print("two.read():{}\n".format(two.read()))
elif a==3 :
    three=os.popen('arp -a')
    print("three.read():{}\n".format(three.read()))
elif a==4 :
    print("1.检测连通")
    print("2.持续连接")
    b=int(input("请输入1~2进行选择："))
    if b==1 :
        abcone=os.popen('ping 172.21.80.222')
        print("abcone.read():{}\n".format(abcone.read()))
    if b==2 :
        abctwo=os.popen('ping 172.21.80.222 -l -t')
        print("abctwo.read():{}\n".format(abctwo.read()))   
elif a==5 :
    five=os.popen('chkdsk')
    print("five.read():{}\n".format(five.read()))   
elif a==6 :
    print("有任何疑问请联系jiyuzhi1001081@outlook.com或在github地址git@github.com:jiyuzhi100108/SchoolNetworkTool.git中提交Issues")    
else :
    print("请正确输入1~6")     