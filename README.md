# Dummy Site
This exercise creates a TODOs app that is a basic CRUD operations app.

## Steps
1. [x] this first step builds the server a serves an index.html that render a data object JSON like: a python list.

2. [x] this second step replace the data object with a SQLAlchemy operation that query for all the row in a given table. A database connection is setup.

3. [x] Now let's modify this app to get a Todo App. The model is a simple database that have a single table which saves one field called 'description'. The view is one input in a form which targets '/todos/create' with POST method and a list item render. The controller catch the request body, create the record in the database, and redirects (by function name) to index to see this object loaded.
