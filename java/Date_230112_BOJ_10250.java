import java.util.HashMap;
import java.util.Scanner;

// BOJ 10250
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int TestCase = sc.nextInt();
        for (int i = 0; i < TestCase; i++) {
            int height = sc.nextInt();
            int width = sc.nextInt();
            int N = sc.nextInt();
            int ans = check(height,width,N);
            System.out.println(ans);
        }
    }
    public static int check(int H, int W, int N)
    {
        HashMap<Integer,Integer> dict = new HashMap<Integer,Integer>();
        for(int i = 1; i < W + 1; i++) {
            for (int j = 1; j < H + 1; j++) {
                dict.put(j + (H * (i-1)),j*100+i);
            }
        }
        return dict.get(N);
    }
}
