import java.util.HashSet;
import java.util.Scanner;

// BOJ 3052
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> s = new HashSet<Integer>();
        for (int i = 0 ; i < 10; i++)
        {
            int N = sc.nextInt();
            s.add(N % 42);
        }
        System.out.println(s.size());

    }
}
