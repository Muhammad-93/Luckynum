### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
   RESTful routing is a set of standards used in many different languages to create efficient, reusable routes. It aims to map HTTP methods (GET, POST, PATCH, DELETE) and CRUD actions (Create, Read, Update, Destroy) together in a conventional pattern.


- What is a resource?
    A resource is a representation of what the website's URL returns. It can be a file, JSON, or information. Once the resource is grabbed, the developer can decide what to do with it.



- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
  There is no reason to use render or redirect because building a JSON API passes the information from the route to a JSON dictionary in postgrSQL via POST.


- What does idempotent mean? Which HTTP verbs are idempotent?
  Idempotent means that the result is the same no matter how many times it is requested. However, the data requested CAN be changed. GET, PUT/PATCH, and DELETE are idempotent because the state of the server will always be the same after the HTTP verb occurs.

- What is the difference between PUT and PATCH?
  PUT updates the entire server while PATCH updates a small part of it.

- What is one way encryption?
   One way encryption is when only the user who created the account has access to the password itself non-reversibly. That way a company doesn't store the exact password in its database. However, a company can verify the password as the same input must always have the same output.


- What is the purpose of a `salt` when hashing a password?
  A cryptographic salt is made up of random bits added to each password instance before its hashing. Salts create unique passwords even in the instance of two users choosing the same passwords.
  

- What is the purpose of the Bcrypt module?
  The bcrypt hashing function allows us to build a password security platform that scales with computation power and always hashes every password with a salt


- What is the difference between authorization and authentication?
Authentication confirms that users are who they say they are. Authorization gives those users permission to access a resource

https://medium.com/@ratrosy/authorization-and-authentication-in-api-services-9b4db295a35b

-Python hash() method

Python offers hash() method to encode the data into unrecognisable value.