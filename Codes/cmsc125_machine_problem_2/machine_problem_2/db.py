import sqlite3

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES,
                )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db  = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))



@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Cleared the database and created new tables.")


def init_app(app):
    # tells Flask to call that function when cleaning up after returning the response.
    app.teardown_appcontext(close_db)
    # adds a new command that can be called with the flask command.
    app.cli.add_command(init_db_command)


def insert_process(quantum = None):
    get_db().execute(
            "INSERT INTO process (quantum) VALUES (?)",
            (quantum,),
            )


def insert_job(process_id: int, job_id: int, arrival_time: int, burst_time: int, priority = None ):
    """process_id: Process ID of the job
    job_id: Job ID
    arritval_time: Time job arrived
    burst_time: Job duration
    priority: Priority ranking for Priority scheduling (optional)"""

    get_db().execute(
            "INSERT INTO job (process_id, job_id, arrival_time, burst_time, priority) VALUES (?, ?, ?, ?, ?)",
            (process_id, job_id, arrival_time, burst_time, priority),
            )

def commit():
    get_db().commit()
