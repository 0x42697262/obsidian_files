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
![[Pasted image 20220928163403.png]]
![[Pasted image 20220928163426.png]]

```cpp
#include <iostream>
#include <sqlite3.h>

int callback(void *NotUsed, int argc, char **argv, char **azColName){
  for(int i=0; i < argc; i++)
    std::cout << azColName[i] << ": " << argv[i] << std::endl;
  std::cout << std::endl;

  return 0;
 }
class SIS_db {
  int rc;
  char *zErrMsg = 0;
  sqlite3 *DB;

public:
  SIS_db(){
    this->rc = sqlite3_open("SIS.db", &this->DB);
    this->rc = sqlite3_exec(this->DB, "CREATE TABLE IF NOT EXISTS StudentInformation(name TEXT, age INTEGER, gpa REAL, grade_level TEXT)", NULL, 0, &this->zErrMsg);
    if(this->rc != SQLITE_OK){
      std::cerr << "Error loading the database." << std::endl;
      sqlite3_free(this->zErrMsg);
    }
  };


  void delete_entry(std::string name){
    std::string sql = "DELETE FROM StudentInformation WHERE name='";
    sql.append(name + "'");
    this->rc = sqlite3_exec(this->DB, sql.c_str(), NULL, 0, &this->zErrMsg);
  }

  void insert(std::string name, int age, float gpa, std::string grade_level){
    std::string sql = "INSERT INTO StudentInformation VALUES('";
    sql.append(name + "', ");
    sql.append(std::to_string(age) + ", ");
    sql.append(std::to_string(gpa) + ", '");
    sql.append(grade_level + "')");
    this->rc = sqlite3_exec(this->DB, sql.c_str(), NULL, 0, &this->zErrMsg);
  }

  void close_connection(){
    sqlite3_close(this->DB);
  }

  void query(){
    std::string data("CALLBACK FUNCTION");
    std::string sql = "SELECT * FROM StudentInformation";
    this->rc = sqlite3_exec(this->DB, sql.c_str(), callback, (void*)data.c_str(), NULL);
  }
} db;


void message_header(){
  std::cout << "==== Student Information System ====" << std::endl;
  std::cout << "1) Insert Student" << std::endl;
  std::cout << "2) Delete Student" << std::endl;
  std::cout << "3) Show Student" << std::endl;
  std::cout << "0) Quit" << std::endl;
}


int main(){
  int u_in = -1;

  std::string name;
  int age;
  float gpa;
  std::string grade_level;

  while(u_in != 0){
    message_header();
    std::cout << "> ";
    std::cin >> u_in;

    switch(u_in){
      case 1:
        std::cout << "Name: ";
        std::cin >> name;
        std::cout << "Age: ";
        std::cin >> age;
        std::cout << "GPA: ";
        std::cin >> gpa;
        std::cout << "Grade Level: ";
        std::cin >> grade_level;

        db.insert(name, age, gpa, grade_level);
        break;

      case 2:
        std::cout << "Name: ";
        std::cin >> name;

        db.delete_entry(name);
        break;

      case 3:
        db.query();
        break;

      case 0:
        break;
    }
  }

  db.close_connection();
  return 0;
}
```
![[Pasted image 20220928212441.png]]

![[Pasted image 20220928212453.png]]
![[Pasted image 20220928212516.png]]


```rust
use rusqlite::{params, Connection, Result};

struct Student {
    name: String,
    age: u32,
    gpa: f64,
    grade_level: String,
}

fn message_header() {
    println!("==== Student Information System ====");
    println!(
        "1) Insert Student
2) Delete Student
0) Quit"
    );
}

fn input_handler() -> String {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Input Error.");

    input
}

fn main() -> Result<()> {
    let db_con = Connection::open("SIS.db")?;
    db_con.execute(
        "CREATE TABLE IF NOT EXISTS StudentInformation(
            name TEXT, 
            age INTEGER, 
            gpa REAL, 
            grade_level TEXT)",
        params![],
    )?;

    let mut student = Student {
        name: String::from("test"),
        age: 4,
        gpa: 2.1,
        grade_level: String::from("Senior"),
    };

    let mut input = String::new();

    while input != "0" {
        message_header();
        input = input_handler().trim().to_string();

        if input == "1" {
            println!("Name:");
            student.name = input_handler().trim().to_string();
            println!("Age:");
            student.age = input_handler().trim().parse().expect("Not Integer.");
            println!("GPA:");
            student.gpa = input_handler().trim().parse().expect("Not Float.");
            println!("Grade Level:");
            student.grade_level = input_handler().trim().to_string();

            db_con.execute(
                "INSERT INTO StudentInformation (name, age, gpa, grade_level) VALUES(
                ?1, ?2, ?3, ?4
                )",
                params![student.name, student.age, student.gpa, student.grade_level],
            )?;
        }

        if input == "2"{
            println!("Name:");
            student.name = input_handler().trim().to_string();

            db_con.execute(
                "DELETE FROM StudentInformation WHERE name=?1",
                params![student.name],
                )?;
        }
    }

    Ok(())
}
```
![[Pasted image 20220929174443.png]]![[Pasted image 20220929174508.png]]
```java

```


# 4. Now, evaluate each PL according to the different language evaluation criteria discussed in  class.

# 5. Determine the paradigm(s) of your chosen PL. Remember that there is no particular paradigm suited to a specific PL, so list down all applicable paradigm.

# 6. Describe the method of implementation for every PL you have chosen. Explain in detail what happens to your source code upon compilation, down to execution.


---- 
# References
[1] _Data Types - The Rust Programming Language_. (n.d.). Retrieved September 27, 2022, from https://doc.rust-lang.org/book/ch03-02-data-types.html
[2] _Programming a Guessing Game - The Rust Programming Language_. (n.d.). Retrieved September 27, 2022, from https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html
[3] _SQLite In 5 Minutes Or Less_. (n.d.). Retrieved September 28, 2022, from https://www.sqlite.org/quickstart.html
[4] _sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.10.7 documentation_. (n.d.). Retrieved September 28, 2022, from https://docs.python.org/3/library/sqlite3.html
[5] _SQLite - Rust Cookbook_. (n.d.). Retrieved September 29, 2022, from https://rust-lang-nursery.github.io/rust-cookbook/database/sqlite.html