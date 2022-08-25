/*
 * 별 찍기 - 1
 * https://www.acmicpc.net/problem/2438
 */
package kitty;

import java.util.Scanner;

public class Date_220825_BOJ_2438 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		sc.close();
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < i + 1; j++)
			{
				System.out.print("*");
			}
			System.out.print("\n");
		}
	}

}
