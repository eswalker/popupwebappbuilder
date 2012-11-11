Running Pop-up Web App Builder:

Step 1:Put popup.py in the directory where you want your django project

Step 2: type the following in the terminal:
	sudo python popup.py
	*enter your password if prompted

Step 3: Fill out Pop-up Web App's simple form

Step 4: type 'yes' if you want access to the admin site *
	if 'yes', fill in username, email, and password

Step 5: type the following into the terminal:
	cd your_project_name
	python manage.py runserver 8000

Step 6: Go to localhost:8000 in your browser to see your running web app!^

Notes:
*When your site is running go to localhost:8000/admin to access the admin site
^To let others see your apps type python manage.py runserver 0.0.0.0:8000 into the terminal and have them type YourIPAddress:8000 in their browser