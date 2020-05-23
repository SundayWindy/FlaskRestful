# flask-restful

[![Build Status](https://travis-ci.com/RuiCoreSci/flask-restful.svg?branch=master)](https://travis-ci.com/RuiCoreSci/flask-restful) &nbsp; [![Coverage Status](https://coveralls.io/repos/github/RuiCoreSci/flask-restful/badge.svg?branch=master)](https://coveralls.io/github/RuiCoreSci/flask-restful?branch=master) &nbsp; [![codebeat badge](https://codebeat.co/badges/2c118356-0bab-4888-87a1-43acc91e9c72)](https://codebeat.co/projects/github-com-ruicoresci-flask-restful-master) &nbsp; ![python3.8](https://img.shields.io/badge/language-python3.8-blue.svg) &nbsp; ![framework](https://img.shields.io/badge/framework-flask--restful-blue) &nbsp; ![issues](https://img.shields.io/github/issues/RuiCoreSci/flask-restful) ![stars](https://img.shields.io/github/stars/RuiCoreSci/flask-restful) &nbsp; ![license](https://img.shields.io/github/license/RuiCoreSci/flask-restful)

* This is a web backend project based on the ```flask-restful```, coding in ```python3.8```.
* You can treat it as a template to **learn web-framework** or just simply **a start to use python** writing web project.
* This project use **Python Typing Hint**.

## Table of Contents

  - [1. Require](#1-require)
  - [2 Run](#2-run)
    - [2.1 Docker(Recommend)](#21-dockerrecommand)
    - [2.2. Shell](#22-shell)
    - [2.3. Load Sample Data](#23-load-sample-data)
  - [3. REST](#3-rest)
  - [4. Benefits of Rest](#4-benefits-of-rest)
  - [5. Unified Response Structure](#5-unified-response-structure)
  - [6. Unified Exception Handling](#6-unified-exception-handling)
  - [6. Unified Query Model, Response Model and DataBaseModel](#6-unified-query-model-reaponse-model-and-databasemodel)
      - [6.1. This Project Use Query Model for Request arguments:](#61-this-project-use-query-modle-for-requset-arguments)
      - [6.2. This Project Use Response Model for Response results:](#62-this-project-use-response-modle-for-response-results)
      - [6.3 This Project Use ORM for Managing Database](#63-this-project-use-orm-for-managing-database)
      - [6.4 This Project Use Alembic for Updating Database](#64-this-proejct-use-alembic-for-updating-database)
  - [7. Swagger or Not Swagger](#7-swagger-or-not-swagger)
  - [8. Structure of This Project](#8-structure-of-this-project)
      - [8.1 Model ( Models in this project): Store information about resources.](#81-model--models-in-this-project-store-information-about-resources)
      - [8.2 View (Resources in this project): Do Routing Work](#82-view-resources-in-this-project-do-routing-work)
      - [8.3 Controller (Handlers in this project): Do Logic Work](#83-controller-handlers-in-this-project-do-logic-work)
      - [8.4 Some Other Folders/Files](#84-some-other-foldersfiles)
  - [9. N + 1 Problem](#9-n--1-problem)
  - [10. The Downside of Rest](#10-the-downside-of-rest)
  - [11. Improvements](#11-improvements)
  - [12. Some Tools Should be Mentioned](#12-some-tools-should-be-mentioned)
  - [13. A Word](#13-a-word)
  - [Maintainers](#maintainers)
  - [Contributing](#contributing)
  - [License](#license)

## 1. Require

* Python3.8
* MySql（5.7 or above）

## 2 Run

### 2.1 Docker(Recommend)

1. install [docker](https://docs.docker.com/get-docker/) 
2. cd to project directory，run  ```make run ``` until it is finished.
* ```make run ``` will build docker image, start server (Mysql for example).
3. run ```make init``` to initial database (create database, create table , **No data is imported**).
* go to [localhost](http://0.0.0.0:24579/health) to check if it is start correctly.

**Note**: ```make test``` will run all unittest in folder ```tests```.
### 2.2. Shell

1. use command like ```CREATE DATABASE flask DEFAULT CHARSET utf8 ``` or GUI (such as [DataGrip](https://www.jetbrains.com/datagrip/)) tool to create database in your own db server.
2. modify ```SQLALCHEMY_DATABASE_URI``` and ```SQLALCHEMY_DATABASE_BASE``` in file ```settings.py``` to your own setting.
3. run:
```shell script
python3.8 -m venv --clear venv
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
4. go to [localhost](http://0.0.0.0:24579/health) to check if it is start correctly.

### 2.3. Load Sample Data

* If you want to load soma data to play with thin project, use ```data.sql``` in this project.
1. Open DataGrip, connect to Mysql Database;
2. Use any editor to open ```data.sql```,copy it's content to console, execute it;

* Using DataGrip, you should get someting like this:

![datagrip](https://github.com/RuiCoreSci/flask-restful/blob/master/datagrip.png?raw=false)

## 3. REST

* what is **REST** ? REST stands for **(Resource) Representational State Transfer**,it's a stateless communications protocol. The core concept of rest is **Resource**. In rest point of view, each concept that can be abstracted is called a Resource. Let's say name, age, email can be abstract as a User Model,so User can be represented as a Resource. 
* Transfer means resources are transferred from server side to clint side. 
* In rest world, each operation is operated on Some kind of resource, and has pre-defined **Verb** to describe it. Such as **Post** means to create a resource, **Put** means to update a resource, **Delete** means to delete a resource. These three Verb is mainly used,you can check it out [here](https://realpython.com/flask-connexion-rest-api/) for more detail.

## 4. Benefits of Rest

* Use REST,you will get some advantages:
1. Each **URI** (or URL) is for one specific Resource, it makes your code clean and **[self-describing](https://en.wikipedia.org/wiki/Self-documenting_code)**.Basically, self-describing means what you see is what you get,you can make a quick guess about what you will get from the uri.
2. Resource is separated from view function, which means you can change your backend logic function without affect others,only if your take the same arguments and return the same resource, which is easy to achieve.
3. It's is stateless, which means you don't need to worry about the surrounded context before you make request for resource.

## 5. Unified Response Structure

* Using Rest,we should make the response that we return **remain tha same**. In most Case，the response data should contains two parts: **meta** and **data**.
* **Meta** means the info about the request,is it a success or a failure ? Is it successfully understood by server but that request is not allowed ?
* **Data** means the resource that request want to get.
* In this project, the response  are defined as follow:

```python
{
    "data": data,
    "error_code": error_code,
    "error_msg": error_msg,
}
```
* For example, when a request want to get a user, let's say **User 1**, he may get:

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
* **Some thing you should aware**:
* Basically,we don't directly return json data in our handler function，instead we return object.
* So before return to frontend we should marshal our object to json format.
* In flask,you can use **jsonify** function to do this,to transfer costumed data to json，you can rewrite **json.JSONEncoder** function.
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
* And register to flask app:

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

* Exception **doesn't** means bad, on the other side, it's is crucial to let user know that they are doing something that the server can not satisfied. And they need to known why.
* In order to give the user corresponding error info, and to raise exception properly, this project use a file **exceptions** to clarify all exceptions

```py
class ServerException(Exception):
    code = 500


class ArgumentInvalid(ServerException):
    code = 400

```
* You may add a **message** property to each class.
* We want to raise exception in our code,a exception handler function is need:

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
* **Note**: If you want to raise exception directly in your code and don't want to write exception handler function, all Exceptions **must be** subclass of **werkzeug.exceptions.HTTPException**

## 6. Unified Query Model, Response Model and DataBaseModel

* In object oriented programming, it's better to keep your arguments to be a single object than many separated args. It's so in Python and Flask. 
* Let's say you want to query a user by it name and/or age and/or email, it's better to write:

```py
    def get_user(filter_obj):
        pass
```
* not:
```py
    def get_user(name,age,email):
        pass
```
#### 6.1. This Project Use Query Model for Request arguments:

```py
class BaseQueryModel(BaseModel):
    def __init__(self, **kwargs: dict):
        super().__init__(drop_missing=False, **kwargs)
        """ Some logic """
```
* And **Query Model args Validation** Can be write in BaseModel

#### 6.2. This Project Use Response Model for Response results:

```py
class BaseResponseModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """ Some logic """

```
* **Don't forget to jsonify your response model before return to frontend**.

#### 6.3 This Project Use ORM for Managing Database
* **Object-relational mapping** is used for communicate with database,it free you from writing SQL statements, keeps you **coding in Objected way**.

```python
from flask_sqlalchemy import SQLAlchemy

class Base(db.Model, SurrogatePK):
    """DataBase Model that Contains CRUD Operations"""

    __abstract__ = True

    """Some logic that all subclass should inherited """
```

#### 6.4 This Project Use Alembic for Updating Database

```py
from sqlalchemy.ext.declarative import declarative_base

Meta = declarative_base()
db = SQLAlchemy(model_class=Meta)

class Base(db.Model, SurrogatePK):
    """DataBase Model that Contains CRUD Operations"""
```

* **Alembic** is kind of like git,it keeps every version of your database model. It will generate a folder ```alembic```,```alembic/versions```,all versions are stored in ```versions```.

## 7. Swagger or Not Swagger

* Swagger provide an automatic way to generate documentation，so you don't need to update your docs yourself. Web frontend developer can check it out for developing.
* But in my experience，fronted developer and backend developer discuss Product Requirements before developing，automatic generated docs are not specified enough to declare requirements. So this project don't use it.
* If you want to use swagger,check it out [here](https://flask-restplus.readthedocs.io/en/stable/swagger.html).

## 8. Structure of This Project

![iamge](https://github.com/RuiCoreSci/flask-restful/blob/master/flask-restful.png?raw=false)

* **MVC(Model, View, Controller)** is a typical design pattern. This porject is programed in mvc pattern, but is not strictly stick to it.
#### 8.1 Model ( Models in this project): Store information about resources.
* Specifically, they are: 
  * Database Model,**ORM** is in this folder,which transfer your python object to database rows.
  * QueryModel, arguments  organized together as one Model. So frontend send args to backend, backend put them together to create a new object to do arguments validation work, because use Model,some default functions can be bound to it.
  * ResponseModel, resources that are returned to frontend.

#### 8.2 View (Resources in this project): Do Routing Work
* Views are handling routing work, when a url is request, view function know what logic function to call.

#### 8.3 Controller (Handlers in this project): Do Logic Work
* Handlers are used to to logic work,such as **CRUD** work.

#### 8.4 Some Other Folders/Files

* folder **exemptions** store customized exceptions file and a send error to DingDing file.
* folder **blueprints** is used to organize all apis.
* folder **tests** store all **unittest case**, **using test case** is a good way to keep project running well when new feature is developed.

## 9. N + 1 Problem

* Query one table 10 times each time fetch one row is slow than query one table one time to fetch 10 rows.
* **ORM** release programer from writing original sql statements,but it also introduce some new problems. The Database Query **N+1** Problem is a common one.
* Let's say you have two tables, **User** and **Post**, one user can write many posts. Consider the scenario blow:
* **you have a page which need to show ten random users' info, and also you are asked to show all posts for each user.**
* what will orm do in this scenario? **First**, query User Table **once** to get ten users; **Second**,for loop users to query Post Table for each user at one time, orm query Post Table **ten** times
* code would be something like this:

```py

users = User.query.limit(10) # query once

for user in users:
    posts = Post.query.filter_by(user_id==user.id)
# Query ten times
# All times Query Table is 1 + 10
```
* If you query User Table 1 time and get **N** users,then you need Query Post Table **N**  times to get posts,all times query tables are **1+N**, this is Called **N+1** Problem(May be called 1+N more reasonable).
* In fact,if you are familiar with join, there is no need to query N+1 times.
* So in your project,**Carefully** deal with this scenario.
* Facebook provide a solution called **DataLoader** to solve this.

## 10. The Downside of Rest

* Although REST has many advantages,it does has some disadvantages.
* The major downside is waste of resources, such as NetWork IO.
* In REST,you query a resource you get **all fields** of it. In many case,you just want a part of it.
* Another problem is url mixed,in REST,each resource need a url,when there are many resources, managing these urls could be a difficult problem.
* Because of all these, another framework **Graphql** is invented by FaceBook.
* In **Graphql**, there is one url,and you write query to request the fields that you want to get. It fix REST's problem.
* If you want to know more about graphql, check it out **here**.

## 11. Improvements
* In this project, some code can be abstracted as a base class. In **Handlers**, basically they all did CRUD work, with only different args and slightly different logic.
* If CURD work has been abstracted as a base class, the code could be cleaner.

## 12. Some Tools Should be Mentioned

* **Docker**,using docker to run project in different platform.
* **Docker-compose**,a tool that provides you easy way to manage docker.
* **Makefile**,auto compile tools that can save you a lot of time.
* **pre-commit**,auto format you code before you commit,these keep your project well formatted,especially useful when work in teams.
* **[travis-ci.com](https://travis-ci.com/)**, auto integration platform, which can run your tests automatically after you push.
* **[coveralls.io](http://coveralls.io/)**, get test coverage report after tests has been run,for example,you can use travis-ci for CI and let it send report to coveralls.
* **[codebeat.co](https://codebeat.co/)**, calculate the complexity of your code.
* **[shields.io](https://shields.io/)**, provide beautiful metadata badge for your project.You can just simply put your github repository url in blank,it will automatically generate suggested badges for you.

## 13. A Word
* This project is coded in Python3.8 using flask-restful framework, you can treat it as **a template to learn web-framework** or just simply a **start to use python writing web project**.
* I try to explain the framework clearly above, but if you find any mistake or want to improve the code ,you are **welcomed to contact me at hrui835@gmail.com**.
* If this project is helpful, **please click a Star**.
##  Maintainers

[@RuiCore](https://github.com/ruicore)

## Contributing

PRs are accepted.

Small note: If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2020 ruicore
