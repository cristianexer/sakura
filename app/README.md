# The API Layer 


For this part the Sanic framework was used to implement the control layer for Prisma



```bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python app.py

```
Do not forget to add your credentials.

Tip: Do not worry about the jwt from prisma, is already handled in here.

```python
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

```



