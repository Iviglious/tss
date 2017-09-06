Welcome for Treat SMA Sophoe
==================

This is the code for a fundraising website helping Sophie.


Info
----------------------------

This is sample Python 2.7 website with HTML, CSS and Javascript.

------------------------------


Functionalities
----------------------------

- Nice visuals: Materialize http://materializecss.com/

------------------------------


Technical details
----------------------------

- Core technology: Flask with Python 2.7 (RedShift template)
- Max Memory: 1GB
- Num. of CPUs: 1 core
- GitHub code: https://github.com/Iviglious/tss

------------------------------

Repo layout
===========
wsgi/ - Externally exposed wsgi code goes
wsgi/static/ - Public static content gets served here
libs/ - Additional libraries
data/ - For not-externally exposed wsgi code
setup.py - Standard setup.py, specify deps here
../data - For persistent data (also env var: OPENSHIFT_DATA_DIR)
.openshift/action_hooks/pre_build - Script that gets run every git push before the build
.openshift/action_hooks/build - Script that gets run every git push as part of the build process (on the CI system if available)
.openshift/action_hooks/deploy - Script that gets run every git push after build but before the app is restarted
.openshift/action_hooks/post_deploy - Script that gets run every git push after the app is restarted


Environment Variables
=====================

OpenShift provides several environment variables to reference for ease
of use.  The following list are some common variables but far from exhaustive:

    os.environ['OPENSHIFT_APP_NAME']  - Application name
    os.environ['OPENSHIFT_DATA_DIR']  - For persistent storage (between pushes)
    os.environ['OPENSHIFT_TMP_DIR']   - Temp storage (unmodified files deleted after 10 days)

When embedding a database using 'rhc cartridge add', you can reference environment
variables for username, host and password:

If you embed MySQL, then:

    os.environ['OPENSHIFT_MYSQL_DB_HOST']      - DB host
    os.environ['OPENSHIFT_MYSQL_DB_PORT']      - DB Port
    os.environ['OPENSHIFT_MYSQL_DB_USERNAME']  - DB Username
    os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']  - DB Password

To get a full list of environment variables, simply add a line in your
.openshift/action_hooks/build script that says "export" and push.


Notes about layout
==================
Please leave wsgi, libs and data directories but feel free to create additional
directories if needed.

Note: Every time you push, everything in your remote repo dir gets recreated
please store long term items (like an sqlite database) in ../data which will
persist between pushes of your repo.


Notes about setup.py
====================

Adding deps to the install_requires will have the OpenShift server actually
install those deps at git push time.