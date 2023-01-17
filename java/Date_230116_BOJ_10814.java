
import java.util.*;

// BOJ 10814
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, String> dict = new HashMap<>();
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int age = sc.nextInt();
            String name = sc.next();
            if (dict.containsKey(age))
            {
                String temp = dict.get(age);
                dict.put(age,temp + "," + name);
            }
            else {
                dict.put(age, name);
            }
        }
        for (Integer i : dict.keySet()) {
            if (dict.get(i).contains(","))
            {
                String[] ans = dict.get(i).split(",");
                for(int j = 0 ; j<ans.length; j++)
                {
                    System.out.print(i+ " ");
                    System.out.println(ans[j]);
                }
            }
            else
            {
                System.out.print(i +" ");
                System.out.println(dict.get(i));
            }
        }



    }
}
