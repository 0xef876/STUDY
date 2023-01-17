/*
// BOJ 10950
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;
        while(count != n)
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(a+b);
            count++;
        }
    }
}
