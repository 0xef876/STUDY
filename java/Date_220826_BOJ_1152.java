/*
 * 단어의 개수
 * https://www.acmicpc.net/problem/1152
 */

import java.util.Scanner;

public class Main {

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

