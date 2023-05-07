# Before Running

Make sure to have a python environment configured. I won't set it inside here to not clutter my obsidian-notes git repo, so I'll set it up outside that directory.

# Running

First initialize the database sqlite by

```bash
$ flask --app machine_problem_2 init-db
```

Move to the root directory, then run:

```bash
$ flask --app machine_problem_2 run --debug
```

# Project Layout

I based the project layout structure on [Flask's documentation](https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/) since following ChatGPT's structure was quite confusing.
Not to mention, video tutorials like from YouTube are also confusing. Hence, I will follow this kind of structure:

```
.
├── machine_problem_2/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── templates/
│       └── base.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
```

Note that I skipped some files from the standard layout since I do not need them.
