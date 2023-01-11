
import java.util.Scanner;

// BOJ 2908
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        String new_a = String.valueOf(a);
        String new_b = String.valueOf(b);
        String real_a = "";
        String real_b = "";

        for (int i = 2 ; i >= 0 ; i--)
        {
            real_a = real_a + new_a.charAt(i);
            real_b = real_b + new_b.charAt(i);
        }

        int real_real_a = Integer.valueOf(real_a);
        int real_real_b = Integer.valueOf(real_b);
        System.out.println(Math.max(real_real_a,real_real_b));
    }
}
