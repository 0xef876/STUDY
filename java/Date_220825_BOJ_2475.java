/*
 * 검증수
 * https://www.acmicpc.net/problem/2475 
 */

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		int e = sc.nextInt();
		sc.close();
		int s = a*a + b*b + c*c + d*d + e*e;
		System.out.println(s%10);
	}

}
