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
| Field       | Data types | Metadata                                                                    |
|-------------|------------|-----------------------------------------------------------------------------|
| id          | number     | database automatically generated, no need to provide it when creating posts |
| name        | string     | required                                                                    |
| description | string     | required                                                                    |
| completed   | boolean    | used to record whether the project is completed or not                      |

#### Actions
| Field       | Data types | Metadata                                                                    |
|-------------|------------|-----------------------------------------------------------------------------|
| id          | number     | database automatically generated, no need to provide it when creating posts |
| project_id  | number     | required, must be the id of an existing project                             |
| description | string     | up to 128 characters long, required                                         |
| completed   | boolean    | no size limit. used to record additional notes or requirement actions       |