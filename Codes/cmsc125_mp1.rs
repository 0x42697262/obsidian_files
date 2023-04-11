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
use rand::distributions::Uniform;
use rand::Rng;
use std::collections::VecDeque;
use std::{thread, time};

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

    resource_id: i32,
    jobs_list: VecDeque<Job>,
    current_job: Option<Resource>,
    job_time: f64,
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
    user_id: u32,
    resource_id: u32,
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
    fn new(user_id: u32, resource_id: u32, duration: f64) -> Job {
        return Job {
            user_id,
            resource_id,
            duration,
        };
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

    let mut rng = rand::thread_rng();
    let range = Uniform::new(min, max);
    let items: Vec<i32> = (0..count).map(|_| rng.sample(&range)).collect();

    items
}

fn main() {
    let MAX_USERS: i32 = 11;
    let MAX_RESOURCES: i32 = 5;
    let MAX_TIME: u32 = 5;

    let mut rng = rand::thread_rng();
    let one_secs = time::Duration::from_millis(1000);

    let mut resources: Vec<Option<Resource>> = (0..rng.gen_range(1..MAX_RESOURCES))
        .map(|id| {
            Some(Resource {
                id,
                label: format!("R{}", id + 1),
            })
        })
        .collect();

    let mut users: VecDeque<User> = (0..rng.gen_range(1..MAX_USERS))
        .map(|id| User {
            id,
            label: format!("U{}", id + 1),
            resource_id: -1,
            jobs_list: VecDeque::new(),
            current_job: None,
            job_time: 0.0,
        })
        .collect();

    let mut jobs: VecDeque<Job> = VecDeque::new();

    // Populate users with random jobs at initialization
    for user in users.iter_mut() {
        let job_count = rng.gen_range(1..=resources.len() as u32);
        let job_items = pick_random_items_from_list(job_count as i32, 0, resources.len() as i32);
        for res_id in job_items {
            user.jobs_list.push_back(Job::new(
                user.id as u32,
                res_id as u32,
                rng.gen_range(1..=MAX_TIME) as f64,
            ));
        }
    }

    for j in jobs {
        println!("{:?}", j);
    }
    // Loop Inits
    let mut total_time: f64 = 0.00; // seconds
    let mut working_users: u32;
    loop {
        working_users = users.len() as u32;

        print!("\x1B[2J\x1B[1;1H");
        println!("Total Resources: {}", resources.len());
        println!("Time: {} seconds", total_time);
        println!();
        println!(
            "USER   TIME LEFT   STATUS      CURRENT JOB                             NEXT JOB    "
        );
        println!(
            "----------------------------------------------------------------------------------"
        );
        for user in users.iter_mut() {
            if user.job_time > 0.0 {
                user.job_time -= 1.0;
            }
            if user.current_job.is_some() && user.job_time == 0.0 {
                resources[user.resource_id as usize] = user.current_job.take();
                user.resource_id = -1;
            }

            if user.current_job.is_none() && !user.jobs_list.is_empty() {
                for i in 0..user.jobs_list.len() {
                    let mut job_id: i32;
                    job_id = user.jobs_list[i].resource_id as i32;

                    match resources[job_id as usize].take() {
                        None => continue,
                        resource => {
                            let j: Job = user.jobs_list.remove(i).unwrap(); // runs at O(n)
                            user.current_job = resource;
                            user.job_time = j.duration;
                            user.resource_id = j.resource_id as i32;
                            break;
                        }
                    }
                }
            }
            if user.current_job.is_none() && user.jobs_list.is_empty() {
                working_users -= 1;
            }
            if !user.jobs_list.is_empty() {
                println!(
                    "{}         {}          {}          {:?}               {:?}",
                    user.id, user.job_time, -1, user.current_job, user.jobs_list[0]
                );
            } else {
                println!(
                    "{}         {}          {}          {:?}               {:?}",
                    user.id, user.job_time, -1, user.current_job, user.jobs_list
                );
            }
        }

        println!(
            "----------------------------------------------------------------------------------"
        );
        println!("RESOURCES:");
        for r in &resources {
            println!(" {:?}", r);
        }

        total_time += 1.0;
        thread::sleep(one_secs);

        if working_users == 0 {
            break;
        }
    }

    // for u in users.iter() {
    //     println!("ID: {:?}", u.id);
    //     println!("Job: {:?}", u.current_job);
    //     println!("Time Remaining: {:?}", u.job_time);
    //     println!("Job List: {:?}", u.jobs_list);
    //     println!();
    // }
}
