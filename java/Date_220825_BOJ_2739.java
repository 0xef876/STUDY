/*
 * 구구단
 * acmicpc.net/problem/2739
 */

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		sc.close();
		for (int i = 1; i < 10; i++)
		{
			System.out.printf("%d * %d = %d\n",a,i,a*i);
		}
	}

}
