import java.util.*;

/*
순열 비교할때 while문의 값비교가 =도 포함되어야 순열에서 같은값에 대한 처리가 가능하다. 아니면 while문을 못벗어나서
시간초과가 뜸.
 */
public class 차이를최대로 {
    //public static int n;
    //public static int[] a;
    //public static int ans=0;

    public static boolean next_permutation(int[] a){
        int i=a.length-1;
        while(i>0 && a[i-1]>=a[i]){
            i-=1;
        }
        if(i<=0) return false;
        int j=a.length-1;
        while(j>=i && a[i-1]>=a[j]){
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
    public static int calc(int[] a){
        int sum=0;
        for(int i=0;i<a.length-1;i++) {
            sum+=Math.abs(a[i]-a[i+1]);
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n;
        int[] a;
        n=sc.nextInt();
        a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        Arrays.sort(a);
        int ans=0;
        do{
            int temp=calc(a);
            ans=Math.max(ans,temp);
        }while(next_permutation(a));

        System.out.println(ans);
    }
}
