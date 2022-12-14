import java.util.*;
/*
우선순위큐를 길이가 k가 분기가되도록 다룬다.
길이가 k미만인 경우, add poll add의 순서
길이가 k이상인 경우, add poll poll add의 순서.

전자의 경우 poll한걸 answer[i]에 할당.
후자의 경우 두번째 poll한걸 answer[i]에 할당.
왜냐하면, 첫번째 poll한건 명예의 전당에 들지 못한 사람을 내보내는것이기 때문.
*/
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i=0;i<score.length;i++){
            if (pq.size()<k){
                pq.add(score[i]);
                int minNum = pq.poll();
                answer[i]=minNum;
                pq.add(minNum);
            }
            else{
                pq.add(score[i]);
                pq.poll();
                answer[i]=pq.poll();
                pq.add(answer[i]);
            }
            
             
        }
        
        return answer;
    }
}
