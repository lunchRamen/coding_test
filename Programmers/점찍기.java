/*
"원점과 거리"가 d이하인 x,y좌표의 경우의 수를 return하는 문제.
원점과의 거리가 일정한 집합 = 원.
x**2 + y**2 <= d**2
-> 0~d까지 범위를 x로 대입하고, y에 대해 방정식을 세워서 y의 갯수를 answer에 더해주는 방식으로 푼다.
해당 y의 갯수 또한 k의 간격으로만 존재하므로 Math.floor(y/k)+1씩 더해주면 된다.
*/
class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        
        for (int i=0;i<=d;i+=k){
            int y = (int)Math.sqrt(Math.pow(d,2)-Math.pow(i,2));
            answer += Math.floor(y/k)+1;
        }
        return answer;
    }
}
