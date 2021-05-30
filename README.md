# YTVote
YouTube Voting System

## Setup
1. Prepare a python virtualenv:  
   `python3 -m venv env` (Use python3.8 or later)
1. Enter to the virtualenv:  
   `. env/bin/activate`
1. Install YTVote (and the all dependencies):  
   `pip install -e .[dev]`  
   (In the production, `pip install .`)

## Preparation of setting files
### Configurations directory
- `/conf.default`  
   Default configuration files (templates, git managed)
- `/conf`
   Actual configuration files (gitignored)
### List of the configuration files
- `apikeys.yaml`  
   Definitions of API-keys
- `app.yaml`    
   Application settings
- `users.yaml`  
   User credentials: dictionary of username and password hash
- `apache2.conf`  
   Apache2 webserver settings for the production
  - `%%PORT%%`: Port number
  - `%%USERNAME%%`: Runner user name
  - `%%GROUPNAME%%`: Runner group name
  - `%%PROJECT_ROOT%%`: Project root directory  
    (The path where this README.md locates)

## Debugging server
- Run `app/run.py`
- Access to the address like `localhost:5050` via your web browser.  
  (Replace `5050` to your port number)

## Settings of the production server
1. Install apache2 wsgi modules:  
   `sudo apt install apache2 libapache2-mod-wsgi-py3`
1. Copy `conf.default/apache2.conf` to `/etc/apache2/sites-available/ytvote.conf`
1. Fill the placeholders in the `ytvote.conf`  
   (see the "List of the configuration files" above)
1. Enable ytvote:  
   `pushd sites-enabled; sudo ln -s ../sites-available/sakai-city-integrator.conf .; popd`
1. Edit `/etc/apache2/ports.conf`:  
   Append `Listen %%PORT%%` (%%PORT%%: Port number)
1. Edit `/etc/apache2/envvars`:  
   Comment out `export LANG=C`, and append `export LANG="en_US.UTF-8"`
1. Restart apache2:  
   `sudo service apache2 restart`

- Access to the address like `127.0.0.1:5050` via your web browser.  
  (Replace `127.0.0.1` to your IP address, `5050` to your port number)
  - The other clients in the same network can access.
  - Run `sudo service apache2 restart` when you modify the codes
