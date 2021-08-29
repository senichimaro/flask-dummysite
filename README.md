# Dummy Site
This exercise creates a TODOs app that is a basic CRUD operations app.

## Steps
1. [x] this first step builds the server a serves an index.html that render a data object JSON like: a python list.

2. [x] this second step replace the data object with a SQLAlchemy operation that query for all the row in a given table. A database connection is setup.

3. [x] Now let's modify this app to get a Todo App. The model is a simple database that have a single table which saves one field called 'description'. The view is one input in a form which targets '/todos/create' with POST method and a list item render. The controller catch the request body, create the record in the database, and redirects (by function name) to index to see this object loaded.

4. Setup Migrations. Migrations allow us to track database changes give us the opportunity to keep or discard changes and to move to previous versions. This comes very important to make changes in a secure manner and to handle/prevent data lost.
  - Setup Migrations.
    1. We'll use Flask-Migrate package `pip install Flask-Migrate`
    2. from `flask_migrate` import Migrate and pass app and db into an instance
    3. initialize migrations shell from CMD CLI `flask db init`
    4. initialize db version from CMD CLI `flask db migrate`
    5. implement version from CMD CLI `flask db upgrade`
    6. Changes to Database
      1. implement changes into their class
      2. db version `flask db migrate`
      3. apply `flask db upgrade`
      4. working with existing data **TOPIC**


## 4. working with existing data
Modify existing tables challenge existing data when constrains are required. The database could break and changes won't be applyed. To deal with this the version is manipulated to adecuate existing tables shapes to new table shapes setting placeholder values that new table shape needed to exist.

In this particular case, a mew column is added to an existing table with nullable constrain. Without manipluation the upgrade won't be applied because existing values will be updated will null values, directly challenging contrains.

The suggested solution is manipulate the version setting a "pre-step" where the new column is setted without constrains, then a SQL statement is executed to update all null values to the constrain value, and finally the column is altered to constrains requirements.

Example:
~~~
# Initial Constrain Requirement that crash ( nullable=False )
op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=False))

# Manipulation ( nullable=True )
op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
op.alter_table('todos', 'completed', nullable=False)
~~~
