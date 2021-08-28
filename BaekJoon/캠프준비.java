/*
기존에 생각했던 방법
main함수에서 for문을 돌려서 a[i]를 시작점으로 한 go 재귀함수 구현
->결과적으로 내가 원하는 답이 첫번째 케이스 외엔 제대로 구현이 안됨.

->강사님 코드를 보고 이해한 점
생각 자체는 비슷했다. 다만 방문 여부를 따져주면 따로 ArrayList로 함수를 넣고 빼고 할 필요 없이
a배열과 c배열 두개로만 재귀 여부와 sum이 l보다 크고 r보다 작은지, 최대-최소가 x보다 큰지 알 수 있으며
객체를 담는 Collections를 안쓰는 가장 큰 장점인 재귀로 넘길때 배열 정보가 공유되지 않는 장점을 제대로 사용한 케이스.
아마 나는 ArrayList에 a[i]에 대한 원소를 담고 출발해서 제대로 된 정답이 안나왔던 듯.

그래서 똑같은 go(idx+1) 재귀의 경우에도
c[idx]=true;하고 go(idx+1)하고
c[idx]=false;하고 go(idx+1)하면
첫번째 재귀가 돌때는 idx번째 원소를 방문했다고 알고 돌고, 두번째 재귀에서는 idx번재 원소 방문을 안한 상태로 돌게된다.
->기본 자료형 배열을 사용했을때 가장 큰 장점. 객체를 담는 자료구조들은 해당 자료구조의 상태가 재귀를 하더라도
항상 공유되어 업데이트 된다.
 */

import java.util.*;
public class 캠프준비 {
    static int n;
    static int l;
    static int r;
    static int x;
    static int[] a=new int[15];
    static boolean[] c=new boolean[15];
    static int go(int idx){
        if(idx==n){
            int cnt=0;
            int sum=0;
            int hard=-1;
            int easy=-1;
            for(int i=0;i<n;i++){
                if(c[i]==false) continue;
                cnt+=1;
                sum+=a[i];
                if(hard==-1 || hard<a[i]) hard=a[i];
                if(easy==-1 || easy>a[i]) easy=a[i];
            }
            if(cnt>=2 && sum>=l && sum<=r && hard-easy>=x) return 1;
            else return 0;
        }
        c[idx]=true;
        int cnt1=go(idx+1);
        c[idx]=false;
        int cnt2=go(idx+1);
        return cnt1+cnt2;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        l=sc.nextInt();
        r=sc.nextInt();
        x=sc.nextInt();

        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        System.out.println(go(0));
    }
}
