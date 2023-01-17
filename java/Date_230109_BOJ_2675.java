/*
// BOJ 2675
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;
        for (int i = 0; i < n * 2; i++) {
            String ans = "";
            String s = sc.next();
            if (i % 2 == 0) {
                a = Integer.parseInt(s);
            } else {
                for (int j = 0; j < s.length(); j++) {
                    for (int k = 0; k < a; k++) {
                        System.out.print(s.charAt(j));
                    }
                }
                System.out.println();
            }
        }
    }
}
