StackAnalyze
============

Live Demo
---------
* [https://cryptic-beach-92808.herokuapp.com/](https://cryptic-beach-92808.herokuapp.com/)

How to run?
------------
* `git clone git@github.com:vipul-sharma20/stack-analyze.git`
* `cd stack-analyze`
* `sudo pip install virtualenv` (if virtualenv not installed)
     * Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already.
     * If you don't have pip installed, visit here to see steps to install virtualenv: [https://virtualenv.readthedocs.org/en/latest/installation.html](https://virtualenv.readthedocs.org/en/latest/installation.html)
* `virtualenv so`
* `source so/bin/activate`
* `pip install -r requirements.txt` (wait till the requirements are installed)
* `python manage.py syncdb`
* `python manage.py getdata` (Read Below for explanation)
* `python manage.py runserver` This will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Getting the data
----------------
A custom `django-admin` command is created to get the data of top 50 tags from
StackOverflow and populate the models. Use:
* `python manage.py getdata` (This may take some time to make requests and store the data)

This command runs `script.py` of the app to make API requests and store data into the DB