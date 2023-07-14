/*
 * 숫자의 합
 * https://www.acmicpc.net/problem/11720
 */
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s = sc.next();
		sc.close();
		int res = 0;
		for (int i = 0; i < n; i++) {
			res += s.charAt(i) - '0';
		}
		System.out.println(res);
	}

}
