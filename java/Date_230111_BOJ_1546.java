import java.util.ArrayList;
import java.util.Scanner;

// BOJ 1546
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<Integer>();
        ArrayList<Float> arr2 = new ArrayList<Float>();
        int N = sc.nextInt();
        int Max = 0;
        float total = 0F;
        for (int i = 0; i < N; i++)
        {
            int temp = sc.nextInt();
            arr.add(temp);
            if (temp > Max)
            {
                Max = temp;
            }
        }
        for (int j = 0; j < N; j++)
        {
            if (Max == arr.get(j))
            {
                total += 100F;
            }
            else
            {
                float temp = (float) arr.get(j) / Max;
                total += temp * 100F;
            }
        }
        System.out.println(total / (float) N);

    }
}
