/*
// BOJ 2562
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[9];
        int max = 0;
        int max_idx = 0;
        for(int i = 0;i<9;i++)
        {
            int a = sc.nextInt();
            if (a >= max)
            {
                max_idx = i;
                max = a;
            }
            arr[i] = a;

        }
        System.out.println(max);
        System.out.println(max_idx+1);

    }
}
