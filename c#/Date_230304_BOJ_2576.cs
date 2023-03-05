using System;
class BOJ {
  static void Main() {
      int ans = 0;
      int min = 99999;
      for (int i = 1; i <= 7; i++) // 7번 반복
      {
    int number = int.Parse(Console.ReadLine());
    if(number % 2 != 0)
    {
        if (min > number)
        {
            min = number;
        }
        ans = ans + number;
    }
      }
      if (ans == 0)
      {
        Console.WriteLine(-1);
      }
      else{
          Console.WriteLine(ans);
          Console.WriteLine(min);
          
      }
  }
}
