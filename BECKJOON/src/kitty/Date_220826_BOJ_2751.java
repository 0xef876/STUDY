/*
 * 수 정렬하기 2
 * https://www.acmicpc.net/problem/2751
 */
package kitty;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Date_220826_BOJ_2751 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		int n = sc.nextInt();
		
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			list.add(sc.nextInt());
		}
		Collections.sort(list);
		for(Integer c: list)
		{
			sb.append(c).append("\n");
		}
		System.out.println(sb);
	}

}
