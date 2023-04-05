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
Create a struct of `Users` and `Resources`. Imagine that this problem is somewhat similar to Internet Cafe. It is entirely possible to generate multiple resources but only 1 resource is used by all users.

---
# TODO
- [ ] Generate Random Amount of Users
- [ ] Generate Random Amount of Resources
- [ ] Randomizing User using at least one resource
- [ ] User Interface
	- [ ] Status
	- [ ] Interactivity

---
## Users
### Fields
- `enabled` : bool
- `id` : i32
- `label` : String
- 

## Resources
- `enabled` : bool
- `id` : i32
- `label` : String
- `is_used` : bool
- `is_available` : bool

---
## Randomization
Use `rand::Rng` [crate](https://rust-lang-nursery.github.io/rust-cookbook/algorithms/randomness.html). To generate a random number between two integers (min and max), do this:
```rust
let mut rng =  rand::thread_rng();
let num: i32 = rng.gen_range(0..31);
```

## Creating and Indexing Vectors
Read it from this [documentation](https://doc.rust-lang.org/book/ch08-01-vectors.html).
