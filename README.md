# simple-events
A Project for Events Management 

# step 1: Installing Modules and setup virtual Environment
if You have an existing environment with django and restframework libraries you can skip this step.
After Cloning the repository change the directory to root directory of project, command to create virtual environment using pip.

# pip install virtualenvwrapper
This install necessary modules which are used to create virtual environment.
# mkvirtualenv venv
This will creates a virtual environment venv.

# pip install -r requirements.txt
This will install all required libraries to run my django application.

# step 2 : running server on localhost
The default port is 8000
To run the server use the following command.
# python manage.py runserver <port>
A server will run on localhost at 8000 port default.

# step 3: Testing API
The working baseurl is 
# http://localhost:8000/api/   --baseurl

# GET http://localhost:8000/api/list_events/   
  This fetches all events which are existed.
  
  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/1ed242eb-464a-4e1e-bbaa-26db518675af)

# POST http://localhost:8000/api/list_events/
  This api is used to create event
  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/6753d04f-e146-4832-8e48-8450fcf8900a)
  
# GET http://localhost:8000/api/event_detail/{event_id}  
  This fetches the particular event data through the event_id
  Make sure replace the {event_id} with a proper event id value.
  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/6afdf5a5-1855-4ad3-85d4-035a0c0c07de)

  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/54e017b8-be68-44d7-900d-6e073919389e)


# POST http://localhost:8000/api/register_event/
  This takes a id and participant details.
  
  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/f94be0e4-371b-4d2d-aef8-4b2fa2733f5b)  

  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/0441712c-e789-426d-92aa-edc1da7f4e0b)
# Each Participant can only have unique email address

  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/6030a1ab-76c1-4b42-a0b5-2a6e8d5637d0)

# according to given assignment I linked only one participant to one event
  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/e4edc5c3-6db2-4624-9e46-4910b99f14cb)

  ![image](https://github.com/Hello-Sai/simple-events/assets/90458132/b4f4fa1e-49e2-435b-8e70-2e059efa3216)

