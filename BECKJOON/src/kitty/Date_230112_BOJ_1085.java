
import java.util.Scanner;

// BOJ 1085
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();
        System.out.println(check(x, y, w, h));
    }
    public static int check(int a, int b, int c, int d)
    {
        int ans = 9999999;
        for(int i=0; i<=d; i++) {
            int distance = dist(a, b, 0 , i);
            if (ans > distance) {
                ans = distance;
            }
            int distance2 = dist(a, b, c , i);
            if (ans > distance2) {
                ans = distance2;
            }
        }
        for(int i=0; i<=c; i++) {
            int distance = dist(a, b, i , 0);
            if (ans > distance) {
                ans = distance;
            }
            int distance2 = dist(a, b, i , d);
            if (ans > distance2) {
                ans = distance2;
            }
        }
        return ans;
    }
    public static int dist(int x,int y,int z,int w)
    {
        return (int) Math.sqrt(Math.pow(x - z,2) + Math.pow(y - w,2));
    }
}

