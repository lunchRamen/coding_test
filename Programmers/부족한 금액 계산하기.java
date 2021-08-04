class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;

        long res=0;
        for(int i=1;i<=count;i++){
           res+=price*i;
        }
        if(res-money<=0) return 0;
        else return res-money;
    }
}
