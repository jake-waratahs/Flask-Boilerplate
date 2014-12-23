Deployment
==================================================

Deployment Using Supervisor
***************************************

Debian, Ubuntu and Similar
#######################################

#. Install Supervisor (Only do this for the first time you deploy on the server)

    .. code-block:: bash
        
        sudo apt-get update
        sudo apt-get install python3 python3-dev python3-setuptools
        sudo apt-get install supervisor
        sudo service supervisor restart
        sudo easy_install3 pip


#. Copy your project to the server. I recomend you use some sort of git webhook setup that automatically pulls new changes whenever they are pushed to the repository. 

#. Perform the standard installation method of the project and double check it runs.
    
    .. code-block:: bash

        cd /path/to/project/
        pip3 install -r requirements.txt
        ./app


#. edit: ``/etc/supervisor/conf.d/my_app.conf``

    .. code-block:: bash

        sudo vim /etc/supervisor/conf.d/my_app.conf


    Fill it with: (Replacing the placeholders). The argument -p tells meinheld to host the app on port 80.

    .. code::

        [program:<MYAPP>]
        command=/path/to/project/app meinheld -c Production -p 80
        directory=/path/to/project/
        autostart=true
        autorestart=true
        stderr_logfile=/path/to/project/<MYAPP>.err.log
        stdout_logfile=/path/to/project/<MYAPP>.out.log


    .. code-block:: bash
        
        sudo service supervisor restart
        sudo supervisorctl reload
        sudo supervisorctl start MYAPP

#. You're done!
    If you're having trouble, attempt to run /path/to/project/app manually and see what's going on.