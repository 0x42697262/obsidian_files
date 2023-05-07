DROP TABLE IF EXISTS processes;

CREATE TABLE
  processes (
    process_id INTEGER NOT NULL,
    algorithm TEXT NOT NULL,
    arrival_time INTEGER NOT NULL,
    burst_time INTEGER NOT NULL,
    quantum INTEGER NOT NULL,
    priorities INTEGER NULL,
    PRIMARY KEY (process_id, algorithm)
  );
