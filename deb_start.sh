#!/bin/bash

xdg-open .
gnome-terminal -e 'python3 manage.py runserver'
cd {{project_name}}/project-static/phy.scss
gnome-terminal -e 'sass --watch phy.scss:../css/style.min.css --style compressed'
xdg-open "http://localhost:8000"
cd ~/Documents/sublime/
xdg-open {{project_name}}.sublime-project
