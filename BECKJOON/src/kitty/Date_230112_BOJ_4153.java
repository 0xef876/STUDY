
import java.util.Scanner;

// BOJ 4153
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            if (a ==0 && b==0 && c==0)
            {
                break;
            }

            System.out.println(check(a,b,c));
        }
    }
    public static String check(int x, int y, int z)
    {
        if (x*x == y * y + z * z)
        {
            return "right";
        }
        else if (y*y == x*x + z*z)
        {
            return "right";
        } else if (z * z == x * x + y*y) {
            return "right";
        }
        else return "wrong";
    }
}
