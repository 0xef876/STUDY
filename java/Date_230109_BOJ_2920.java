/*
// BOJ 2920
*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ans1 = "ascending";
        String ans2 = "descending";
        String ans3 = "mixed";
        boolean state1 = true;
        boolean state2 = true;
        boolean state3 = true;
        int temp = 0;
        for (int i=0; i<8;i++)
        {
            int a = sc.nextInt();
            if (i != 0)
            {
                if (a > temp)
                {
                    state2 = false;
                }
                else if (a < temp)
                {
                    state1 = false;
                }
            }
            temp = a;

        }
        if (state1 != state2)
        {
            state3 = false;
        }

        if(state1)
        {
            System.out.println(ans1);
        }
        else if (state2)
        {
            System.out.println(ans2);
        }
        else if (state3)
        {
            System.out.println(ans3);
        }
    }
}
