import java.util.*;
/**
자바로 푼 버전
파이썬의 max(map(len,dic.values()))를 직접 구현해야하는 점.
ArrayList일때는 인덱스로 접근 못하고 get함수로 접근해야하는 점.

for each 구문을 써야할때를 구분해야하는점 유의하기.
 */
class Solution {
    public int minimumCardPickup(int[] cards) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();

        for (int i = 0; i<cards.length; i++){
            if (map.containsKey(cards[i])){
                ArrayList<Integer> temp = map.get(cards[i]);
                temp.add(i);
                map.put(cards[i],temp);
            }
            else{
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(i);
                map.put(cards[i],temp);
            }
        }
        int maxLength = 0;
        
        int answer = Integer.MAX_VALUE;
        for (ArrayList<Integer> value: map.values()){
            maxLength = Math.max(maxLength,value.size());
        }
        if (maxLength<2) return -1;

        for (ArrayList<Integer> value: map.values()){
            for (int i=0;i<value.size()-1;i++){
                int compare = Math.abs(value.get(i)-value.get(i+1));
                answer = Math.min(answer,compare+1);
            }
        }
        return answer;
    }
}
