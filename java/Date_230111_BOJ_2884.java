import java.util.Scanner;

// BOJ 2884
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        if (M < 45) {
            if (H == 0) {
                H = 23;
            } else {
                H = H - 1;
            }
            M = M + 15;
        }
        else
        {
            M = M - 45;
        }
        System.out.println(H + " " + M);

    }
}
