"""
모든 경우의 수를 dic으로 만들어 진행.
2,5,8,0의 경우 같은 숫자를 또 똑같이 누르는 경우도 다뤄줘야함. 이걸 생각못해서 한참을 고민.
"""
def solution(numbers, hand):
    answer = ''
    left_hand="*"
    right_hand="#"
    
    dic=dict()
    
    dic["12"]=1 ;dic["32"]=1
    dic["15"]=2 ;dic["35"]=2
    dic["18"]=3 ;dic["38"]=3
    dic["10"]=4 ;dic["30"]=4
    dic["42"]=2 ;dic["62"]=2
    dic["45"]=1 ;dic["65"]=1
    dic["48"]=2 ;dic["68"]=2
    dic["40"]=3 ;dic["60"]=3
    dic["72"]=3 ;dic["92"]=3
    dic["75"]=2 ;dic["95"]=2
    dic["78"]=1 ;dic["98"]=1
    dic["70"]=2 ;dic["90"]=2
    dic["25"]=1 ;dic["28"]=2 ; dic["20"]=3
    dic["58"]=1 ;dic["50"]=2 ; dic["80"]=1
    dic["*2"]=4;dic['*5']=3;dic["*8"]=2;dic['*0']=1
    dic["#2"]=4;dic['#5']=3;dic['#8']=2;dic['#0']=1
    dic["22"]=0;dic["55"]=0;dic["88"]=0;dic["00"]=0
    
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer+="L"
            left_hand=str(number)
        elif number==3 or number==6 or number==9:
            answer+="R"
            right_hand=str(number)
        else:
            left_finger1=str(number)+left_hand
            left_finger2=left_hand+str(number)
            right_finger1=str(number)+right_hand
            right_finger2=right_hand+str(number)
            
            if left_finger1 in dic:
                left_distance=dic[left_finger1]
            else:
                left_distance=dic[left_finger2]
            
            if right_finger1 in dic:
                right_distance=dic[right_finger1]
            else:
                right_distance=dic[right_finger2]
            
            if left_distance>right_distance:
                answer+="R"
                right_hand=str(number)
            elif left_distance==right_distance:
                if hand=="left":
                    answer+="L"
                    left_hand=str(number)
                else:
                    answer+="R"
                    right_hand=str(number)
            else:
                answer+="L"
                left_hand=str(number)
                    
            
            
    return answer
