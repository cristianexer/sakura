from sanic import Sanic

#from commands import commands

from blueprints.account import account
from blueprints.ineed import ineed


app = Sanic(__name__)

app.debug = True

app.config['prisma'] = {
    'service' : 'demo@dev',
    'roles': ['admin'],
    'secret': 'managementAPISecretKey',
    'endpoint': 'https://eu1.prisma.sh/daniel-cristian-fat-964bc7/demo/dev'
}

app.config['sakura'] = {
    'service': 'sakura@dev',
    'secret': 'some_very_secret_thing',
    'token_lifetime_minutes': 20
}


app.blueprint(account)
app.blueprint(ineed)

#app.cli.add_command(commands)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)


