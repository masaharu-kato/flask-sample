#!env/bin/python
""" Run the flask application """

import yaml
from main import app

# Load config file
with open('conf/app.yaml', mode='r') as f:
    APPCFG = yaml.load(f, Loader=yaml.SafeLoader)

if __name__ == "__main__":
    dscfg = APPCFG.get('debugserver') or {}
    app.run(
        debug = dscfg.get('debug', False),
        host = dscfg.get('host', '0.0.0.0'),
        port = dscfg.get('port', 5050),
    )
