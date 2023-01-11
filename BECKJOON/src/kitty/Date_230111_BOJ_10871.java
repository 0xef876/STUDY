// BOJ 10871
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();

        for (int i = 0; i < N; i++)
        {
            int a = sc.nextInt();
            if (a < X)
            {
                System.out.print(a);
                System.out.print(" ");
            }
        }
    }
    }
