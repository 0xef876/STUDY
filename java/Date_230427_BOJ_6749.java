// BOJ 6749

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int son3 = sc.nextInt();
        int son2 = sc.nextInt();
        int son1 = son2 + son2 - son3;
        System.out.println(son1);
    }
}