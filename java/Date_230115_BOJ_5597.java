import java.util.ArrayList;
import java.util.Scanner;
// 5597
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> ans = new ArrayList<>();

        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 1; i <= 28; i++){
            int temp = sc.nextInt();
            arr.add(temp);
        }
        for(int j = 1; j<=30;j++)
        {
            boolean state = false;
            for (int k = 0; k<arr.size();k++)
            {
                if (arr.get(k) == j)
                {
                    state = true;
                    break;
                }
            }
            if (state != true)
            {
                ans.add(j);
            }


        }
        System.out.println(Math.min(ans.get(0),ans.get(1)));
        System.out.println(Math.max(ans.get(0),ans.get(1)));

    }
}
