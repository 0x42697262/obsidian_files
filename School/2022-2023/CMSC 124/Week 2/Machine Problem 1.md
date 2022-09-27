CMSC 124 Machine Problem 1  
Topic Coverage: Background and Preliminaries


# 1. Choose 4 programming languages (hereafter referred to as PL) that you are comfortable  working with.

# 2. Create a simple program that will ask for a temperature in Fahrenheit and will output its equivalent value in Celsius

```python
temp_f = int(input("Enter Fahrenheit Value: "))
print(f"Equivalent Celcius: {(temp_f - 32)*(5/9)}")
```
![[Pasted image 20220927113626.png]]

```cpp
#include <iostream>
#include <string>

int main(){
  float temp_f = 0;
  std::cout << "Enter Fahrenheit Value: ";
  std::cin >> temp_f;
  temp_f = (temp_f - 32) *(5.0/9.0);
  std::cout << "Equivalent Celcius: " << temp_f << std::endl;
  return 0;
}
```
![[Pasted image 20220927131408.png]]

```rust
fn main(){
  let mut input_text = String::new();
  let mut temps_f: f32 = 0.0;

  println!("Enter Fahrenheit Value: ");

  std::io::stdin()
            .read_line(&mut input_text)
            .expect("No temperature entered.");
  temps_f = input_text
              .trim()
              .parse()
              .expect("Not a temperature.");
  temps_f = (temps_f - 32.0)*(5.0/9.0);
  println!("Equivalent Celcius: {temps_f}");
}
```
![[Pasted image 20220927145554.png]]

```java
import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner input_scanner = new Scanner(System.in);
    System.out.println("Enter Fahrenheit Value: ");
    double temps_f = input_scanner.nextFloat();
    temps_f = (temps_f - 32) * (5.0/9.0);

    System.out.println("Equivalent Celcius: " + temps_f);
  }
}
```
![[Pasted image 20220927165056.png]]

# 3. Write a small program in your chosen PL that can store student information, such as the  following: Name, Age, GPA (float), Grade Level (“Freshman”, “Sophomore”, “Junior”,  “Senior”)
```python
class Student:
    def __init__(self, name, age, gpa, grade_level) -> None:
        self._name = name
        self._age = age
        self._gpa = gpa
        self._grade_level = grade_level

    def query(self) -> list:
        return [self._name, self._age, self._gpa, self._grade_level]

def main():
    print("Student Information System")
    s1 = Student("Wi", 69, 5, "Junior Level")
    print(s1.query())


if __name__ == "__main__":
    main()
```

# 4. Now, evaluate each PL according to the different language evaluation criteria discussed in  class.

# 5. Determine the paradigm(s) of your chosen PL. Remember that there is no particular paradigm suited to a specific PL, so list down all applicable paradigm.

# 6. Describe the method of implementation for every PL you have chosen. Explain in detail what happens to your source code upon compilation, down to execution.


