import requests
import os
def details(name):
    k=name
    result= requests.get('http://api.hackertarget.com/whois/?q='+k)
    k=result.text
    print(k)
def trace(name):
    command = "tracert " + name
    process = os.popen(command)
    result = str(process.read())
    return result


print("enter \n1 for details\n2 for trace ")
i=int(input())
if i==1:
    details(input("enter ip or domain :"))
elif i==2:
    trace(input("enter ip or domain name :"))
