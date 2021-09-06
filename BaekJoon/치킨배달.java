import java.util.*;
class Pair{
    int first;
    int second;
    Pair(int f,int s){
        this.first=f;
        this.second=s;
    }
}
public class 치킨배달 {
    static int n,m;
    static int[][] a;
    static boolean next_permutation(int[] a){
        int i=a.length-1;
        while(i>0 && a[i-1]>=a[i]) i-=1;

        if(i<=0) return false;

        int j=a.length-1;
        while(j>i && a[j]<=a[i-1]) j-=1;

        int temp=a[i-1];
        a[i-1]=a[j];
        a[j]=temp;

        j=a.length-1;
        while(i<j){
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i+=1;
            j-=1;
        }
        return true;

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();//도시 크기
        m=sc.nextInt();//남길 치킨집 갯수.
        int[][] a=new int[n][n];
        ArrayList<Pair> people =new ArrayList<>();
        ArrayList<Pair> store=new ArrayList<>();
        //0:빈칸 1:집 2:치킨집이니까
        //입력받은 a[i][j]중 1이면 people에 x,y좌표 더하고 2면 store에 더함.

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                a[i][j]=sc.nextInt();
                if(a[i][j]==1){
                    people.add(new Pair(i,j));
                }
                if(a[i][j]==2){
                    store.add(new Pair(i,j));
                }
            }
        }
        //그다음, 가게의 갯수만큼 d를 만듬.
        int[] d=new int[store.size()];
        for(int i=0;i<m;i++){
            d[i]=1;
        }
        //d배열 자체는 가게의 갯수만큼 배정해놓고 다 0으로 초기화 되어있음.
        //근데 m(남길 치킨집의 갯수)만큼만 1로 바꿈
        //->110000 이런 상태로 있는걸 모두 순열을 돌림
        //->결과적으로 d배열은 남길치킨집 m개의 대해 선택하고 순열을 돌려 모든 경우의 치킨집을
        //남기는것에 대해 확인하는 용도.

        Arrays.sort(d);
        //000011이렇게 되어있음. 이래야 순열을 돌릴수 있다( 1234 1243.. 이런식이니까)
        int ans=-1;
        do{
            int sum=0;
            for(Pair p:people){//모든 people ArrayList에대해
                int min=-1;//최소값 설정
                for(int i=0;i<store.size();i++){//"가게의 갯수"만큼 for문을 돌림
                    if(d[i]==0) continue;//0이면 볼필요 없음 d[i]=1인 경우가 남길 치킨집이니까.
                    Pair s=store.get(i);//d[i]가 1인 곳의 가게좌표를 가져옴
                    int d1=p.first-s.first;//모든 집들에 대해 가게와의 거리를 구함
                    int d2=p.second-s.second;
                    if(d1<0) d1=-d1;
                    if(d2<0) d2=-d2;
                    int dist=d1+d2;
                    if(min==-1 || min>dist) min=dist;//모든 집들에 대해 가게와의 거리를 구한 합이
                    //최소라면, 최소를 갱신해준다.
                    //이중 for문을 돌리는 이유
                    //모든 집에 대해 모든 치킨집의 거리를 돌려서, 가장 가까운 치킨집의 거리를
                    //sum에 더해주기 위해서 거리와 min을 비교하는 if문이 존재.
                    //그럼 min에 있는 값은 각 집에 대해 가장 가까운 치킨집의 거리가 있게됨.
                }
                sum+=min;//이 최소를 합계에 더해줌.
            }
            if(ans==-1 || ans>sum) ans=sum;//이 합계를 ans와 비교해서 작으면 갱신해줌.

        }while(next_permutation(d));

        System.out.println(ans);
    }
}
