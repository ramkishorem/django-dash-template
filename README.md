Django application project template with my dashboard setup
===========================================================

This is a template to start a django project which brings in the dashboard skeleton that I start most of my applications with. The dashboard skeleton is used to build a more customized and friendly interface for the staff/superuser to use the backyard of the website.


## Steps to start a project

    1. Create project
        django-admin startproject --template=https://github.com/ramkishorem/django-dash-template/archive/master.zip project_name

    2. Create environment_settings.py alongside settings.py with template from settings.py

    3. Create first app after cd to folder containing app_template:
        django-admin startapp --template=app_template app_name

    4. Replace #firstAppName# with name of the app across the project

    5. Replace #firstAppTitle# with title of the app across the project


## License

The MIT License (MIT)

Copyright (c) 2017 Ramkishore M

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.