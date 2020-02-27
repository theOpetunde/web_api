# Solution to Coding Challenge - Projects and Actions

## Description
In this challenge, you design and create a web API to manage the following resources: Projects and Actions. 

## Instructions
### Minimum Viable Product
Design and build the necessary endpoints to: 
* Perform CRUD operations on projects and actions. When adding an action, make sure the project_id provided belongs to an existing project. If you try to add an action with an id of 3 and there is no project with that id the database will return an error. 
* Retrieve the list of actions for a project. 
* Deploy your application to Heroku free Dynos or Amazon free tier server or any other free hosting service and make it accessible through a postman client 
 
 ### Database Schemas
 The description of the structure and extra information about each resource stored in the database is listed below. 

#### Projects
 Field | Data Type | Metadata
------------ | -------------
id | number | no need to provide it when creating projects, the database automatically enerates it
name | string | required
description | string | required
completed | boolean | not required, used to indicate if the project is completed

#### Actions
Field| Data type | Metadata
------------ | -------------
id | number | automatically generated in the database
project_id | number | required, must be the id of an existing project
description | string | up to 128 characters long, required
notes | string | no size limit, required.