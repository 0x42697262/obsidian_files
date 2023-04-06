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

---
# TODO
- [x] Generate Random Amount of Users
- [x] Generate Random Amount of Resources
- [x] Randomizing User using at least one resource
- [x] Proceed to next job if job is taken
- [ ] Return the resource after borrowing
- [ ] User Interface
	- [ ] Status
	- [ ] Interactivity
		- [ ] Steps
		- [ ] Pause

---
## Users
### Fields
- `id` : i32
- `label` : String
- `jobs_list` : Vec\<Job\>
- `current_job`: Option\<Resource\>

**Note:**
1. A user can take multiple jobs (resource/s) and can only have one current job. And after finishing all the jobs, a may not have a job.

## Resources
- `id` : i32
- `label` : String

---
## Randomization
Use `rand::Rng` [crate](https://rust-lang-nursery.github.io/rust-cookbook/algorithms/randomness.html). To generate a random number between two integers (min and max), do this:
```rust
let mut rng =  rand::thread_rng();
let num: i32 = rng.gen_range(0..31);
```

## Creating and Indexing Vectors
Read it from this [documentation](https://doc.rust-lang.org/book/ch08-01-vectors.html).

---
# Code History
```rust
// Save the IDs of the enabled resources and users into a vector.
let mut available_resources_id: Vec<i32> = Vec::<i32>::new();
for res in resources.iter() {
	if res.enabled == true {
		available_resources_id.push(res.id);
	}
}
let mut active_users_id: Vec<usize> = Vec::<usize>::new();
for (i, user) in users.iter().enumerate() {
	if user.enabled == true {
		active_users_id.push(i);
	}
}

// Randomize the jobs for the users
let mut resources_id_to_use: Vec<i32>;
for id in active_users_id.iter() {
	resources_id_to_use = pick_random_items_from_list(
		rng.gen_range(0..available_resources_id.len()) as i32,
		0,
		available_resources_id.len() as i32,
	);

	for res_ids in resources_id_to_use {
		users[*id].jobs_list.push(Job::new(res_ids, rng.gen_range(1..31)));
	}
}
```
So, there's a minimized version of this code which translates to:
```rust
let available_resources_id: Vec<i32> = resources
	.iter()
	.filter(|res| res.enabled)
	.map(|res| res.id)
	.collect();

let active_users_id: Vec<usize> = users
	.iter()
	.enumerate()
	.filter(|(_, user)| user.enabled)
	.map(|(i, _)| i)
	.collect();

for id in &active_users_id {
	let resources_id_to_use = pick_random_items_from_list(
		rng.gen_range(0..available_resources_id.len()) as i32,
		0,
		available_resources_id.len() as i32,
	);

	for res_id in resources_id_to_use {
		users[*id]
			.jobs_list
			.push(Job::new(res_id, rng.gen_range(1..31) as f64));
	}
}

```
Here's what this code does:
-   `available_resources_id` is computed using the `filter` and `map` iterator methods. The `filter` method returns only the resources that are enabled, and the `map` method extracts the IDs of those resources. Finally, the `collect` method collects the IDs into a `Vec<i32>`.
-   `active_users_id` is computed using a similar approach, but with the `enumerate` method to get the index of each user.
-   The loop that assigns jobs to users is simplified by using the `extend` method of the `Vec` type to add the randomly selected resources to each user's job list.