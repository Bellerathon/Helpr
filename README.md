# Helpr
Website that allows students to queue for help. 

# Context
First time using HTML, CSS and Javascript. 

# Details
<b>helpr.py</b> - Contains all the logic of the website, has a function for each feature on the website (view queue, cancel request etc..).  
<b>server.py</b> - Contains a basic FLASK server, that calls each function in helpr.py.  
<b>templates/mainpage.html</b> - A static file that serves as the main homepage for the webpage and contains most of the user facing features.  
<b>templates/adminpage.html</b> - A static file that serves as the administrator/tutor page that allows them to maipulate the queue and other higher privilege abilites.  

# How to run

1. Install dependencies from requirements.txt.
2. Run python3 server.py.
3. Click on generated URL.
4. check URL port is 5000 (not 5001).
