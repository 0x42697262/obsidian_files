> [!INFO]
> Status: 
> Tags: #programming #rust

----
# Rust Programming
- [[Rust Programming#Stacks|Implementing Stacks]]
- [[#Summation of Array]]

---

# Implementing Stacks
Use [Linked Lists](https://doc.rust-lang.org/std/collections/struct.LinkedList.html) or [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html). I will be using linked lists.
```rust
// initiate new stack through vectors
let mut stack: Vec<i32> = Vec::new(); 

// pushing on to the stack
stack.push(69);
stack.push(420); 

// popping from the stack
stack.pop().unwrap() // 42
```
When unwrapping, make sure that the value is not `None`. Otherwise it panics:
```rust
thread 'main' panicked at 'called `Option::unwrap()` on a `None` value', src/main.rs:9:12
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

# Summation of Array
```rust
fn sum_of_array(ar: &[i32]) -> i32 {
	return ar.iter().sum();
}
```