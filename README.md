# flask-restful

[![Build Status](https://travis-ci.com/RuiCoreSci/FlaskRestful.svg?branch=master)](https://travis-ci.com/RuiCoreSci/FlaskRestful) &nbsp; [![Coverage Status](https://coveralls.io/repos/github/RuiCoreSci/flask-restful/badge.svg?branch=master)](https://coveralls.io/github/RuiCoreSci/flask-restful?branch=master) &nbsp; [![codebeat badge](https://codebeat.co/badges/2c118356-0bab-4888-87a1-43acc91e9c72)](https://codebeat.co/projects/github-com-ruicoresci-flask-restful-master) &nbsp; ![python3.9](https://img.shields.io/badge/language-python3.9-blue.svg) &nbsp; ![framework](https://img.shields.io/badge/framework-flask--restful-blue) &nbsp; ![issues](https://img.shields.io/github/issues/RuiCoreSci/flask-restful) ![stars](https://img.shields.io/github/stars/RuiCoreSci/flask-restful) &nbsp; ![license](https://img.shields.io/github/license/RuiCoreSci/flask-restful)

* This is a web backend project based on the ```flask-restful```, coding in ```python3.9```.
* You can treat it as a template to **learn web-framework** or just simply **a start to use python** writing web project.
* This project uses **Typing** for typing hint.
* This project uses **Unittest** for testing.

## Table of Contents

  - [1. Require](#1-require)
  - [2. Run](#2-run)
    - [2.1 Docker(Recommend)](#21-dockerrecommend)
    - [2.2 Shell](#22-shell)
    - [2.3 Load Sample Data](#23-load-sample-data)
  - [3. REST](#3-rest)
  - [4. Benefits of Rest](#4-benefits-of-rest)
  - [5. Unified Response Structure](#5-unified-response-structure)
  - [6. Unified Exception Handling](#6-unified-exception-handling)
  - [7. Unified Query Model, Response Model and DataBaseModel](#7-unified-query-model-response-model-and-databasemodel)
      - [7.1 This Project Use Query Model for Request arguments](#71-this-project-use-query-model-for-request-arguments)
      - [7.2 This Project Use Response Model for Response Results](#72-this-project-use-response-model-for-response-results)
      - [7.3 This Project Use ORM for Managing Database](#73-this-project-use-orm-for-managing-database)
      - [7.4 This Project Use Alembic for Updating Database](#74-this-project-use-alembic-for-updating-database)
  - [8. Swagger or Not Swagger](#8-swagger-or-not-swagger)
  - [9. Structure of This Project](#9-structure-of-this-project)
      - [9.1 Model ( Models in this project): Store information about resources](#91-model--models-in-this-project-store-information-about-resources)
      - [9.2 View (Resources in this project): Do Routing Work](#92-view-resources-in-this-project-do-routing-work)
      - [9.3 Controller (Handlers in this project): Do Logic Work](#93-controller-handlers-in-this-project-do-logic-work)
      - [9.4 Some Other Folders/Files](#94-some-other-foldersfiles)
  - [10. N + 1 Problem](#10-n--1-problem)
  - [11. The Downside of Rest](#11-the-downside-of-rest)
  - [12. Improvements](#12-improvements)
  - [13. Some Tools Should be Mentioned](#13-some-tools-should-be-mentioned)
  - [14. A Word](#14-a-word)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
  - [License](#license)

## 1. Require

* Python3.9
* MySql（5.7 or above）

## 2. Run

### 2.1 Docker(Recommend)

* You can run this project either using Docker **or** Shell.

1. install [docker](https://docs.docker.com/get-docker/).
2. cd to project directory, run  ```make run ``` until it is finished.
* ```make run ``` will build docker image, start server (Mysql for example).
3. run ```make init``` to initial database (create database, create table , **No data is imported**).
* go to [localhost](http://0.0.0.0:24579/health) to check if it starts correctly.

**Note**: ```make test``` will run all unit tests in folder ```tests```.

### 2.2 Shell

1. use commands like ```CREATE DATABASE flask DEFAULT CHARSET utf8 ``` or GUI tool (such as [DataGrip](https://www.jetbrains.com/datagrip/)) to create a database in your own DB server.
2. modify ```SQLALCHEMY_DATABASE_URI``` and ```SQLALCHEMY_DATABASE_BASE``` in file ```settings.py``` to your own setting.
3. run:
```shell script
python3.11 -m venv --clear venv
```
```shell script
source ./venv/bin/active
```
```shell script
pip install -r requirements.txt
```
```shell script
python server.py
```
4. go to the [localhost](http://0.0.0.0:24579/health) to check if it starts correctly.

### 2.3 Load Sample Data

* If you want to load soma data to play with this project, use ```data.sql``` provided in this project.
1. Open **[DataGrip](https://www.jetbrains.com/datagrip/)** (a GUI tool for managing with database), connect to Mysql Database;
2. Use any editor to open ```data.sql```, copy it's content to console, execute it;

* Using [DataGrip](https://www.jetbrains.com/datagrip/), you should get something like this:

![datagrip](https://github.com/RuiCoreSci/flask-restful/blob/master/datagrip.png?raw=false)

## 3. REST

* what is **REST** ? REST stands for **(Resource) Representational State Transfer**, it's a stateless communications protocol. The core concept of rest is **Resource**. In **REST** point of view, each concept that can be abstracted is called a Resource. Let's say properties ```name```, ```age```, ```email``` can be abstract as a User Model, so ```User``` can be represented as a Resource.
* **Transfer** means resources are transferred from the server-side to the client-side.
* In **REST** world, each operation is operated on Some kind of resource, and has pre-defined **Verb** to describe it. Such as **Post** means to create a resource, **Put** means to update a resource, **Delete** means to delete a resource. These three Verb is mainly used, you can check it out [here](https://realpython.com/flask-connexion-rest-api/) for more detail.

## 4. Benefits of Rest

* Using REST, you will get some advantages:
1. Each **URI** (or URL) is for one specific Resource, it makes your code clean and **[self-describing](https://en.wikipedia.org/wiki/Self-documenting_code)**. Basically, self-describing means what you see is what you get, you can make a quick guess about what you will get from the URI.
2. Resource is separated from view function, which means you can change your backend logic function without affecting others, only if you take the same arguments and return the same resource, which is easy to achieve.
3. It's is stateless, which means you don't need to worry about the surrounded context before you make a request for resources.

## 5. Unified Response Structure

* Using Rest, we should make the response that we return to **remain the same**. In most cases, the response data should contain two parts: **meta** and **data**.
* **Meta** means the info about the request, is the request from client a success or a failure? Is it successfully understood by the server but the request is not allowed?
* **Data** means the resource that request want to get.
* In this project, the response  are defined as follow:

```python
{
    "data": data,
    "error_code": error_code,
    "error_msg": error_msg,
}
```
* For example, when a request want to get a user, let's say **User 1**, it may get:

```json

{
    "data": {
        "id": 1,
        "name": "John",
        "web_site": "https://github.com/account",
        "email": "hrui801@gmail.com",
        "create_time": "2020-05-22 13:41:49",
        "update_time": "2020-05-22 13:41:49"

    },
    "error_code": 0,
    "error_msg": "success"
}
```
* **Something you should be aware of**:
* Basically, we don't directly return JSON data in our handler function, instead we return an object.
* So before return to frontend we should marshal our object to JSON format.
* In flask, you can use **jsonify** function to do this, to transfer customized data to JSON, you can rewrite **json.JSONEncoder** function.
* In this project, the json.JSONEncoder is rewrite as:

```py
class JsonEncoder(json.JSONEncoder):
    def default(self, value) -> Any:
        if isinstance(value, (datetime.datetime, datetime.date)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(value, ApiResponse):
            return value.get()
        if isinstance(value, BaseModel):
            return value.marshal()
        if isinstance(value, types.GeneratorType):
            return [self.default(v) for v in value]

        return json.JSONEncoder.default(self, value)
```
* And then register it to flask app:

```py
    app.json_encoder = JsonEncoder
```
* Finlay, before you return data to frontend, call ```jsonify``` function:

```py
def schema(query_model: BaseQueryModel, response_model: ApiDataType):
    def decorator(func):

        @wraps(func)
        def wrapper(self, **kwargs) -> Callable:
            """Some logic """
            # jsonify function is called here
            return jsonify(func(self, **kwargs))

        return wrapper

    return decorator
```

## 6. Unified Exception Handling

* Exception **doesn't** mean bad, on the other hand, it's is crucial to let user know that they are doing something that the server can not satisfied. And they need to know why.
* In order to give the user corresponding error info, and to raise exception properly, this project uses a file **exception** to clarify all exceptions.

```py
class ServerException(Exception):
    code = 500


class ArgumentInvalid(ServerException):
    code = 400

```
* You may add a **message** property to each class.
* We want to raise exception in our code, a **unified exception handler function** is needed:

```py
def handle_exception(e) -> Tuple[Dict[str, Union[Union[int, str, list], Any]], Union[int, Any]]:
    code = 500
    if isinstance(e, (HTTPException, ServerException)):
        code = e.code

    logger.exception(e)
    exc = [v for v in traceback.format_exc(limit=10).split("\n")]
    if str(code) == "500":
        send_dingding_alert(request.url, request.args, request.json, repr(e), exc)
    return {'error_code': code, 'error_msg': str(e), 'traceback': exc}, code
```

* Then register to app:

```py
    app.register_error_handler(Exception, handle_exception)
```
* **Note**: If you want to raise exception directly in your code and don't want to write exception handler function, all exceptions **must be** a subclass of **werkzeug.exceptions.HTTPException**.

## 7. Unified Query Model, Response Model and DataBaseModel

* In object-oriented programming, it's better to keep your arguments to be a single object rather than many separated args. It's so in Python and Flask.
* Let's say you want to query a user by its **name** and/or **age** and/or **email**, it's better to write:

```py
    def get_user(filter_obj):
    # filter_obj will have property:name, age, email
        pass
```
* not:
```py
    def get_user(name, age, email):
        pass
```
#### 7.1 This Project Use Query Model for Request arguments

```py
class BaseQueryModel(BaseModel):
    def __init__(self, **kwargs: dict):
        super().__init__(drop_missing=False, **kwargs)
        """ Some logic """
```
* And **Query Mode's args Validation** Can be write in BaseModel.

#### 7.2 This Project Use Response Model for Response Results

```py
class BaseResponseModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """ Some logic """

```
* **Don't forget to jsonify your response model before return to the frontend**.

#### 7.3 This Project Use ORM for Managing Database
* **Object-relational mapping** is used to communicate with the database, it free you from writing SQL statements, keeps you **coding in objected way**.

```python
from flask_sqlalchemy import SQLAlchemy

class Base(db.Model, SurrogatePK):
    """DataBase Model that Contains CRUD Operations"""

    __abstract__ = True

    """Some logic that all subclass should be inherited """
```

#### 7.4 This Project Use Alembic for Updating Database

```py
from sqlalchemy.ext.declarative import declarative_base

Meta = declarative_base()
db = SQLAlchemy(model_class=Meta)

class Base(db.Model, SurrogatePK):
    """DataBase Model that Contains CRUD Operations"""
```

* **Alembic** is kind of like git, it keeps every version of your database model. It will generate a folder ```alembic```, ```alembic/versions```, all versions are stored in ```versions```.

## 8. Swagger or Not Swagger

* Swagger provides an automatic way to generate documentation, so you don't need to update your docs yourself. Web frontend developers can check it out for developing.
* But in my experience，fronted developer and backend developer discuss Product Requirements before developing, automatically generated docs are not specified enough to declare requirements. So this project don't use it.
* But it does no harm to use it, if you want to use swagger, check it out [here](https://flask-restplus.readthedocs.io/en/stable/swagger.html).

## 9. Structure of This Project

![image](https://github.com/RuiCoreSci/flask-restful/blob/master/flask-restful.png?raw=false)

* **MVC(Model, View, Controller)** is a typical design pattern. This project is programmed in MVC pattern, but is not strictly stick to it.
#### 9.1 Model ( Models in this project): Store information about resources
* Specifically, they are:
  * Database Model, **ORM** is in this folder, which transfers your python object to database rows.
  * QueryModel, arguments organized together as one Model. So frontend send args to backend, backend put them together to create a new object to do argument validation work, because use Model, some default functions can be bound to it.
  * ResponseModel, resources that are returned to the frontend.

#### 9.2 View (Resources in this project): Do Routing Work
* Views are handling routing work, when a URL is requested, view function know what logic function to call.

#### 9.3 Controller (Handlers in this project): Do Logic Work
* Handlers are used to do logic work, such as **CRUD**.

#### 9.4 Some Other Folders/Files

* folder **exemptions** store customized exception file and a send error to DingDing file.
* folder **blueprints** are used to organize all APIs.
* folder **tests** store all **unit test case**, **using a test case** is a good way to keep the project running well when a new feature is developed.

## 10. N + 1 Problem

* Query one table 10 times each time to fetch one row is slow than query one table one time to fetch 10 rows.
* **ORM** release programmer from writing original SQL statements, but it also introduces some new problems. The Database Query **N+1** Problem is a common one.
* Let's say you have two tables, **User** and **Post**, one user can write many posts. Consider the scenario below:
* **you have a page that needs to show ten random users' info, and also you are asked to show all posts for each user.**
* what will ORM do in this scenario? **First**, query User Table **once** to get ten users; **Second**, for loop users to query Post Table for each user at one time, ORM query Post Table **ten** times.
* code would be something like this:

```py

users = User.query.limit(10) # query once

for user in users:
    posts = Post.query.filter_by(user_id==user.id)
# Query ten times
# All times Query Table is 1 + 10
```
* If you query User Table 1 time and get **N** users, then you need Query Post Table **N**  times to get posts, all times query tables are **1+N**, this is Called **N+1** Problem(maybe called 1+N seems more reasonable).
* In fact, if you are familiar with join, there is no need to query N+1 times.
* So in your project, **Carefully** deal with this scenario.
* Facebook provides a solution called **DataLoader** to solve this.

## 11. The Downside of Rest

* Although REST has many advantages, it does have some disadvantages.
* The major downside is a waste of resources, such as NetWork IO.
* In REST, you query a resource you get **all fields** of it. In many cases, you just want a part of it.
* Another problem is URL mixed, in REST, each resource need a URL, when there are many resources, managing these URLs could be a difficult problem.
* Because of all these, another framework **Graphql** is invented by Facebook.
* In **Graphql**, there is one URL, and you write queries to request the fields that you want to get. It fixes REST's problem.
* If you want to know more about graphql, check it out **[here](https://graphql.org/learn/)**.

## 12. Improvements
* In this project, some code can be abstracted as a base class. In **Handlers**, basically they all did CRUD work, with only different args and slightly different logic.
* If CURD work has been abstracted as a base class, the code could be cleaner and simpler.

## 13. Some Tools Should be Mentioned

* **Docker**, using docker to run projects on different platforms.
* **Docker-compose**, a tool that provides you an easy way to manage docker.
* **Makefile**, auto compile tools that can save you a lot of time.
* **pre-commit**, auto-format you code before you commit, it keeps your project well-formatted, especially useful when working in teams.
* **[travis-ci.com](https://travis-ci.com/)**, auto integration platform, which can run your tests automatically after you push.
* **[coveralls.io](http://coveralls.io/)**, get test coverage report after tests have been run, for example, you can use Travis-ci for CI and let it send report to coveralls.
* **[codebeat.co](https://codebeat.co/)**, calculate the complexity of your code.
* **[shields.io](https://shields.io/)**, provide beautiful metadata badge for your project. You can just simply put your GitHub repository URL in blank, it will automatically generate suggested badges for you.

## 14. A Word
* This project is coded in Python3.11 using flask-restful framework, you can treat it as **a template to learn web-framework** or just simply a **start to use python writing web project**.
* I try to explain the framework clearly above, but if you find any mistake or want to improve the code, you are **welcomed to contact me at hrui835@gmail.com**.
* If this project is helpful, **please click a Star**.
##  Maintainers

[@RuiCore](https://github.com/ruicore)

## Contributing

PRs are accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2020 ruicore
