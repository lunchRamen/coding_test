import java.util.*;

/*
귤의 크기를 HashMap으로 저장한다.
그리고 귤 크기가 최소가 되게끔 한 상자를 꾸리면 되므로,
values에 대해 역순으로 정렬해서 k를 빼가면서 k가 0이하가 되면 return하게끔.
*/
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        for (int i=0;i<tangerine.length;i++){
            map.put(tangerine[i], map.getOrDefault(tangerine[i],0)+1);
        }
        List<Integer> values = new ArrayList<Integer>(map.values());
        Collections.sort(values,Collections.reverseOrder());
        
        for (Integer value: values){
            answer+=1;
            k-=value;
            if (k<=0) break;
        }
        
        return answer;
    }
}
