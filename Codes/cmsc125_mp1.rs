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
use rand::{thread_rng, Rng};
use std::collections::HashMap;
use std::collections::VecDeque;
use std::time::Duration;
use std::{thread, time};

struct SETTINGS {
    USERS: u32,
    RESOURCES: u32,
    TIME: Duration,
}

impl SETTINGS {
    fn new(USERS: u32, RESOURCES: u32, TIME: Duration) -> SETTINGS {
        SETTINGS {
            USERS,
            RESOURCES,
            TIME,
        }
    }
}

#[derive(Debug)]
enum ResourceStatus {
    Available,
    Processing,
}

#[derive(Debug)]
enum UserStatus {
    Idle,
    Working,
    Waiting,
}

#[derive(Debug)]
struct Job {
    resource_id: u32,
    user_id: u32,
    job_time: Duration,
}

impl Job {
    fn new(resource_id: u32, user_id: u32, job_time: Duration) -> Job {
        Job {
            resource_id,
            user_id,
            job_time,
        }
    }
}
#[derive(Debug)]
struct Resource {
    id: u32,
    status: ResourceStatus,
    user: Option<u32>,    // user id
    time_left: Duration,  // in seconds
    queue: VecDeque<u32>, // user id list
}

impl Resource {
    fn new(id: u32) -> Resource {
        Resource {
            id,
            status: ResourceStatus::Available,
            user: None,
            time_left: Duration::from_secs(0),
            queue: VecDeque::new(),
        }
    }

    fn make_available(&mut self) {
        self.status = ResourceStatus::Available;
        self.user = None;
    }

    fn make_in_use(&mut self, user: u32, time_left: Duration) {
        self.user = Some(user);
        self.time_left = time_left;
        self.status = ResourceStatus::Processing;
        // check the queue
    }

    fn decrement_time(&mut self) {
        if self.time_left.as_secs() > 0 {
            self.time_left -= Duration::from_secs(1);
        }
    }
    fn check_time(&mut self) -> bool {
        if self.time_left.as_secs() == 0 {
            true
        } else {
            false
        }
    }
}

#[derive(Debug)]
struct User {
    id: u32,
    status: UserStatus,
    resource_using: Option<Resource>,
    jobs: VecDeque<Job>,
}

impl User {
    fn new(id: u32) -> User {
        User {
            id,
            status: UserStatus::Idle,
            resource_using: None,
            jobs: VecDeque::new(),
        }
    }
    fn start_job(&mut self, resource: Option<Resource>) {
        if let Some(job) = self.jobs.pop_front() {
            self.resource_using = resource;
            self.status = UserStatus::Working;

            if let Some(mut res) = self.resource_using.take() {
                res.make_in_use(self.id, job.job_time);
                self.resource_using = Some(res).take();
            }
        }
    }

    fn make_waiting(&mut self) {
        self.status = UserStatus::Waiting;
        self.resource_using = None;
    }

    fn check_if_not_working(&mut self) -> bool {
        if self.resource_using.is_none() {
            true
        } else {
            false
        }
    }
    fn check_if_there_are_jobs(&mut self) -> bool {
        if !self.jobs.is_empty() {
            true
        } else {
            false
        }
    }

    fn are_all_jobs_finished(&mut self) -> bool {
        if self.resource_using.is_none() && self.jobs.is_empty() {
            true
        } else {
            false
        }
    }
}

fn pick_random_items_from_list(count: i32, min: i32, max: i32) -> Vec<i32> {
    let count = count.min(max - min + 1).max(0); // Ensure count is within range

    let mut rng = thread_rng();
    let mut items: Vec<i32> = Vec::with_capacity(count as usize);

    while items.len() < count as usize {
        let item = rng.gen_range(min..=max);
        if !items.contains(&item) {
            items.push(item);
        }
    }

    items
}

fn main() {
    let settings = SETTINGS::new(30, 30, Duration::from_secs(10));
    let mut rng = thread_rng();
    let mut total_time: Duration = Duration::from_secs(0);

    // Generate available resources and users
    let mut resources: Vec<Option<Resource>> = (0..rng.gen_range(1..settings.RESOURCES))
        .map(|id| Some(Resource::new(id)))
        .collect();
    let mut users: Vec<User> = (0..rng.gen_range(1..settings.USERS))
        .map(|id| User::new(id))
        .collect();

    // Add random jobs to a user
    for user in users.iter_mut() {
        let number_of_resources = resources.len();
        let job_count = rng.gen_range(1..=number_of_resources);
        let job_items =
            pick_random_items_from_list(job_count as i32, 0, number_of_resources as i32 - 1);

        for id in job_items {
            user.jobs.push_back(Job::new(
                id as u32,
                user.id,
                Duration::from_secs(rng.gen_range(1..settings.TIME.as_secs())),
                // Duration::from_secs(5),
            ));
        }
    }

    for u in users.iter_mut() {
        println!("{:?}", u);
    }
    println!();
    println!();
    println!();
    // Main Loop
    loop {
        let mut idle_users: u32 = 0;

        // Before taking ownership, return all borrowed resources first.
        for user in users.iter_mut() {
            // holy mother grail of fuck, a lot of borrowing then returning then borrowing then
            // returning again
            // i love rust!!!
            if let Some(mut res) = user.resource_using.take() {
                if res.check_time() == true {
                    res.make_available();
                    user.make_waiting();
                    let rid = res.id as usize;
                    resources[rid] = Some(res);
                } else {
                    user.resource_using = Some(res); // return to the user
                }
            }
        }

        // start borrowing of resource
        for user in users.iter_mut() {
            if user.check_if_not_working() && user.check_if_there_are_jobs() {
                for i in 0..user.jobs.len() {
                    let r = user.jobs[i as usize].resource_id;

                    // println!("User {} is not working should grab job: {}", user.id, r);
                    match resources[r as usize].take() {
                        None => continue,
                        resource => {
                            // println!("User {} took the job: {:?}", user.id, resource);
                            user.start_job(resource);
                            break;
                        }
                    }
                }
            }

            if user.are_all_jobs_finished() == true {
                idle_users += 1;
            }
        }

        // Print shits
        println!("-----");
        println!("Time: {}", total_time.as_secs());
        for r in resources.iter() {
            println!("{:?}", r);
        }
        println!();
        for u in users.iter() {
            println!("{:?}", u);
        }

        // Increment stuffs after printing
        total_time += Duration::from_secs(1);
        thread::sleep(Duration::from_secs(1));
        for user in users.iter_mut() {
            if let Some(mut res) = user.resource_using.take() {
                res.decrement_time();
                user.resource_using = Some(res);
            }
        }

        // Exit loop if all resources are free and all users no longer have tasks/jobs
        if idle_users == users.len() as u32 {
            break;
        }
    }
}
