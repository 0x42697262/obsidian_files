> [!INFO]
> Status: #WIP
> Tags: #CMSC125 #MachineProblem #OperatingSystem

----
# CMSC 125 Machine Problem 1

```markdown
 On Multiprogramming with time-sharing systems
 1. Generate a random number of resources (1-30). Label them by resource number, between 1-30.
 2. Generate a random number of users (1-30). Label them by user number between, 1-30.
 3. Generate the random resource that a user will need and the length of the time that the user will use the resource (1-30 seconds).
    The resource(s) that a user will request must only be those randomly generated resources (from #1).
 4. The program should be able to display the status of the resources, including the user currently using the resource, the time (or time left) that the user needs to use the resource.
 5. The program should also be able to list the users “in waiting” of a resource, if there are any, and when these users will be able to start using the resource.
 6. Finally, the program should be able to say when the resources will be free of users (meaning, no user needs to use the resource).
 
 Additional specs:
 - A user can only request for a specific resource once. User cannot request for a resource multiple times.
 - User request is to be sorted according to priority (by order number, in increasing order)
 
 NOTE: As to the order of the usage, just base it on the user number. You may use any language for implementation.
```
Create a struct of `Users` and `Resources`. Imagine that this problem is somewhat similar to Internet Cafe. It is entirely possible to generate multiple resources but only 1 resource is used by all users. A user will borrow a resource making it unavailable to other users. I think **rust** is the perfect language for that?

**Flow**:
A user takes ownership of a resource from a vector then the user would pop the job and give it to the resource. The resource can then set the current user and duration it will be owned. 

In the loop section, all users must return their borrowed resource first before a user can take a resource because otherwise if a resource ends and a user requests a resource happens at the same time, the user that will borrow a resource would not be able to acquire it.

---
# TODO
- [x] Generate Random Amount of Users
- [x] Generate Random Amount of Resources
- [x] Randomizing User using at least one resource
- [x] Proceed to next job if job is taken
- [x] Return the resource after borrowing
- [ ] User Interface
	- [ ] Status
	- [ ] Interactivity
		- [ ] Steps
		- [ ] Pause

---
## Randomization
Use `rand::Rng` [crate](https://rust-lang-nursery.github.io/rust-cookbook/algorithms/randomness.html). To generate a random number between two integers (min and max), do this:
```rust
let mut rng =  rand::thread_rng();
let num: i32 = rng.gen_range(0..31);
```

## Creating and Indexing Vectors
Read it from this [documentation](https://doc.rust-lang.org/book/ch08-01-vectors.html).

## Sleeping
```rust
use std::{thread, time};
let one_secs = time::Duration::from_millis(1000);
//let now = time::Instant::now();
thread::sleep(one_secs);
```

## Clearing the terminal
```rust
print!("\x1B[2J\x1B[1;1H");
```