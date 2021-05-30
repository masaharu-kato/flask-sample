"""
    Entry script for WSGI application
"""

import os
import sys
import site

# Set project root and python site directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SITE_DIR = os.path.join(PROJECT_ROOT, 'env/lib/python3.8/site-packages')

# Specify python path
site.addsitedir(SITE_DIR)

# Specify project path and run application
sys.path.insert(0, PROJECT_ROOT)

# Set current directory to project root
os.chdir(PROJECT_ROOT)

# Check defualt encoding is UTF-8
assert sys.getdefaultencoding() == 'utf-8', "Default encoding is not 'utf-8'."

# The module named 'application' will be executed
from main import app as application
