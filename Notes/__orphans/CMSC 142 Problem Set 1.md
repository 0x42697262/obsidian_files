
# Solve the following problems. And compute for the T(n) of your solutions.

### int reverse(int n) - returns the reverse of n. e.g. n = 103, return 301; n = 1496, return 6941. The use of any auxiliary function from some library is not allowed. The use of a string is also not allowed.
```c++
int reverse_int(int n)
{
  int reversed = 0;
  while( n != 0 ) 
  {
    reversed = reversed * 10 + (n % 10); 
    n /= 10; 
  }  
  return reversed; 
}
```
$$T(n) = \sum_{0}^{n}{6+3} = 6(n-1-0+1)+3$$
$$T(n) = 6n+3$$


### void reverse(char st\[\]) - reverses the string st. e.g. st = "dragrace", reversed st = "ecargard"; st = "nodevillivedon", reversed st = "nodevillivedon".
```c++
void reverse_str(char st[])
{
  for ( int i=strlen(st); i>=0; i-- ) 
    std::cout << st[i];
} 
```
$$T(n) = \sum_{0}^{n-1}{5+3} = 5(n-1-0+1)+3$$
$$T(n) = 5n+3$$


### bool sorted(int A\[\], int n) - returns true if the array A with size n is sorted in increasing fashion or in decreasing fashion. It returns false otherwise. e.g. A = {10, 8, 7, 7, 2}, return true; A = {1, 17, 19, 43, 53, 53}, return true; A = {3, 23, 10, 17, 15}, return false; A = {4, 4, 4, 4, 4}, return false.
```c++
bool sorted(int A[], int n)
{
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
```
$$T(n) = \sum_{0}^{n-1}{14+9} = 14(n-1-0+1)+9$$
$$T(n) = 14n + 9$$

### int remainder(int a, int b) - returns the remainder when a is divided by b without using the modulo, times, and divide operators. Use of any other function from some library is not allowed as well. Implement this RECURSIVELY.
```c++
int remainder(int a, int b)
{
  if ( a >= b )
    return remainder(a-b, b);
  return a;
}
```
$$T(n) = 4 + T(n-1)$$
$$T(n) = 4 + 4 + T(n-2)$$
$$T(n) = 4 + 4 + \cdots + T(1)$$
$$T(n) = 4(n-1)+2$$
$$T(n) = 4n-4+2$$
$$T(n) = 4n-2$$

---
[Source code](https://github.com/KrulYuno/obsidian_files/blob/master/Codes/CMSC%20142%20Problem%20Set%201.cpp)