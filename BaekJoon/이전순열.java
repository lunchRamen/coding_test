import java.util.Scanner;
/*
다음순열 조건 반대로
a[i-1]>a[i]될때까지 i-=1;
a[j]<a[i-1]될때까지 j-=1; a[i-1]보다 작은 값을 찾아서 바꿔주고, i~n-1까지 순열 역순 배치.

순열을 구하는 조건 flow
a[i-1]과 a[i]의 대소관계 만족하는 가장 큰 i를 찾음.
j>=i && a[j] a[i-1]의 대소관계 만족하는 가장 큰 j를 찾음.
->가장 큰 i혹은 j를 찾는다? 그냥 찾으면 그걸로 끝.
a[i-1]과 a[j]를 swap
a[i]~a[n-1]까지 배열을 역순 배치.
 */
public class 이전순열 {
    public static int n;
    public static int[] a;
    static boolean prev_premutation(int[] a){
        int i=a.length-1;
        while(i>0 && a[i-1]<a[i]){
            i-=1;
        }
        if(i<=0) return false;
        int j=a.length-1;
        while(i<=j && a[j]>a[i-1]){
            j-=1;
        }
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
        Scanner sc= new Scanner(System.in);
        n=sc.nextInt();
        a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        if(prev_premutation(a)){
            for(int i=0;i<a.length;i++){
                System.out.print(a[i]+" ");
            }
        }
        else System.out.println(-1);
    }
}
