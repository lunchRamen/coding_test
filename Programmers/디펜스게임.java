/*
enemy를 순회하면서, n-enemy[i]를 계속 진행했을 떄, n<0이 되는 순간 이전의 i+1를 return.
근데, 그 중 k번을 continue할 수 있다.
이때, 가장 많이 진행할 수 있는 경우를 return.

heapq를 써야한다.(enemy의 길이가 100만이므로, 2중 반복문 안됨.)
-> java에선 PriorityQueue.

설명의 마지막 전제인, 모든 라운드를 막을 수 있는 경우(k>=enemy.length) -> return enemy.length;를 예외처리 먼저 해주고,

start round(answer) = k부터 시작한다.
k개의 무적권을 다 쓴 상태 (enemy[k-1]까지 pq에 넣는다.)로 만들고,
k부터 끝까지 돌면서, pq를 pop시키고, 이 값이 enemy[i]와 비교해서
크면 다시 넣은다음 -=enemy[i]를
작으면 enemy[i]를 add하고 -=temp한다.
이렇게 연산을 하고 난 n의 값이 <0이 되면, break해서 answer를 return하면 됨.
*/
import java.util.*;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        if (k>=enemy.length) return enemy.length;
        int answer = k;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i=0;i<k;i++){
            pq.add(enemy[i]);
        }
        
        for (int i=k;i<enemy.length;i++){
            int temp = pq.remove();
            if (temp>enemy[i]){
                pq.add(temp);
                n-=enemy[i];
            }
            else{
                pq.add(enemy[i]);
                n-=temp;
            }
            if (n<0) break;
            answer+=1;
        }
        
        return answer;
    }
}
