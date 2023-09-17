# Django-React
<h1>Setup<h1>
Creation of new application api -> need to add it into project.settings -> INSTALLED APP

Creation of new urls.py in the new app in order to let it manage the views

In project.urls use   path('', include('api.urls'))   in order to redirect the manage of path starting with '' to api.urls

in order to call a view use    path('', .view.function)