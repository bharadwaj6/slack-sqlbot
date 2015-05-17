# slack-sqlbot
Slack command that runs sql queries on your database right inside Slack.

Usage
-----
1. Fork the repo, and add your databases config to settings.py (read the warning below).

2. Push the app to heroku and note the heroku app URL.

3. Create a slack command for your team (whatever name you like) and specify the callback URL like this:


    `http://heroku-app-url-here/sql/`

4. That's it! Now you can execute your SQL this way:


    `/command_name SELECT something FROM somewhere;`
    
which gives you something like this inside slack:

    id1 something1 something2 
    id2 something3 something4

Warning!
--------

You can execute **ANY** SQL query like this!! 

Creating a new user with read-only permissions to the above database is recommended in most cases, to avoid any headaches.
