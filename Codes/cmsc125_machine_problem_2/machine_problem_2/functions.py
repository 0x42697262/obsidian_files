from flask import Flask, render_template
from . import db

def insert_to_db(process, quantum = None):
    db.insert_process(quantum)
    last_process_id     = db.select_last_process()
    for p in process:
        print(p, process[p])
        db.insert_job(
                last_process_id, 
                p, 
                process[p]['arrival_time'], 
                process[p]['burst_time'], 
                process[p]['priority']
            )
    # db.commit()
