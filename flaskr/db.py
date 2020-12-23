import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

#Returns the database
def get_db():
    #g is special object that holds information
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db #returning database stored in g

#closes database
def close_db(e=None):
    db = g.pop('db',None)

    if db is not None:
        db.close()

#intializes database
def init_db():
    db = get_db() # sets db = g.db
    #executing script to initalize
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

#sets a command line argument init-db to intialize a new database
@click.command('init-db')
@with_appcontext
def init_db_command():
    #Clears existing data and creates new tables.
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db) #tells flask to call this when cleaning up after returning response
    app.cli.add_command(init_db_command) #adds a new command to flask
    