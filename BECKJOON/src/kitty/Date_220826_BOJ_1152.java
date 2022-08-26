/*
 * 단어의 개수
 * https://www.acmicpc.net/problem/1152
 */
package kitty;

import java.util.Scanner;

public class Date_220826_BOJ_1152 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		sc.close();
		String[] arr = s.split(" ");
		int cnt = 0;
		for (int i = 0; i < arr.length; i++) 
		{
			if (arr[i] != "")
			{
				cnt += 1;
			}
		}
		System.out.println(cnt);
	}

}

