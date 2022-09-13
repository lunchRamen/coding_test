class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        엣지케이스 처리하느라 애를 좀 먹었다.
        utf-8에 적합하지 않은 케이스라면, 다 false처리해야되는데 이 조건들이
        1. sequence의 첫 바이트가 10인경우
        2. sequence의 첫 바이트가 1이 5개 이상으로 시작하는 경우
        
        또, data의 길이에 따라 경우를 나눠줘야하는데,
        1. 길이가 1인데, 11이상으로 시작하는 경우 -> false
        
        sequence를 진행하는데, data len을 넘는 경우 -> 적절히 조치.
        만약 1byte sequence의 경우 , +=1 else : +=oneNum으로 해준다.
        
        이정도 처리만 해준다면, 나머지는 그냥 구현 문제.
        """
        idx=0
        flag=True
        
        if len(data)==1:
            binNum=bin(data[0])[2:]
            oneNum=0
            zeroNum = 8-len(binNum)
            binNum = "0"*zeroNum + binNum
            for i in binNum:
                if i == "1":
                    oneNum+=1
                else:
                    break
            if oneNum>=1:
                flag=False
        else:
            while True:
                if not flag:    #utf 규칙을 안지켰을시
                    break
                if idx>=len(data):  #모든 data를 순회했을 시
                    break

                binNum=bin(data[idx])[2:]   #0b를 잘라낸 이진수 변환 문자열
                oneNum=0    #첫번쨰부터 1인 숫자가 몇갠지 확인
                zeroNum = 8 - len(binNum)
                binNum = "0"*zeroNum + binNum
                for i in binNum:
                    if i=='1':
                        oneNum+=1
                    else:
                        break
                if oneNum >= 5:
                    flag = False
                    break
                        
                if oneNum == 1:
                    flag=False
                    break
                    
                dataLen=0
                if idx+oneNum >= len(data):
                    dataLen = len(data)
                else:
                    dataLen = idx+oneNum
                for i in range(idx+1,dataLen): #n-1 byte에 대해서 10으로 시작하는지 확인
                    temp = bin(data[i])[2:]
                    zeroNum = 8-len(temp)
                    temp='0'*zeroNum+temp
                    if temp[:2] =="10":
                        continue
                    else:
                        flag=False
                        break
                        
                if oneNum>0:
                    idx+=oneNum
                else:
                    idx+=1
                
        return flag
