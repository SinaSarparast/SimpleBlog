# SimpleBlog

Hello, thank you for your interest in this project. SimpleBlog is a minimalist blog web application for people who want a simple platform to share their ideas, videos or pictures.
I try to make this repository friendly for new contributors who are interested in developing their product. You are free to contribute to this project by working on
issues or simply fork this repository and develop your product in any way you want.

# Prerequisites
You should know the basics of Django and managing a Django project.
Good knowledge of Python is also very helpful.
You should be comfortable working with the command line environment.

# How to set up the project
First, start by cloning this repository to your local machine.

```
git clone https://github.com/SinaSarparast/SimpleBlog.git
```

then go to the parent directory of where you have cloned this repository. For example, if you have cloned this repository to 'myprojects' directory go tho this repository
then create a virtual environment using the following command:

```
python3 -m venv simpleblog_env
```

After this step, activate your environment by using the command below.

```
source <path_to_simple_env>/simpleblog-env/bin/activate
```

Now, you are in the simple_env virtual environment, which means any package or library that you install in this environment is local to this environment and is not
available globally outside of this environment.

Now, install Django version 3.0 using pip:

```
pip install django
```

If you don't have Python installed try installing Python3 by replacing django with python3 in the command above. The packages installed are limited to your virtual environment
and each time you want to start the django server you need to activate this environment.

Now, you can change directory to the SimpleBlog directory, which you cloned earlier. Start the development server using the following command:

```
python manage.py runserver
```

The development server will start on "http://127.0.0.1:8000/" by default. You can reach the homepage through "http://127.0.0.1:8000/articles/home".

There is a django superuser available already:

username: admin
password: simpleblog

You can change the credentials using the django admin panel "http://127.0.0.1:8000/admin/auth/user/".
