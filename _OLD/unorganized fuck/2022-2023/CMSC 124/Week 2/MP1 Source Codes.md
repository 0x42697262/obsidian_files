```python
temp_f = int(input("Enter Fahrenheit Value: "))
print(f"Equivalent Celcius: {(temp_f - 32)*(5/9)}")
```
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

----
Need of caution, all codes below here are highly vulnerable to sql injection. I didn't care but you should. Practice sanitizations please.

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

```java
import java.util.Scanner;
import java.sql.*;

public class SIS{
  static void message_header(){
    String s =  "1) Insert Student\n" + "2) Delete Student\n" + "3) Show Students\n" + "0) Quit\n";
    System.out.println("==== Student System Information ====");
    System.out.print(s);
    System.out.print("> ");
  }

  public static void main(String[] args){
    // gotta run this java with: java -cp '.:sqlite-jdbc.jar' SIS
    // download sqlite-jdbc driver on github
    Connection con = null;
    Statement stmt = null;
    PreparedStatement pstmt = null;

    try {
      Class.forName("org.sqlite.JDBC");
      con = DriverManager.getConnection("jdbc:sqlite:SIS.db");
      con.setAutoCommit(false);
      

      String sql_table = "CREATE TABLE IF NOT EXISTS StudentInformation(name TEXT, age INTEGER, gpa REAL, grade_level TEXT)";
      String sql_insert = "INSERT INTO StudentInformation (name, age, gpa, grade_level) VALUES (?,?,?,?)";
      String sql_delete = "DELETE FROM StudentInformation WHERE name=?";
      String sql_query = "SELECT * FROM StudentInformation";
      
      stmt = con.createStatement();
      stmt.executeUpdate(sql_table);
      
      Scanner sc = new Scanner(System.in);
      int choice;

      String name;
      int age;
      float gpa;
      String grade_level;

      while (true) {
        message_header();
        choice = sc.nextInt();
        switch (choice){
          case 0:
            System.exit(0);
            break;
          case 1:
            System.out.print("Name: ");
            name = sc.nextLine();
            name = sc.nextLine();
            System.out.print("Age: ");
            age = sc.nextInt();
            System.out.print("GPA: ");
            gpa = sc.nextFloat();
            System.out.print("Grade Level: ");
            grade_level = sc.nextLine();
            grade_level = sc.nextLine();

            pstmt = con.prepareStatement(sql_insert);
            pstmt.setString(1, name);
            pstmt.setString(2, String.valueOf(age));
            pstmt.setString(3, String.valueOf(gpa));
            pstmt.setString(4, grade_level);
            pstmt.executeUpdate();
            con.commit();

            break;

          case 2:
            System.out.print("Name: ");
            name = sc.nextLine();
            name = sc.nextLine();

            pstmt = con.prepareStatement(sql_delete);
            pstmt.setString(1, name);
            pstmt.executeUpdate();
            con.commit();

            break;

          case 3:
            ResultSet rs = stmt.executeQuery(sql_query);
            while(rs.next()){
              String n = rs.getString("name");
              int a = rs.getInt("age");
              float g = rs.getFloat("gpa");
              String g_l = rs.getString("grade_level");

              System.out.println("Name: " + n);
              System.out.println("Age: " + a);
              System.out.println("GPA: " + g);
              System.out.println("Grade Level: " + g_l);
              System.out.println();
            }

            break;

          default:
            break;
        }
      }
    
      // con.commit();

    } catch (Exception e) {
      System.out.println(e); // remind me to remove this line;
    }
  }
}
```