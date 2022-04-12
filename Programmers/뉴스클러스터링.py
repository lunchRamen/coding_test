import copy

def solution(str1, str2):
    answer = 0
    
    arr1=[]
    arr2=[]
    specific="1234567890[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]_"
    
    for i in range(len(str1)-1):
        if str1[i]==" " or (str1[i] in specific):
            continue
        elif str1[i+1]==" " or ("0"<=str1[i+1]<="9") or (str1[i+1] in specific):
            continue
        else:
            arr1.append((str1[i]+str1[i+1]).lower())
            
    for i in range(len(str2)-1):
        if str2[i]==" " or (str2[i] in specific):
            continue
        elif str2[i+1]==" " or ("0"<=str2[i+1]<="9") or (str2[i+1] in specific):
            continue
        else:
            arr2.append((str2[i]+str2[i+1]).lower())
        
    intersect=[]
    union=[]
    
    #교집합
    temp=copy.deepcopy(arr1)
    for elem in arr2:
        if elem in temp:
            temp.remove(elem)
            intersect.append(elem)
    
    #합집합
    union=copy.deepcopy(arr1)
    temp=copy.deepcopy(arr1)
    for elem in arr2:
        if elem not in temp:
            union.append(elem)
        else:
            temp.remove(elem)
    print(union,temp)
    
    if not arr1 and not arr2:
        answer=65536
    else:
        answer=int(len(intersect)/len(union)*65536)
    
    
    return answer