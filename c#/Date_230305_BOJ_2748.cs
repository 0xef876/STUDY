using System;
class BOJ {
  static void Main() {
    long f1 = 1;
    long f2 = 1;
    long f3 = 1;
    long number = int.Parse(Console.ReadLine());
    for (int i = 0; i < number-2; i++)
    {
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
    }
  Console.WriteLine(f3);
}
}
