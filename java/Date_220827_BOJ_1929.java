/*
 * 소수 구하기
 * https://www.acmicpc.net/problem/1929
 */
package kitty;

import java.util.Scanner;

public class Date_220827_BOJ_1929 {
	
	public static boolean[] array;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		sc.close();
		array = new boolean[N+1];
		check();
		for(int i=M; i<= N;i++)
		{
			if (array[i] != true)
			{
				System.out.println(i);
			}
		}
	}
	public static void check() { // 에라토스테네스의채 알고리즘
		array[0] = array[1] = true;
		for (int i = 2; i <= Math.sqrt(array.length); i++) {
			if (array[i]) continue;
			for (int j = i*i; j < array.length; j += i) {
				array[j] = true;
			}
		}
		
	}

}
