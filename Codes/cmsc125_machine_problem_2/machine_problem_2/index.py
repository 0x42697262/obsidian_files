import functools
from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for
        )
from machine_problem_2.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')



