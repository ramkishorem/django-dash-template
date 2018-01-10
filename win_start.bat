e:
cd Projects/{{project_name}}
explorer .
start cmd.exe /c run.cmd
cd {{project_name}}/project-static/phy.scss
start cmd.exe /c watch.cmd
cd e:/Documents/sublimeprojects
start {{project_name}}.sublime-project
d:
start chrome "http://localhost:8000"
cd d:/Essentials/cmder
start cmder.exe e:/Projects/{{project_name}}