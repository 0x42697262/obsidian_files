/****
 *
 * LABARATORY EXERCISE 1 (https://github.com/KrulYuno/obsidian_files/blob/master/Notes/020%20Studies/CMSC%20125%20Machine%20Problem%201.md)
 *
 * On Multiprogramming with time-sharing systems
 * 1. Generate a random number of resources (1-30). Label them by resource number, between 1-30.
 * 2. Generate a random number of users (1-30). Label them by user number between, 1-30.
 * 3. Generate the random resource that a user will need and the length of the time that the user will use the resource (1-30 seconds).
 *    The resource(s) that a user will request must only be those randomly generated resources (from #1).
 * 4. The program should be able to display the status of the resources, including the user currently using the resource, the time (or time left) that the user needs to use the resource.
 * 5. The program should also be able to list the users “in waiting” of a resource, if there are any, and when these users will be able to start using the resource.
 * 6. Finally, the program should be able to say when the resources will be free of users (meaning, no user needs to use the resource).
 *
 * Additional specs:
 * - A user can only request for a specific resource once. User cannot request for a resource multiple times.
 * - User request is to be sorted according to priority (by order number, in increasing order)
 *
 * NOTE: As to the order of the usage, just base it on the user number. You may use any language for implementation.
 *
 */

#[derive(Debug)]

/// Represents a Resource, with currently in use and availability
///
/// # Examples
///
/// ```
/// let resource_1 = Resource::new(1);
/// ```
///
struct Resource {
    enabled: bool,
    id: i32,
    label: String,
}

impl Resource {
    fn new(id: i32) -> Resource {
        return Resource {
            enabled: false,
            id,
            label: format!("resource{}", id),
        };
    }
}

// A `Job` represents a task that needs to be completed using a particular `Resource`.
///
/// # Examples
///
/// Creating a new `Job`:
///
/// ```
/// let job = Job::new(1, 2.5);
/// ```
///
/// This creates a new `Job` that needs to be completed using the `Resource` with an ID of 1, and has a duration of 2.5 seconds.
#[derive(Debug)]
struct Job {
    resource_id: i32,
    duration: f64,
}

impl Job {
    /// Creates a new `Job` with the specified `resource_id` and `duration`.
    ///
    /// # Arguments
    ///
    /// * `resource_id` - The ID of the `Resource` needed to complete this `Job`.
    /// * `duration` - The duration of the `Job`.
    ///
    /// # Examples
    ///
    /// Creating a new `Job` with an ID of 1, and a duration of 2.5 seconds:
    ///
    /// ```
    /// let job = Job::new(1, 2.5);
    /// ```
    fn new(resource_id: i32, duration: f64) -> Job {
        return Job {
            resource_id,
            duration,
        };
    }
}

/// Represents a User
///
/// # Examples
///
/// ```
/// let user_1 = User::new(1);
/// ```
///
struct User {
    enabled: bool,
    id: i32,
    label: String,

    jobs_list: Vec<Job>,
    current_job: Option<Resource>,
}

impl User {
    fn new(id: i32) -> User {
        User {
            enabled: false,
            id,
            label: format!("user{}", id),

            jobs_list: Vec::<Job>::new(),
            current_job: None,
        }
    }
}

// Picks a given number of unique random integers within a specified range.
///
/// # Arguments
///
/// * `count`: the number of integers to pick
/// * `min`: the minimum value of the range (inclusive)
/// * `max`: the maximum value of the range (exclusive)
///
/// # Returns
///
/// A vector containing the selected integers.
///
/// # Example
///
/// ```
/// use rand::Rng;
///
/// let selected = pick_random_items_from_list(5, 0, 10);
/// println!("{:?}", selected);
/// ```
fn pick_random_items_from_list(mut count: i32, min: i32, max: i32) -> Vec<i32> {
    // Ensure count is within range
    if max - min < count {
        count = max - min;
    }
    let mut items: Vec<i32> = Vec::new();

    let mut rng = rand::thread_rng();

    let mut item: i32;
    while items.len() < count as usize {
        item = rng.gen_range(min..max);
        if !items.contains(&item) {
            items.push(item);
        }
    }

    items
}

fn generate_resources(count: i32, total: i32) -> Vec<Resource> {
    let mut entities: Vec<Resource> = Vec::<Resource>::new();

    for i in 0..total {
        let resource = Resource::new(i);
        entities.push(resource);
    }

    let selected: Vec<i32> = pick_random_items_from_list(count, 1, total);
    for e in selected {
        entities[e as usize].enabled = true;
    }

    entities
}

fn generate_users(count: i32, total: i32) -> Vec<User> {
    let mut entities: Vec<User> = Vec::<User>::new();

    for i in 0..total {
        entities.push(User::new(i));
    }

    let selected: Vec<i32> = pick_random_items_from_list(count, 0, total);
    for e in selected {
        entities[e as usize].enabled = true;
    }

    entities
}

use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    // Generate random amount of resources and users
    let resources = generate_resources(rng.gen_range(1..31), 30);
    let mut users = generate_users(rng.gen_range(1..31), 30);

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

    // Randomize the jobs for the users
    for id in &active_users_id {
        let resources_id_to_use = pick_random_items_from_list(
            rng.gen_range(0..available_resources_id.len()) as i32,
            0,
            available_resources_id.len() as i32,
        );

        for res_id in resources_id_to_use {
            users[*id]
                .jobs_list
                .push(Job::new(res_id, rng.gen_range(1..6) as f64));
        }
    }

    let mut new_user = User::new(69);
    new_user.enabled = true;
    new_user
        .jobs_list
        .push(Job::new(11, rng.gen_range(1..6) as f64));
    new_user
        .jobs_list
        .push(Job::new(7, rng.gen_range(1..6) as f64));
    new_user
        .jobs_list
        .push(Job::new(13, rng.gen_range(1..6) as f64));

    let mut new_user_job = new_user.jobs_list.pop();
    new_user.current_job = Some(resources[0]);

    users.push(new_user);
    for a in users {
        if a.enabled == true {
            println!("{} {:?} {:?}", a.id, a.current_job, a.jobs_list);
        }
    }
    println!("{:?} ", new_user_job.unwrap().duration);
    println!("{:?} ", resources[0]);
}
