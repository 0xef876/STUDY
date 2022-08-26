/*
 * 숫자의 개수
 * https://www.acmicpc.net/problem/2577
 */
package kitty;

import java.util.Scanner;

public class Date_220826_BOJ_2577 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		sc.close();
		
		int res = a * b * c;
		String str = Integer.toString(res);
		String[] s = str.split("");
		int[] arr = {0,0,0,0,0,0,0,0,0,0};
		
		for (int i = 0; i < s.length; i++) {
			int idx = Integer.parseInt(s[i]);
			arr[idx] += 1;
		}
		for (int j = 0; j < arr.length; j++) {
			System.out.println(arr[j]);
		}

	}

}
