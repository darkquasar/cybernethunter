## *** Generic Config Parameters *** ##
## ********************************* ##

# jupyterhub_config.py
c = get_config()

import os
pjoin = os.path.join

runtime_dir = os.path.join('/opt/cybernethunter/jupyter/')
notebooks_dir = pjoin(runtime_dir, 'notebooks')
if not os.path.exists(notebooks_dir):
    os.makedirs(notebooks_dir)

# The location of jupyterhub data files (e.g. /usr/local/share/jupyterhub)
c.JupyterHub.data_files_path = '/opt/cybernethunter/conda3/share/jupyterhub'

# JupyterHub cookie secret and state db location (/opt/cybernethunter/jupyter)
c.JupyterHub.cookie_secret_file = pjoin(runtime_dir, 'cookie_secret')
c.JupyterHub.db_url = pjoin(runtime_dir, 'jupyterhub.sqlite')

# Interval (in seconds) at which to update last-activity timestamps.
c.JupyterHub.last_activity_interval = 300

# File to write PID Useful for daemonizing JupyterHub.
c.JupyterHub.pid_file = pjoin(runtime_dir, 'jupyterhub-proxy.pid')

## *** Network Config Parameters *** ##
## ********************************* ##
ssl_dir = '/opt/cybernethunter'
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = pjoin(ssl_dir, 'key.pem')
c.JupyterHub.ssl_cert = pjoin(ssl_dir, 'cert.pem')

# The public facing ip of the proxy
# c.JupyterHub.ip = '0.0.0.0'
# The public facing port of the proxy
# c.JupyterHub.port = 443
# The port for this process
c.JupyterHub.hub_port = 8081
# The ip for this process
c.JupyterHub.hub_ip = '127.0.0.1'
# Number of days for a login cookie to be valid. Default is two weeks.
c.JupyterHub.cookie_max_age_days = 5

## *** Load Service *** ##
## ******************** ##

#c.JupyterHub.services = [
#    
#           {
#              'name': 'cull_idle',
#              'command': ['/path/to/cull_idle_servers.py'],
#           }
# ]

## *** Spawner Parameters *** ##
## ************************** ##

# Use LocalProcessSpawner
# c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

# Use SudoSpawner
c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'

c.Spawner.cmd = ['jupyter-labhub']
c.Spawner.default_url = '/lab'
c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']
c.Spawner.start_timeout = 60

# start single-user notebook servers in notebooks_dir so students can load each other's notebooks
c.Spawner.notebook_dir = notebooks_dir
# c.Spawner.args = ['--NotebookApp.default_url=/notebooks/cybernethunter_welcome.ipynb']

# setting the amount of users that can spawn a notebook at the same time (default 100)
c.JupyterHub.concurrent_spawn_limit = 5


## *** Authenticator Parameters *** ##
## ******************************** ##

# General Settings
c.Authenticator.auth_refresh_age = 300
c.Authenticator.admin_users = {'cybernethunter'}

# Use Local Authenticator
c.LocalAuthenticator.create_system_users = True
c.LocalAuthenticator.add_user_cmd = ['sudo', 'adduser', '-q', '--gecos', '""', '--ingroup', 'jupyterhub', '--disabled-password']

# Use Dummy Authenticator
# c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
# c.DummyAuthenticator.admin_users = {'cybernethunter'}
# c.DummyAuthenticator.password = "cybernethunter"

# Use NativeAuthenticator
# c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
# c.Authenticator.open_signup = True