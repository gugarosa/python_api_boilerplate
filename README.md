# Python-API: A Python-based API Boilerplate

## Welcome to Python-API Boilerplate.

An ideal solution to your boilerplate needs. Firstly, we are offering this custom API that can be overridden anywhere and anytime. You can define your handlers and models, but we are offering the basics you will need. From a token-based authentication system to multi-user annotation services, we are here to speed up all the projects. Please, follow along the next sections in order to learn more about this fantastic tool.

Python-API Boilerplate is compatible with: **Python 3.6+**.

---

## Package guidelines

1. The very first information you need is in the very **next** section.
2. **Installing** is also easy if you wish to read the code and bump yourself into, follow along.
3. Note that there might be some **additional** steps in order to use our solutions.
4. If there is a problem, please do not **hesitate**, call us.

---

## Getting started: 60 seconds with Python-API Boilerplate

First of all. Code is all commented. Yes, they are commented. Just browse to any file, chose your subpackage, and follow it. We have high-level code for most tasks we could think of.

Alternatively, if you wish to learn even more, please take a minute:

Python-API Boilerplate's is based on the following structure, and you should pay attention to its tree:

```
- python-api
    - decorators
        - auth
    - handlers
        - login
        - user
        - register
        - sample
    - models
        - user
        - sample
    - postman
```

### Decorators

Essentially, you can define what you want in the decorators. They work like prior operations to other methods, being instantiated before them.

```auth```: Do you need to protect your resource? If yes, add this decorator before your function, and it will check if the incoming token is valid.

### Handlers

This is why we are called Python-API Boilerplate. This will deal with all the inputs your users can perform. Again, you can define whatever you desire.

```login```: An handler for any login request.

```user```: A handler for any user-related requests.

```register```: A handler for registering new users.

```sample```: A handler for any sample-related requests.

### Models

Models are your database structure. You can define single models, relationships, and much more! We are using the 'Yet Another Document Mapper' as our ODM. It will make things way easier when working with MongoDB.

```user```: An user model.

```sample```: An sample model.

### Postman

This is where all the Postman's requests are. It will serve as a guide when working with this API. All available requests will be defined here, and we will also provide all the input data needed to work with them.

---

## Installation

We believe that everything has to be easy. Not tricky or daunting, Python-API Boilerplate will be the one-to-go package that you will need, from the very first installation to the daily-tasks implementing needs.

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
DATABASE = pythonapi
```

Finally, you can start the API:

```
python api.py
```

Also, remember that you have to have an instance of MongoDB running. To use it, open another terminal screen and type:

```
mongod
```

### Production

We are still working on finishing this section.

---

## Environment configuration

Note that sometimes, there is a need for additional implementation. If needed, from here you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository or gth.rosa@uol.com.br.

---
