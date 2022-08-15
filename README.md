# Django Rest Framework - Internship tasks

This repository contains a base project for internship program at EBS Integrator, each candidate for position of Junior Backend Developer must be able to develop all the tasks in the following lists. Fork it and bring it to the next level. 

### Worflow

1. Before starting this program you should know Python or another programming language at a level beginner, and understand syntax, variables, functions, algorithms, etc. If you have lacked in language understanding then start with https://www.learnpython.org/
2. First milestone is to prove that you are ready for internship program
3. Before each milestone estimate each task in hours of work to understand how much time you need to achieve the finish, don't worry if your estimations are wrong because you don't have experience.
4. After each milestone or sequence of tasks create a merge request to your mentor to receive feedback, after code review you will have something to fix this will improve your coding skills
5. Be focused on tasks and ask questions when you don't understand something and you didn't find anything on Google (googling is a base skill for developers)

#### References

1. https://www.djangoproject.com/ - official documentation of Django framework 
2. https://www.django-rest-framework.org/ - documentation of DRF, an package for Django to transform it in a full REST API framework
3. https://restfulapi.net/ - documentation about REST APIs communication standard
4. https://github.com/ebs-integrator/rest-api-guide - A short REST API guide used in the company
5. https://swagger.io/docs/specification/2-0/what-is-swagger/
6. https://github.com/HackSoftware/Django-Styleguide - A styleguide for Django developers
7. https://www.django-antipatterns.com/ - A resource with most frequent mistakes in Django development

#### Project requirements
* [Python 3.8](https://docs.python.org/3.8)
* [Django 3.2](https://docs.djangoproject.com/en/3.2)

### First steps to run the project

Some steps before start work on tasks.

https://docs.djangoproject.com/en/3.2/intro/install/

1. Install python requirements ```pip install -r requirements.txt```
2. Database is SQLite, local, and execute ```python manage.py migrate```
3. Start the project ```python manage.py runserver```
4. Open website and register a user in /users/register/ endpoint
5. Login with registered credentials in /users/token/ endpoint
6. In swagger click "Authorize" button and type ```Bearer <access token from response>```
7. Let's do first milestone!

### Milestone 1

We start with some changes to understand the project code

#### What will you learn

1. How to add new fields in Django Models
2. How to add new Django Models entities
3. How to create a new API endpoint that add data in database
4. How to manage information in Django Admin

#### Tasks

1. Add in Blog model a boolean field ```enabled``` to make some posts published or unpublished (ref: https://docs.djangoproject.com/en/3.2/ref/models/fields/#booleanfield)
2. Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8 (ref: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table (ref: https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
4. Create a new model ```Comments``` with ```text``` and ```blog``` foreign key, here we will save comments for each blog post.
5. Add Comments for management in Django Admin (ref: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#modeladmin-objects)
6. Create an endpoint that creates a comment to a blog post (input: blog_id, text)
7. In endpoint ```/blog/blog/{id}/``` return the Blog post object and list of comments.