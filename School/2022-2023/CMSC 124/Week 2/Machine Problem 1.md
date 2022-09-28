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
import sqlite3


class SIS_db:
    def __init__(self) -> None:
        self.db_con = sqlite3.connect("SIS.db")
        self.db_cur = self.db_con.cursor()
        self.db_cur.execute("CREATE TABLE IF NOT EXISTS StudentInformation(name TEXT, age INTEGER, gpa REAL, grade_level TEXT)")
    
    def commit(self) -> None:
        self.db_con.commit()

    def insert(self, name, age, gpa, grade_level) -> None:
        self.db_cur.execute(f"""INSERT INTO StudentInformation VALUES(
                                "{name}", {age}, {gpa}, "{grade_level}")
                """)
        self.commit()

    def delete(self, name) -> None:
        self.db_cur.execute(f"DELETE FROM StudentInformation WHERE name='{name}'")
        self.commit()

    def query(self) -> list:
        query = self.db_cur.execute("SELECT * FROM StudentInformation")
        return query.fetchall()

def message_header():
    print("==== Student Information System ====")
    print("""
1) Insert Student
2) Delete Student
3) Show Students
0) Quit
""")

def main():
    db = SIS_db()

    while True:
        message_header()
        u_in = input("> ")

        if u_in == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gpa = float(input("GPA: "))
            grade_level = input("Grade Level: ")
            db.insert(name, age, gpa, grade_level)
        if u_in == "2":
            name = input("Name: ") 
            db.delete(name)
        if u_in == "3":
            print(db.query())
        if u_in == "0":
            break

   
if __name__ == "__main__":
    main()
```

# 4. Now, evaluate each PL according to the different language evaluation criteria discussed in  class.

# 5. Determine the paradigm(s) of your chosen PL. Remember that there is no particular paradigm suited to a specific PL, so list down all applicable paradigm.

# 6. Describe the method of implementation for every PL you have chosen. Explain in detail what happens to your source code upon compilation, down to execution.


