import re

def solution(new_id):
    answer = ''
    
    #step1
    new_id=new_id.lower()
    print(new_id)
    #step2
    id_regex=re.compile("[a-z0-9._-]")
    temp=""
    for i in new_id:
        if id_regex.match(i):
            temp+=i
    #step3
    while True:
        if ".." in temp:
            temp=temp.replace("..",".")
        else:
            break
    #step4
    if temp[0]==".":
        temp=temp[1:]
    for i in range(len(temp)):
        if i==len(temp)-1:
            if temp[i]==".":
                temp=temp[:i]
    #step5
    if not temp:
        temp+="a"
    #step6
    if len(temp)>=16:
        temp=temp[:15]
    if temp.strip()[-1]==".":
        temp=temp[:-1]
    #step7
    if len(temp)<=2:
        t=temp.strip()[-1]
        while True:
            if len(temp)>=3:
                break
            temp+=t
    
    
            
    
        
    return temp
