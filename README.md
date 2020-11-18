# Football Tournament

##Setup

##### The first thing to do is to clone the repository:
#### $ git clone krishnapm642/football_tournaments
#### $ cd football_tournaments


##Create a virtual environment to install dependencies in and activate it:


## Then install the dependencies:

##### (env)$ pip install -r requirements.txt


(env)$ cd project
 
open two terminal and run the server and celery worker

(env)$ python manage.py runserver
(env)$ celery -A football_tournaments worker
