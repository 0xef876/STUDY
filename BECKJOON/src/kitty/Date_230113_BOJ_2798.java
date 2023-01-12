
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
// BOJ 2798
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0; i < N; i++)
        {
            int temp = sc.nextInt();
            arr.add(temp);
        }
        Collections.sort(arr);
        //System.out.println(arr);


        int ans = 0;
        for(int i = 0; i < arr.size(); i++){
            for(int j = i+1; j < arr.size(); j++) {
                for (int k = j + 1; k < arr.size(); k++) {
                    int temp = arr.get(i) + arr.get(j) + arr.get(k);
                    if (temp <= M) {
                        if (ans <= temp) {
                            ans = temp;
                        }
                    }
                }
            }
        }
        System.out.println(ans);
    }
}

