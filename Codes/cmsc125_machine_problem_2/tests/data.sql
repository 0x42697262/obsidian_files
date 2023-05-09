INSERT INTO
  process (quantum)
VALUES
  (4),
  (4),
  (NULL),
  (NULL),
  (NULL);

INSERT INTO
  job (
    process_id,
    job_id,
    arrival_time,
    burst_time,
    priority
  )
VALUES
  (1, 1, 0, 20, 0),
  (1, 2, 1, 15, 0),
  (1, 3, 2, 11, 1),
  (1, 4, 3, 9, 1),
  (1, 5, 4, 11, 2),
  (1, 6, 5, 9, 3),
  (2, 1, 0, 10, 5),
  (2, 2, 1, 3, 1),
  (2, 3, 2, 15, 0),
  (2, 4, 3, 24, 4),
  (2, 5, 4, 6, 2),
  (2, 6, 5, 7, 0);
