from sanic import Sanic

#from commands import commands

from blueprints.account import account
from blueprints.ineed import ineed


app = Sanic(__name__)

app.debug = True

app.config['api_token'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InNlcnZpY2UiOiJkZW1vQGRldiIsInJvbGVzIjpbImFkbWluIl19LCJpYXQiOjE1NzEyNTQwNTAsImV4cCI6MjU3MTg1ODg1MH0.cONlHOvJ0vHds4gHcZJUHOtjxrpgfqIUVxAD-qvWdAc' 

app.config['api_endpoint'] = 'https://eu1.prisma.sh/daniel-cristian-fat-964bc7/demo/dev'

#jwt = JWT(app, authenticate_by_email_and_password, identity)


app.blueprint(account)
app.blueprint(ineed)

#app.cli.add_command(commands)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)


