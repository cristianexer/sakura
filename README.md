# sakura

sakura is a hybrid between frameworks and it is binding Sanic and Prisma too implement this tool for the purpose of creating APIs very fast.

#### Why sakura ?

Well is quite simple, as Prisma it's generating everything for us, it still needs a graphql server to filter the exposed actions.

#### Why Sanic ?

Because Python.

#### What is special about sakura ?

Well, nothing really. It's just a cool approach to create a fully functional API crazy fast.

#### How is it working ?

The Sanic frameworks which looks pretty much like Flask, is masking the Prisma's API to filter the querys. However filtering is quite different of the graphql approach, we have an /ineed endpoint which purely expects to be given a query and the variables or the query name from the queryStorage and the variables.

#### Wait, what? What's the queryStorage ?

Well the queryStorage is the simple idea to store the queries in the database in a table called queryStorage, so we have queries with names as their unique identifier. So you can always call them by their name, update them in the database so you do not have to always deploy you app when you change something.

#### So still what is this thing ?

In a nutshell is some sort of black magic which needs a database schema, then it is generating everything for you. After that, if you need custom stuffs you can just create a new endpoint almost like you are usually doing. You already have the Authentication done with JWT, but you can still change that bit.


#### How scalable or secure is this witchcraft?

We do not know yet, but you can give it a try and help us to find out.


#### Let's start


```bash
docker-compose up -d
```


#### TODOS

- [ ] Authentication Middleware
- [ ] Role Middleware
- [ ] Seeding
- [ ] Backup
- [ ] Security Improvement
- [ ] Performance benchmarking
- [ ] Security benchmarking





