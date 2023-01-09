/*
// BOJ 10818
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        int M = -1000000; // max
        int N = 1000000; // min
        while(count != n)
        {
            int a = sc.nextInt();
            if (M <= a){
                M = a;
            }
            if (N >= a)
            {
                N=a;
            }
            count++;
        }
        System.out.print(N);
        System.out.print(" ");
        System.out.println(M);

    }
}
