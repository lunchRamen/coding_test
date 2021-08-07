import java.util.*;
public class BFS스페셜저지 {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        ArrayList<Integer>[] a=new ArrayList[n];
        int[] parent=new int[n];//해당 인덱스의 이전 정점 저장.
        int[] order=new int[n];//순서를 저장.
        boolean[] check=new boolean[n];
        for(int i=0;i<n;i++){
            a[i]=new ArrayList<>();
        }//각 정점들에 연결된걸 양방향 연결.
        for(int i=0;i<n-1;i++){
            int u=sc.nextInt()-1;
            int v=sc.nextInt()-1;
            a[u].add(v);
            a[v].add(u);
        }
        for(int i=0;i<n;i++){
            order[i]=sc.nextInt()-1;
        }//순서를 입력받음. 인덱스체계니까 -1씩해서 저장.
        Queue<Integer> q=new LinkedList<>();
        q.add(0);
        check[0]=true;
        int m=1;
        //q를 만들고, 0을 집어넣음. 1부터 N까지 자연수가 1번씩 등장하는게 규칙이니까 1의 인덱스체계인 0을 넣음.
        //m은 현재 q의 크기를 나타냄. 1개 집어넣었으니까 1.
        for(int i=0;i<n;i++){
            //0~n까지 for문 돌림.
            if(q.isEmpty()){
                System.out.println(0);
                System.exit(0);
            }//q가 비었으면 실패.
            int x=q.remove();
            if(x!=order[i]){
                System.out.println(0);
                System.exit(0);
            }//q의 첫번째 원소를 지우고 x가 i번째 순서가 아니여도 실패.(bfs
            int cnt=0;
            for(int y:a[x]){
                if(check[y]==false){
                    parent[y]=x;
                    cnt+=1;
                    //y는 x를 통해서만 들어갈 수 있는 순서를 정해줌. 그리고 q에 들어갈 원소 1개 추가.
                }
            }//cnt를 0으로 두고 a[x]에 연결된 모든 원소에 대해 방문하지 않은 정점의 경우 해당 정점의 이전 정점을
            //parent[y]=x로 놔서 이전정점 저장 후 cnt+1함.(q의 크기 체크하기위해)
            for(int j=0;j<cnt;j++){//0~cnt에 대해서
                if(m+j>=n || parent[order[m+j]]!=x){
                    //범위검사, 순서 검사
                    System.out.println(0);
                    System.exit(0);
                }
                q.add(order[m+j]);
                check[order[m+j]]=true;
            }
            m+=cnt;
        }
        System.out.println(1);
    }
}
