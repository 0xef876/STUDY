/*
 * 수 찾기
 * https://www.acmicpc.net/problem/1920
 */
package kitty;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;

public class Date_220829_BOJ_1920 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int[] arr = new int[N];
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			list.add(sc.nextInt());
		}
		Collections.sort(list);
		int i = 0;
		for(Integer c: list)
		{
			arr[i] = c;
			i++;
		}
		int M = sc.nextInt();
		for (int j = 0; j < M; j++) {
			System.out.println(BinarySearch(arr,sc.nextInt()));
		}
		sc.close();
	}
	public static int BinarySearch(int arr[] , int target)
	{
		    int low = 0;
		    int high = arr.length - 1;
		    int mid;
		    while(low <= high) {
		        mid = (low + high) / 2;
		        if (arr[mid] == target)
		            return 1;
		        else if (arr[mid] > target)
		            high = mid - 1;
		        else
		            low = mid + 1;
		    }
		    return 0;
		}
	}

