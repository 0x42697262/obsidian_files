DROP TABLE IF EXISTS process;

DROP TABLE IF EXISTS job;

CREATE TABLE
  process (
    process_id INTEGER NOT NULL PRIMARY KEY,
    quantum INTEGER NULL
  );

CREATE TABLE
  job (
    process_id INTEGER NOT NULL,
    job_id INTEGER NOT NULL,
    arrival_time INTEGER NOT NULL,
    burst_time INTEGER NOT NULL,
    priority INTEGER NULL,
    PRIMARY KEY (process_id, job_id),
    FOREIGN KEY (process_id) REFERENCES process (process_id)
  );
