# Noter: A Python-Inspired Annotation API

## Welcome to Noter.

An ideal solution to your annotation needs. Firstly, we are offering this custom API that can be overrided anywhere and anytime. You can define your own handlers and models, but we are offering the basics you will need. From token-based authentication system to multi-user annotation services, we are here to annotate all the data. Please, follow along the next sections in order to learn more about this fantastic tool.

Noter is compatible with: **Python 3.6+**.

---

## Package guidelines

1. The very first information you need is in the very **next** section.
2. **Installing** is also easy, if you wish to read the code and bump yourself into, just follow along.
3. Note that there might be some **additional** steps in order to use our solutions.
4. If there is a problem, please do not **hesitate**, call us.

---

## Getting started: 60 seconds with Noter

First of all. Code is all commented. Yes, they are commented. Just browse to any file, chose your subpackage and follow it. We have high-level code for most tasks we could think of.

Or if you wish to learn even more, please take a minute:

Noter's API is based on the following structure, and you should pay attention to its tree:

```
- noter-api
    - decorators
        - auth
    - handlers
        - login
        - user
        - register
    - models
        - user
    - postman
```

### Decorators

Essentialy, you can define what you want in the decorators. They work like prior operations to another methods, being instanciated before them.

```auth```: Do you need to protect your resource? If yes, just add this decorator prior to your function and it will check if the incoming token is valid.

### Handlers

This is why we are called Noter. This will deal with all the inputs your users can perform. Again, you can define whatever your desire.

```login```: An handler for any login request.

```user```: A handler for any user-related requests.

```register```: A handler for registering new users.

### Models

Models are your database structure. You can define single models, relationships and much more! We are using the 'Yet Another Document Mapper' as our ODM. It will make things way easier when working with MongoDB.

```user```: An user model.

### Postman

This is where all the Postman's requests are. It will serve as a guide when working with this API. All avaliable requests will be defined here, and we will also provide all the input data needed to work with them.

---

## Installation

We belive that everything have to be easy. Not difficult or daunting, Noter will be the one-to-go package that you will need, from the very first instalattion to the daily-tasks implementing needs.

### Development

First of all, define the Python environment you are going to use (raw, conda, virtualenv) and enter it, for example:

```
conda activate <environment>
```

Next, install the needed requirements by performing the following commands:

```Python
pip install -r requirements.txt
```

Before running any application, create a ```config.ini``` file by copying it from ```config.ini.example```.

```
[API]
PORT = 8080
SECRET = 'thisshouldbealongsecret'

[MONGO]
STRING = mongodb://localhost:27017
DATABASE = noter
```

Finally, you can start the API:

```
python noter.py
```

Also, remember that you have to have a instance of MongoDB running. To use it, just open another terminal screen and type:

```
mongod
```

### Production

We are still working to finish this section.

---

## Environment configuration

Note that sometimes, there is a need for an additional implementation. If needed, from here you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Support

We know that we do our best, but it's inevitable to acknowlodge that we make mistakes. If you every need to report a bug, report a problem, talk to us, please do so! We will be avaliable at our bests at this repository or gth.rosa@uol.com.br.

---
