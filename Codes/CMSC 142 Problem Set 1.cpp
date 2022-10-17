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
  std::cout << reverse_int(42069) << std::endl;
  std::cout << reverse_int(103) << std::endl;
  std::cout << reverse_int(1496) << std::endl;
  
  char st[] = "dragrace";
  reverse_str(st);
  char st1[] = "nodevillivedon";
  reverse_str(st1);

  int s[] = {10,8,7,7,2};
  std::cout << sorted(s, 5) << std::endl;
  int s1[] = {1, 17, 19, 43, 53, 53};
  std::cout << sorted(s1, 6) << std::endl;
  int s2[] = {3, 23, 10, 17, 15};
  std::cout << sorted(s2, 5) << std::endl;
  int s3[] = {4, 4, 4, 4, 4};
  std::cout << sorted(s3, 5) << std::endl;
  int s4[] = {10, 18, 71, 71, 224};
  std::cout << sorted(s4, 5) << std::endl;

  std::cout << remainder(49, -7) << std::endl;
  return 0;
}

int reverse_int(int n)
{
  // source: https://www.programiz.com/c-programming/examples/reverse-number
  
  int reversed = 0; // T(n) = 1

  while( n != 0 ) // n+1
  {
    reversed = reversed * 10 + (n % 10); // T(n) = 4
    n /= 10; // n = n / 10; T(n) = 2
  }
  
  return reversed; // T(n) = 1
} // T(n) = 3 + 6n + 1 = 6n + 4

void reverse_str(char st[])
{
  for ( int i=strlen(st); i>=0; i-- ) // 
  {
    std::cout << st[i]; // 1
  }
  // CONSTANTS: 1
  // ITERATIONS: 3n
  // FOR LOOP LAST CHECK: 1
} // T(n) = 3n + 2 (not sure if 3n+2 or 3n+3)

bool sorted(int A[], int n)
{
  for ( int i=0; i<=n-1; i++ )
  {
    if ( A[i+1] < A[i] ) 
      return false;
  }
  return true;
  // CONSTANTS: 2
  // ITERATIONS: 4n - 1
  // FOR LOOP LAST CHECK: 1
} // T(n) = 4n + 2

int remainder(int a, int b)
{
  b = b < 0 ? -b : b; // source: https://github.com/lattera/glibc/blob/master/stdlib/abs.c (for absolute values)
  if ( a >= b )
    return remainder(a-b, b);
  return a;
  // CONSTANTS: 3 + 1
  // idk lol
}
