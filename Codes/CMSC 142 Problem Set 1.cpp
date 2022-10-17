/*
  Solve the following problems. And compute for the T(n) of your solutions.

    int reverse(int n) - returns the reverse of n. e.g. n = 103, return 301; n = 1496, return 6941. The use of any auxiliary function from some library is not allowed. The use of a string is also not allowed.

    void reverse(char st[]) - reverses the string st. e.g. st = "dragrace", reversed st = "ecargard"; st = "nodevillivedon", reversed st = "nodevillivedon".

    bool sorted(int A[], int n) - returns true if the array A with size n is sorted in increasing fashion or in decreasing fashion. It returns false otherwise. e.g. A = {10, 8, 7, 7, 2}, return true; A = {1, 17, 19, 43, 53, 53}, return true; A = {3, 23, 10, 17, 15}, return false; A = {4, 4, 4, 4, 4}, return false.

    int remainder(int a, int b) - returns the remainder when a is divided by b without using the modulo, times, and divide operators. Use of any other function from some library is not allowed as well. Implement this RECURSIVELY.
*/

#include <iostream>
#include <string>
#include <cstring>

int reverse_int(int n);
void reverse_str(char st[]);
bool sorted(int A[], int n);
int remainder(int a, int b);


int main (int argc, char *argv[])
{
  char st[] = "HELP ME!";
  reverse_str(st);
  return 0;
}

int reverse_int(int n)
{
  // source: https://www.programiz.com/c-programming/examples/reverse-number
  
  int reversed = 0;

  while( n != 0 )
  {
    reversed = reversed * 10 + (n % 10);
    n /= 10;
  }
  
  return reversed; 
}

void reverse_str(char st[])
{
  for ( int i=strlen(st); i>=0; i--)
  {
    std::cout << st[i];
  }

  std::cout << std::endl;

}

bool sorted(int A[], int n)
{

  return true;
}
