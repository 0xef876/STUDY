import java.util.HashMap;
import java.util.Scanner;

// BOJ 1157
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        a = a.toUpperCase();
        int Max = 0;
        int Overlap = 0;
        char ans = 'A';
        HashMap<Character,Integer> dict = new HashMap<Character, Integer>();
        for (int i = 65; i < 91; i++) {
            char ch = (char) i;
            dict.put(ch, 0);
        }

        for (int i = 0; i < a.length(); i++)
        {
            int count = dict.get(a.charAt(i));
            dict.put(a.charAt(i),count+1);
        }
        for (char i : dict.keySet())
        {
            if (Max < dict.get(i))
            {
                Max = dict.get(i);
                Overlap = 0;
                ans = i;
            }
            else if (Max == dict.get(i))
            {
                Overlap++;
            }
        }

        if (Overlap >= 1) {
            System.out.println("?");
        }
        else
        {
            int num = (int) ans;
            char result = (char) num;
            System.out.println(result);
        }
    }
}
