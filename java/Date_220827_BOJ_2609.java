/*
 * 최대공약수와 최소공배수
 * https://www.acmicpc.net/problem/2609
 */
package kitty;

import java.util.Scanner;

public class Date_220827_BOJ_2609 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		sc.close();
		gcd_print(a,b);
		lcm_print(a,b);
	}
	public static void gcd_print(int x,int y)
	{
		int gcd = 0;
		if (x>y)
		{
			for (int i = 1; i <= y; i++) {
				if (y % i == 0 && x % i == 0)
				{
					gcd = i;
				}
			}
		}
		else
		{
			for (int i = 1; i <= x; i++) {
				if (y % i == 0 && x % i == 0)
				{
					gcd = i;
				}
			}
		}
		System.out.println(gcd);
	}
	public static void lcm_print(int x, int y)
	{
		int lcm = 0;
		if (x>y)
		{
			for(int i=1; i<=x; i++)
			{
				if ((y * i) % x == 0)
				{
					lcm = y*i;
					break;
				}
			}
		}
		else
		{
			for(int i=1; i<=y; i++)
			{
				if ((x * i) % y == 0)
				{
					lcm = x*i;
					break;
				}
			}
		}
		System.out.println(lcm);
	}

}
