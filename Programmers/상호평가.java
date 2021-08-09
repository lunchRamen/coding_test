
/*
상호평가
코드를 짤 때 중요했던점

2중 for문으로 각 평가지를 다 돌때
평균, 최대점수, 최소점수를 기록해놓고
첫번째 inner for문에서는 평균을 구하기위해 avg에 합을 더하고, 최고점과 최저점을 가르는 조건문을 넣어서 찾아낸다.

이후 나 자신에 대한 평가(scores[i][i] or scores[j][j]가 최고점 혹은 최저점인 경우)를 봤을때,
최고점 혹은 최저점인 내 평가와 같은 점수를 매긴 사람이 있으면 평균을 그대로 구하고,
나 혼자 이 점수를 매겼으면 내 점수를 빼서 평균을 구한다.

그리고 이 외의 경우(내가 매긴 내 점수가 최고점도, 최저점도 아닌경우)도 예외처리를 해줘야 답으로 처리 되었다.
else문에도  똑같은 코드 처리.

이후 String에 점수에 맞는 학점 더해서 처리.
*/

class Solution {
    public String solution(int[][] scores) {
        String answer = "";
        double[] a=new double[scores.length];
        for(int i=0;i<scores.length;i++){
            double avg=0;
            int maxScore=0;
            int minScore=100;
            int self=scores[i][i];
            int cnt=0;
            for(int j=0;j<scores.length;j++){
                avg+=scores[j][i];
                if(maxScore<scores[j][i]) maxScore=scores[j][i];
                if(minScore>scores[j][i]) minScore=scores[j][i];
            }
            if(scores[i][i]==maxScore || scores[i][i]==minScore) {
                for(int j=0;j<scores.length;j++){
                    if(scores[i][i]==scores[j][i] && j!=i) cnt+=1;
                }
                if(cnt==0) {
                    avg=avg-self;
                    avg=avg/(scores.length-1);
                }
                else{
                    avg=avg/scores.length;
                }
            }
            else{
                avg=avg/scores.length;
            }
            a[i]=avg;
        }
        
        for(int i=0;i<scores.length;i++){
            if(a[i]>=90) answer+='A';
            else if(80<=a[i] && a[i]<90) answer+='B';
            else if(70<=a[i] && a[i]<80) answer+='C';
            else if(50<=a[i] && a[i]<70) answer+='D';
            else answer+='F';
        }
        return answer;
    }
}
