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
use rand::Rng;
use std::{collections::VecDeque, fmt::format};

/// Represents a Resource, with currently in use and availability
///
/// # Examples
///
/// ```
/// let resource_1 = Resource::new(1);
/// ```
///
#[derive(Debug)]
struct Resource {
    id: i32,
    label: String,
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
#[derive(Debug)]
struct User {
    id: i32,
    label: String,

    jobs_list: VecDeque<Job>,
    current_job: Option<Resource>,
    duration: f64,
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

fn main() {
    let MAX_USERS: i32 = 11;
    let MAX_RESOURCES: i32 = 5;

    let mut rng = rand::thread_rng();

    let mut resources: Vec<Option<Resource>> = (0..rng.gen_range(1..MAX_RESOURCES))
        .map(|id| {
            Some(Resource {
                id,
                label: format!("resource{}", id),
            })
        })
        .collect();

    let mut users: VecDeque<User> = (0..rng.gen_range(1..MAX_USERS))
        .map(|id| User {
            id,
            label: format!("user{}", id),
            jobs_list: VecDeque::new(),
            current_job: None,
            duration: 0.00,
        })
        .collect();

    // Populate a user with random jobs
    let mut count: u32;
    let mut items: Vec<i32>;
    for u in users.iter_mut() {
        count = rng.gen_range(1..=resources.len() as u32);
        items = pick_random_items_from_list(count as i32, 0, resources.len() as i32);

        for i in items {
            u.jobs_list
                .push_back(Job::new(i, rng.gen_range(1..=30) as f64));
        }
        // println!("{} Items: {:?}", u.id, u.jobs_list);
        // check if resource is taken or already owned
        let mut job: i32;
        let mut job_resource: Option<Resource> = None;
        for i in 0..u.jobs_list.len() {
            job = u.jobs_list[i].resource_id;
            job_resource = resources[job as usize].take();

            match &job_resource {
                None => {
                    continue;
                }
                Some(_) => {
                    // maybe on this part we add a new field for the resource that has duration
                    // which if it is 0, it should be returned
                    let j: Job = u.jobs_list.remove(i).unwrap(); // runs at O(n)
                    u.current_job = job_resource;
                    u.duration = j.duration;

                    break;
                }
            }
        }
    }

    // testing area ++
    resources = (0..3)
        .map(|id| {
            Some(Resource {
                id,
                label: format!("resource{}", id),
            })
        })
        .collect();

    users = (0..6)
        .map(|id| User {
            id,
            label: format!("user{}", id),
            jobs_list: VecDeque::new(),
            current_job: None,
            duration: 0.00,
        })
        .collect();

    users[0].jobs_list.push_back(Job::new(2, 4.00));
    users[0].jobs_list.push_back(Job::new(0, 2.00));

    users[1].jobs_list.push_back(Job::new(2, 5.00));
    users[1].jobs_list.push_back(Job::new(0, 9.00));

    users[2].jobs_list.push_back(Job::new(0, 11.00));
    users[2].jobs_list.push_back(Job::new(1, 10.00));

    users[3].jobs_list.push_back(Job::new(1, 3.00));
    users[3].jobs_list.push_back(Job::new(2, 5.00));

    users[4].jobs_list.push_back(Job::new(0, 7.00));
    users[4].jobs_list.push_back(Job::new(1, 7.00));

    users[5].jobs_list.push_back(Job::new(2, 10.00));

    for u in users.iter_mut() {
        let mut job: i32;
        let mut job_resource: Option<Resource> = None;
        for i in 0..u.jobs_list.len() {
            job = u.jobs_list[i].resource_id;
            job_resource = resources[job as usize].take();

            match &job_resource {
                None => {
                    continue;
                }
                Some(_) => {
                    // maybe on this part we add a new field for the resource that has duration
                    // which if it is 0, it should be returned
                    let j: Job = u.jobs_list.remove(i).unwrap(); // runs at O(n)
                    u.current_job = job_resource;
                    u.duration = j.duration;

                    break;
                }
            }
        }
    }

    // testing area --

    let mut TOTAL_TIME: f64 = 0.00; // seconds

    loop {
        let mut all_free: u32 = 0;
        println!("Total Resources: {}", resources.len());
        println!("Time: {} seconds", TOTAL_TIME);
        println!();
        println!("USER    CURRENT JOB     TIME LEFT    STATUS      JOBS    ");
        println!("----------------------------------------------------------");

        for u in users.iter_mut() {
            let mut job: &Resource = &Resource {
                id: -1,
                label: format!("None"),
            };
            if u.current_job.is_some() {
                job = u.current_job.as_ref().unwrap();
            }
            if u.current_job.is_none() && u.jobs_list.len() == 0 {
                all_free += 1;
                println!("FREE +1");
            }
            println!(
                "{}    {}     {}    {}      {:?}",
                u.id, job.label, u.duration, -1, u.jobs_list
            );

            // decrease time
            if u.duration > 0.00 {
                u.duration -= 1.00;
            } else {
                if u.current_job.is_some() {
                    resources[job.id as usize] = u.current_job;
                }
            }
        }

        println!("----------------------------------------------------------");

        break;
    }

    // for u in users.iter() {
    //     println!("ID: {:?}", u.id);
    //     println!("Job List: {:?}", u.jobs_list);
    //     println!("Current Job: {:?}", u.current_job);
    //     println!();
    // }
    // println!("----");
    // for r in resources {
    //     println!("{:?}", r);
    // }
}
