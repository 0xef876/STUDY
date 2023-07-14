// BOJ 2023
import java.util.Scanner;

public class Main {
    static int n;
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        DFS(2,1);
        DFS(3,1);
        DFS(5,1);
        DFS(7,1);

    }
    static void DFS(int x,int y)
    {
        if (y == n)
        {
            if (isPrimeNumber(x))
            {
                System.out.println(x);
            }
            return;
        }
        for (int i = 0; i < 10; i++)
        {
            if (i%2 == 0)
            {
                continue;
            }
            if (isPrimeNumber(x * 10 + i))
            {
                DFS(x * 10 + i, y + 1);
            }
        }
    }
    static Boolean isPrimeNumber(int a)
    {
        for (int i = 2; i < a / 2; i++)
        {
            if (a % i == 0)
            {
                return false;
            }
        }
        return true;
    }
}