import java.util.*;
/*
각 문자열에서 두번 이상 등장하는 문자에 대해서 같은 두 문자의 거리를 answer[idx]에 저장하여
answer를 return하는 문제.
*/
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        
        HashMap<Character,Integer> dic = new HashMap<>();
        
        for (int i=0;i<s.length();i++){
            if (!dic.containsKey(s.charAt(i))){
                answer[i]=-1;
                dic.put(s.charAt(i),i);
            }
            else{
                answer[i] = i - dic.get(s.charAt(i));
                dic.put(s.charAt(i),i);
            }
        }
        return answer;
    }
}
