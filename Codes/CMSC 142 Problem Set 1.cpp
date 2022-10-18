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
  std::cout << std::endl;
  char st1[] = "nodevillivedon";
  reverse_str(st1);
  std::cout << std::endl;

  int s[] = {10,8,7,7,2};
  std::cout << "10,8,7,7,2: " << sorted(s, 5) << std::endl;
  int s1[] = {1, 17, 19, 43, 53, 53};
  std::cout << "1, 17, 19, 43, 53, 53: " << sorted(s1, 6) << std::endl;
  int s2[] = {3, 23, 10, 17, 15};
  std::cout << "3, 23, 10, 17, 15: " << sorted(s2, 5) << std::endl;
  int s3[] = {4, 4, 4, 4, 4};
  std::cout << "4, 4, 4, 4, 4: " << sorted(s3, 5) << std::endl;
  int s4[] = {10, 18, 71, 71, 224};
  std::cout << "10, 18, 71, 71, 224: " << sorted(s4, 5) << std::endl;

  std::cout << remainder(41, -7) << std::endl;
  std::cout << remainder(-11, 7) << std::endl;
  return 0;
}

int reverse_int(int n)
{
  // source: https://www.programiz.com/c-programming/examples/reverse-number
  /*
   * CONSTANTS:
   *    int reversed = 0;
   *    return reversed;
   *
   * ITERATED:
   *    n != 0
   *    n % 10
   *    10 + <>
   *    reversed * <>
   *    reversed = <>
   *    n /= 10;
   *
   * EXTRA:
   *    while (n != 0) --- last check
   *
   * T(n) = 2 + 6n + 1
   * T(n) = 6n + 3
   *
   */ 
  
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
    /*
     *
     * CONSTANTS:
     *    int i=strlen(st)
     *
     * ITERATED:
     *    i>=0
     *    i--
     *    std::cout << st[i];
     *
     * EXTRA:
     *    for (i>=0) --- FOR LOOP LAST CHECK
     *    i>=0       --- -1
     *
     * T(n) = 1 + 3n + - 1 + 1
     * T(n) = 3n + 1
     *
    */
  for ( int i=strlen(st); i>=0; i-- ) 
    std::cout << st[i];
} 

bool sorted(int A[], int n)
{
  /*
   *
   * CONSTANTS:
   *    if ( n == 1 )
   *    int sign = 0;
   *    int i=0;
   *    return ( sign == 0 ) ? false : true;
   *      sign == 0
   *
   * ITERATED:
   *    i<n-1;
   *      n-1
   *    i++
   *    if ( sign == 0)
   *    if ( sign < 0 && A[i] > A[i+1] )
   *      sign < 0 && A[i] > A[i+1]
   *        sign < 0
   *        A[i] > A[i+1]
   *          i+1
   *    if ( sign > 0 && A[i] < A[i+1] )
   *      sign > 0 && A[i] < A[i+1]
   *        sign > 0
   *        A[i] < A[i+1]
   *          i+1
   *
   * EXTRA:
   *    sign = A[i] - A[i+1];
   *      A[i] - A[i+1]
   *        i+1
   *    i<n-1;
   *
   * T(n) = 14n + 9
  */

  if ( n == 1 ) return true;

  int sign = 0;

  for ( int i=0; i<n-1; i++ )
  {
    if ( sign == 0)
      sign = A[i] - A[i+1];

    if ( sign < 0 && A[i] > A[i+1] ) 
      return false;
    
    if ( sign > 0 && A[i] < A[i+1] )
      return false;
  }
  
  return ( sign == 0 ) ? false : true; 
 }

int remainder(int a, int b)
{
  /*
   * CONSTANTS:
   *    b == 0
   *    b = <>
   *    b < 0 ?
   *    -b | b
   *    a >= b
   *    a-b
   *    remainder(<>)
   *    return <>
   *
   * T(n) = 8n
   *
   */

  if ( b == 0 )
    exit(1);

  b = b < 0 ? -b : b; // source: https://github.com/lattera/glibc/blob/master/stdlib/abs.c (for absolute values)
  if ( a >= b )
    return remainder(a-b, b);
  return a; // This won't get executed but C++ gcc throws out a warning so I added this (if worse case)

}
