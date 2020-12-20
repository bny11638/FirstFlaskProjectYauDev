from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

#Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    # shows user profile for that user
    return 'User %s ' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show post with gien id, id is an int
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # shows subpath after /path/
    return 'Subpath %s' % escape(subpath)