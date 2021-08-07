/*
10X10 보드판을 사용. 정육면체 주사위는 1~6.

주사위를 굴려 나온 수만큼 이동.
주사위를 돌린 결과가 100을 초과한다면 이동 할 수 없음=딱 100인 경우에만 게임이 끝난다.
도착한 칸이 사다리면,사다리를 타고 위로 올라간다.
도착한 칸에 뱀이 있으면,뱀을 타고 아래로 내려간다.
->도착한 칸에 사다리가 있으면 수가 위로 점프, 뱀이면 아래로 점프(증가,감소)

목표:1번칸에서 100번칸까지 최소횟수로 통과.

사실상, 사다리를 타서 최대한 위로 올라간 다음, 뱀이 있는 칸을 피해서 100까지 진입하면 됨.


이 문제에서 키포인트: 뱀과 사다리에 대한 처리.
-> next배열로 해결.
해당 번호에 사다리나 뱀이 달려있지 않았으면 그냥 그 번호로 남겨두고,
                                    있으면 그 번호를 이동 번호로 바꿔줌.
 */

import java.util.*;
public class 뱀과사다리게임 {
    static int ladder;
    static int snake;
    static int[] dist=new int[101];
    static int[] next=new int[101];
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        ladder=sc.nextInt();
        snake=sc.nextInt();
        
        for(int i=1;i<=100;i++){
            next[i]=i;
            dist[i]=-1;
        }
        for(int k=0;k<snake+ladder;k++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            next[x]=y;
            //x로 가면 y로 가야됨.
        }
        dist[1]=0;//1번째 시작:0번 이동.
        Queue<Integer> q=new LinkedList<>();
        q.add(1);
        while(!q.isEmpty()){
            int x=q.remove();
            for(int i=1;i<=6;i++){//주사위 수 따라.
                int y=x+i;
                if(y>100) continue;//100넘으면 넘기고
                y=next[y];//현재 정점+주사위 수를
                if(dist[y]==-1){//방문 안했으면
                    dist[y]=dist[x]+1;//이전 번호까지 방문횟수 +1해서 저장.
                    q.add(y);//q에 add
                }
            }
        }
        System.out.println(dist[100]);
    }
}
