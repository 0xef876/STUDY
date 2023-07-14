/*
 * 소수 찾기
 * https://www.acmicpc.net/problem/1978
 */

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int cnt = 0;
		for (int i = 0; i < arr.length; i++) {
			boolean TF = false;
			arr[i] = sc.nextInt();
			if (arr[i] == 1)
			{
				TF = true;
			}
			for (int j = 2; j < arr[i]; j++) {
				if (arr[i] % j == 0)
				{
					TF = true;
					break;
				}
			}
			if (TF == false)
			{
			cnt += 1;
		
			}
		}
		sc.close();
		System.out.println(cnt);
	}

}
