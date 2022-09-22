Part 1 
1) 
1. What is Thread and Multithreading?
Thread allows you to execute multiple threads at the same time. 
This is similar to multi-threading which allows the creation of multiple threads to run cocurrently.
2. What is Concurrency and Parallelism and what are the differences?
Concurrency is an application that performs multiple tasks at the same time, it is a method 
that is able to reduce response time of a system and this is done by using the CPU (central process unit).
Whereas Parallelism is an application in which tasks are broken down into small sub-tasks and
this is run simultaneously and it is processed in a parallel. This uses many processors.
3. What is Garbage collector? How does it work?
A Garbage collector deletes or destroys an object that is no longer need or is no longer being used. 
The purpose of this to make more memory. 
4. What is Transaction Management in a relational database (give an example)?
This is used to ensure that data is consistent, it is a unit of work that is performed on a database. It allows
you to access and perform logical units of a program.
5. What is an endpoint and what are the most common methods to interact with
the API data source?
An endpoint is a digital location in API and, it is the end of a communication channel, 
this allows two systems to connect and interact with each other. There are several ways
for an API data source to interact. The most commons ones are getting an API key and reviewing
the API.
6. What is data normalisation in SQL? Please provide an example (any) of a
database restructuring using primary/foreign keys to maintain data integrity.
Normalisation helps to organise data in a database, through this it deletes any data that
is no longer needed/redundant - this allows a database to improve its performance. 
Part 2 
2) Discuss Exception handling (4 pts) and debugging in Python.
When an error occurs in Python during its execution, it will show a runtime error. During this Python will stop and 
generate a message known as exception. These are built in exceptions and this will allow us to debug the 
code and repair it.
Try: This will usually generate an exception because the string is not defined. 
If this exception happens then the control flow will leave the block and go to the except block.
Except: This is only possible to run if an exception was raised by the try block. 
During this, if there is an exception it will not be caught by Python immediately and will just stop the program.
Else: If there are no exceptions raised in ‘except’ then this will need to be run. 
Again, if there is an exception it will not be caught automatically and Python will just stop the program.
Finally: This is necessary to always run and it is the last task to be executed.

3) Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new 
array of the same length with the squares of the original integers also sorted in ascending order.
Example Input:
numbers = [1,2,3,5,6,8,9]
Example Output:
[1,4,9,25,36,65,81]



4) Write tests for the newly created Sorted Squared Numbers
function (in Q3). Provide a brief explanation for your test case
options.

5) Agile methodology: name and describe any 2 of the main roles in a Scrum Agile team.
Scrum is a way to stay aligned through each phase of a project. It is a framework or a technique that allows different 
teams to be able to connect and align their work and make it better. These usually work in sprints, during this sprint a
daily scrum meeting is held. The scrum master and development team  are two of many main roles in a Scrum Agile team. 
The scrum master leads the team by helping facilitate the scrum to the team and during the scrum, they ensure that the 
framework is being followed. 
The development team are a group of teams that come together to deliver the results during a sprint. 


6) Discuss advantages and disadvantages of TDD (Test Driven
Development)
Test Driven Development is the process of writing unit tests before your code. There are a few advantages to this, for
instance there being less bugs in the code because the test is written before the code which means anything needs to be
fixed before the code is run. 
However, this can also come at a disadvantage because it means that a lot of tests will be run at once, which means that 
developers may not think to run the test as frequently as they should. Especially because the test are written in bulk. 

7) What is a Python DB cursor? Provide an example
DB cursor can execute a query by allowing Python to fetch records from a database, such as mySQL. 