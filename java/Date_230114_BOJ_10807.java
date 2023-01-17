import java.util.ArrayList;
import java.util.Scanner;

// 10807
public class Main {
    public static void main(String[] args){
        int cnt = 0;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0; i<N;i++)
        {
            arr.add(sc.nextInt());
        }
        int V = sc.nextInt();
        for(int j = 0; j < arr.size(); j++)
        {
            if (arr.get(j) == V) {
                cnt += 1;
            }
        }
        System.out.println(cnt);

    }
}
