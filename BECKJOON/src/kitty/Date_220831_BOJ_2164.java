/*
 * 수 찾기 2
 * https://www.acmicpc.net/problem/2164
 */
package kitty;

import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;

public class Date_220831_BOJ_2164 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		Queue<Integer> q = new LinkedList<Integer>(); //in형 큐 선언
		for (int i = 1; i <= n; i++) {
			q.add(i);
		}
		while(q.size() != 1)
		{
			q.poll();
			q.add(q.poll());
			
		}
		System.out.println(q.peek());
		
		
	}

}
