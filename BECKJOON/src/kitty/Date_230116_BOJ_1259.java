import java.util.ArrayList;
import java.util.Scanner;

// BOJ 1259
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String s = sc.nextLine();
            if (s.length() == 1 && s.charAt(0) == '0' ) {
                break;
            } else {
                System.out.println(check(s));
            }
        }
    }

    public static String check(String num) {
        int count = 0;
        ArrayList<Character> arr = new ArrayList<>();
        for (int a = 0; a < num.length(); a++)
        {
            arr.add(num.charAt(a));
        }
        for (int i = 0; i < arr.size(); i++)
            if (arr.get(i) == arr.get(num.length() - i - 1))
            {
                count += 1;
            }
        if (count == num.length()){
            return "yes";
        }
        else{
            return "no";
        }
    }
}
