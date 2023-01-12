
import java.util.HashMap;
import java.util.Scanner;
// BOJ 15829
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        String s = sc.next();
        int r = 31;
        long hash = 0;
        long pow = 1;
        int M = 1234567891;
        HashMap<Character,Integer> alpha_dict = make_dict();
        for (int i = 1; i <= x; i++) {
            hash += alpha_dict.get(s.charAt(i-1)) * pow % M;
            pow = pow * r % M;
        }
        System.out.println(hash % 1234567891);

    }
    public static HashMap<Character, Integer> make_dict()
    {
        HashMap<Character,Integer> dict = new HashMap<>();
        String alpha = " abcdefghijklmnopqrstuvwxyz";
        for(int i = 1; i <=26; i++)
        {
            dict.put(alpha.charAt(i),i);
        }
        return dict;
    }
}

