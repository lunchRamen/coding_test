class Solution:
    def intToRoman(self, num: int) -> str:
        answer=""
        """
        구현문젠데, 그냥 쌩노가다로 풀었음.
        중요한 조건문은
        1~3, 4, 5, 6~9 가 10단위,100단위까지 따져줘야한다는 것.
        범위가 3999까지기때문에 1000단위는 무조건 M*1000단위 수 여서
        일의자리 십의자리 백의자리만 위의 분기문을 태워주면 된다.
        속도는 가장 빠름.
        """
        start = 1
        before = 0
        while True:
            if start>num:
                break
            temp = (num-before)%(start*10)
            if temp<=9:
                if 1<=temp<=3:
                    answer="I"*temp+answer
                elif temp == 4:
                    answer="IV"+answer
                elif 5<=temp<=8:
                    answer="V"+"I"*(temp-5)+answer
                elif temp==9:
                    answer="IX"+answer
            elif 10<=temp<=90:
                if 10<=temp<=30:
                    answer="X"*(temp//10)+answer
                elif temp==40:
                    answer="XL"+answer
                elif 50<=temp<=80:
                    answer="L"+"X"*((temp-50)//10)+answer
                elif temp==90:
                    answer="XC"+answer
            elif 100<=temp<=900:
                if 100<=temp<=300:
                    answer="C"*(temp//100)+answer
                elif temp==400:
                    answer="CD"+answer
                elif 500<=temp<=800:
                    answer="D"+"C"*((temp-500)//100)+answer
                elif temp==900:
                    answer="CM"+answer
            elif 1000<=temp:
                answer="M"*((temp)//1000) + answer
            before+=temp
            start*=10
        return answer
