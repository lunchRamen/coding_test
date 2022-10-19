class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        시뮬레이션 문제
        여기서 키포인트는, '다음 사람을 받을때, 이전사람의 업무를 처리하고 있는지'이다.
        만약 이전사람의 업무를 처리하고있다면, 다음사람이 도착하는시간보다 업무가 끝나는 시간이 크거나 같고(customers[i][0]<=start)
        다음사람이 도착할때 기다리는 사람이 없다면, 다음사람의 (도착시간+업무시간)-도착시간을 하면 된다.

        start란걸 따로 두는 이유는, 끝나는 시간을
        1. 이전 업무가 끝난 시간 + 업무시간으로 할지
        2. 지금 도착한 시간 + 업무시간으로 할지 를 정하는 과정이다.
        이렇게 total_time을 구하고, start는 end로 바꾼 후
        return total_time/len(customers)를 하면 정답이 나온다.
        """
        start = customers[0][0] + customers[0][1]
        total_time = customers[0][1]

        for i in range(1,len(customers)):
            end = 0
            if customers[i][0]<=start:
                end = start+customers[i][1]
            else:
                end = customers[i][0]+customers[i][1]
            total_time += end-customers[i][0]
            start = end
            
        return total_time/len(customers)
