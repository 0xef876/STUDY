/*
 * 설탕 배달
 * https://www.acmicpc.net/problem/2839
 */
package kitty;

import java.util.Scanner;

public class Date_220831_BOJ_2839 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.close();
		System.out.println(function(N));
	}
	public static int function(int n)
	{
		while (n != 0)
		{
			int mok = n / 5;
			int na = n % 5;
			if (na % 3 == 0 && na != 0)
			{
				return mok + 1;
			}
			else if (na == 0)
			{
				return mok;
			}
			else
			{	
				int i = 1;
				while(mok - i >= 0)
				{
					int j = (n - (5 * (mok - i)));
					if (j % 3 == 0)
					{
						return (j / 3) + (mok - i);
					}
					else
					{
						i++;
					}
				}
			}
			break;
		}
		return -1;
	}
}