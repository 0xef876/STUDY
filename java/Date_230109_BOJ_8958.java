
/*
//BOJ 8958
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        int count = Integer.parseInt(a);
        for(int k=0;k<count;k++) {
            String n = sc.nextLine();
            int len = n.length();
            int ans = 0;
            int num = 1;
            for (int i = 0; i < len; i++) {
                if (n.charAt(i) == 'O')
                {
                    ans = ans + num;
                    num++;
                }
                else {
                    num = 1;
                }
            }
            System.out.println(ans);
        }
    }
}
