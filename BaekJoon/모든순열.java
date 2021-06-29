import java.util.Scanner;

/*
다음순열 구할 때 1 2 3 4 -> 4 3 2 1로 가는 과정 -> a[i-1]>a[i]로 가야함
그래서 첫번째 while문에선 a[i-1]<a[i]인 튀는 부분을 찾아야 하기때문에 조건이 a[i-1]>a[i]로 해서 false일때를 찾는거고
j에서 swap해줄거 찾을때는 a[i-1]보다 큰걸 찾는거니까 이 경우가 false가 될때이므로
while(i<=j && a[i-1]>a[j]가 조건으로 오게된다.
if문일 경우 true일때 실행이지만 while인 경우 false로 탈출하기때문에 잘 생각하기.
 */
public class 모든순열 {
    public static int n;
    public static int[] a;

    public static boolean next_permutation(int[] a){
        int i=a.length-1;
        while(i>0 && a[i-1]>a[i]){
            i-=1;
        }
        if(i<=0) return false;
        int j=a.length-1;
        while(i<=j && a[i-1]>a[j]){
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
            i++;
            j--;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=i+1;
        }
        for(int i=0;i<n;i++){
            System.out.print(a[i]+" ");
        }
        System.out.print("\n");
        while(next_permutation(a)){
            for(int i=0;i<n;i++){
                System.out.print(a[i]+" ");
            }
            System.out.print("\n");
        }
    }
}
