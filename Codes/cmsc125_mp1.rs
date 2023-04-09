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
    let MAX_TIME: u32 = 10;

    let mut rng = rand::thread_rng();
    let one_secs = time::Duration::from_millis(1000);
    let now = time::Instant::now();

    let mut resources: Vec<Option<Resource>> = (0..rng.gen_range(1..MAX_RESOURCES))
        .map(|id| {
            Some(Resource {
                id,
                label: format!("R{}", id),
            })
        })
        .collect();

    let mut users: VecDeque<User> = (0..rng.gen_range(1..MAX_USERS))
        .map(|id| User {
            id,
            label: format!("U{}", id),
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
    let mut working_users: u32 = users.len() as u32;
    loop {
        working_users = users.len() as u32;
        println!("Total Resources: {}", resources.len());
        println!("Time: {} seconds", total_time);
        println!();
        println!("USER   TIME LEFT   STATUS      CURRENT JOB                             JOBS    ");
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
                let mut job_id: i32;
                let mut job_resource: Option<Resource> = None;
                for i in 0..user.jobs_list.len() {
                    job_id = user.jobs_list[i].resource_id as i32;
                    job_resource = resources[job_id as usize].take();

                    match &job_resource {
                        None => {
                            continue;
                        }
                        Some(_) => {
                            let j: Job = user.jobs_list.remove(i).unwrap(); // runs at O(n)
                            user.current_job = job_resource;
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
            println!(
                "{}         {}          {}          {:?}               {:?}",
                user.id, user.job_time, -1, user.current_job, user.jobs_list
            );
        }

        println!(
            "----------------------------------------------------------------------------------"
        );

        total_time += 1.0;
        thread::sleep(one_secs);

        if working_users == 0 {
            break;
        }
    }

    // loop {
    //     let mut working_users: u32 = users.len() as u32; // if this is 0, then we break the loop
    //
    //     /*
    //      * 1) Populate users with random jobs
    //      *
    //      * This is at `total_time` = 0.0 where everything is initialized. Users would have no jobs
    //      * in the list. Resources would have no users in the list.
    //      *
    //      * Iterate each users then populate them with jobs.
    //      */
    //     let mut job_count: u32;
    //     let mut job_items: Vec<i32>;
    //
    //     for r in resources.iter() {
    //         println!("{:?}", r);
    //     }
    //     for user in users.iter_mut() {
    //         /*
    //          * The amount of jobs should each user should have is between 1 and the length of the
    //          * amount of resources. So randomize that.
    //          *
    //          * We may allow a user to not have any jobs at all. So, a user is FREE in the beginning
    //          * doing nothing.
    //          */
    //
    //         // Only populate users with random jobs at initialization.
    //         if total_time == 0.0 {
    //             job_count = rng.gen_range(1..=resources.len() as u32);
    //             job_items =
    //                 pick_random_items_from_list(job_count as i32, 0, resources.len() as i32);
    //             for res_id in job_items {
    //                 user.jobs_list.push_back(Job::new(
    //                     user.id as u32,
    //                     res_id as u32,
    //                     rng.gen_range(1..=MAX_TIME) as f64,
    //                 ));
    //             }
    //         }
    //
    //         /*
    //          * Begin to move resources to the user.
    //          * But first return all before taking a new resource.
    //          */
    //
    //         let mut job_id: i32;
    //         let mut job_resource: Option<Resource> = None;
    //
    //         // Return the borrowed resource if the user has finished their current job
    //         if user.current_job.is_some() && user.job_time == 0.0 {
    //             resources[user.resource_id as usize] = user.current_job.take();
    //             user.resource_id = -1;
    //         }
    //
    //         for i in 0..user.jobs_list.len() {
    //             job_id = user.jobs_list[i].resource_id as i32;
    //             job_resource = resources[job_id as usize].take();
    //
    //             match &job_resource {
    //                 None => {
    //                     // println!("---- DEBUG: Nothing is taken for id {}", user.id);
    //                     continue;
    //                 }
    //                 Some(_) => {
    //                     let j: Job = user.jobs_list.remove(i).unwrap(); // runs at O(n)
    //                     user.current_job = job_resource;
    //                     user.job_time = j.duration;
    //                     user.resource_id = j.resource_id as i32;
    //
    //                     break;
    //                 }
    //             }
    //         }
    //     }
    //     // let mut t = resources[0].take().unwrap();
    //     // t.wait_time += 1.0;
    //     // println!("-- {:?}", t);
    //     // resources[0] = Some(t).take();
    //
    //     println!("Total Resources: {}", resources.len());
    //     println!("Time: {} seconds", total_time);
    //     println!();
    //     println!("USER   TIME LEFT   STATUS      CURRENT JOB                             JOBS    ");
    //     println!(
    //         "----------------------------------------------------------------------------------"
    //     );
    //     for user in users.iter_mut() {
    //         if user.current_job.is_none() && user.jobs_list.len() == 0 {
    //             working_users -= 1;
    //         }
    //
    //         // let mut current_job: Resource = Resource {
    //         //     id: -1,
    //         //     label: format!("-1"),
    //         // };
    //         //
    //         // if user.current_job.is_some() {
    //         //     current_job = user.current_job.take().unwrap();
    //         // }
    //         println!(
    //             "{}         {}          {}          {:?}               {:?}",
    //             user.id, user.job_time, -1, user.current_job, user.jobs_list
    //         );
    //         if user.job_time > 0.0 {
    //             user.job_time -= 1.0;
    //         }
    //         // if current_job.id >= 0 {
    //         //     user.current_job = Some(current_job).take();
    //         // }
    //         // if user.job_time > 0.0 {
    //         //     user.job_time -= 1.0;
    //         // } else {
    //         //     if user.current_job.is_some() {
    //         //         resources[user.resource_id as usize] = user.current_job.take();
    //         //     }
    //         // }
    //     }
    //
    //     println!(
    //         "----------------------------------------------------------------------------------"
    //     );
    //     total_time += 1.0;
    //     thread::sleep(one_secs);
    //
    //     if working_users == 0 as u32 {
    //         println!("\n All users are free of jobs.");
    //         break;
    //     }
    // }

    // for u in users.iter() {
    //     println!("ID: {:?}", u.id);
    //     println!("Job: {:?}", u.current_job);
    //     println!("Time Remaining: {:?}", u.job_time);
    //     println!("Job List: {:?}", u.jobs_list);
    //     println!();
    // }
    println!("----");
    for r in resources {
        println!("R: {:?}", r);
    }
}
