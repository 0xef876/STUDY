import java.util.HashMap;
import java.util.Scanner;

// BOJ 10809
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        HashMap<Character,Integer> dict = new HashMap<Character,Integer>();
        for(int i = 97; i <123;i++ )
        {
            char ch = (char) i;
            dict.put(ch,-1);
        }
        for(int i = 0; i < s.length(); i++)
        {
            if (dict.get(s.charAt(i)) != -1) // Because Overlap
            {
                continue;
            }
            dict.put(s.charAt(i),i);
        }
        Object[] arr  = dict.values().toArray();
        for(int i = 0; i < arr.length; i++)
        {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
    }
}
