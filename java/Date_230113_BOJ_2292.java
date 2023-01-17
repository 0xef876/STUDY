import java.util.Scanner;
// BOJ 2292
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int ans = 1;
        int res = 0;
        for (int i = 1; i <= 1000000000; i++) {
                ans = ans + (6 * (i - 1));
                res += 1;
                if (N <= ans)
                {
                    System.out.println(res);
                    break;
                }

        }
}}
