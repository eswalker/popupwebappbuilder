'''
    Pop Up Web App Builder
    
    Authors: Ed Walker and Anastasia Georgiou
    Version: 1.0
    Created: 11/11/2012
    
    Description: Creates a fully functional django web app from simple user input.
    
    Winner of the Open Source Prize at the 2012 Princeton Hackathon
    
    
    To RUN:
    Step 1: Put popup.py in the directory where you want your django project
    
    Step 2: Type the following into the terminal:
	sudo python popup.py
	*enter your password if prompted
    
    Step 3: Fill out Pop-up Web App's simple form
    
    Step 4: Type 'yes' if you want access to the admin site *
	if 'yes', fill in username, email, and password
    
    Step 5: Type the following into the terminal:
	sudo chmod -R 777 your_project_name
	cd your_project_name
	python manage.py runserver 8000
    
    Step 6: Go to localhost:8000 in your browser to see your running web app!^
    
    *When your site is running go to localhost:8000/admin to access the admin site
    ^To let others see your apps type python manage.py runserver 0.0.0.0:8000 into the terminal and have them type YourIPAddress:8000 in their browser
    
    
    
    Note: All elements are in one file to increase portability
    Three major sections:
    1. Django Templates (Ed),
    2. Django Project Setup (Ed),
    3. Tkinter form (Anastasia)
    
    
'''


import os, shutil, random, sys, stat, subprocess,re
from Tkinter import *

###################################################################################
# Start of Django Templates
###################################################################################
DJANGO_TEMPLATES = {
'manage.py':
"""
#!/usr/bin/env python
import os
import sys
    
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "@project_name.settings")
    
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
""",
'settings.py':
"""
# Django settings for @project_name project.
import os
    
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          # ('Your Name', 'your_email@example.com'),
          )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '@cwd/@project_name/sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ( os.path.join(PROJECT_ROOT, '@model_name/static'), )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
                       'django.contrib.staticfiles.finders.FileSystemFinder',
                       'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
                       )

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@secret_key'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    #     'django.template.loaders.eggs.Loader',
                    )

MIDDLEWARE_CLASSES = (
                      'django.middleware.common.CommonMiddleware',
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      # Uncomment the next line for simple clickjacking protection:
                      # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
                      )

ROOT_URLCONF = '@project_name.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '@project_name.wsgi.application'

TEMPLATE_DIRS = (
                 # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
                 # Always use forward slashes, even on Windows.
                 # Don't forget to use absolute paths, not relative paths.
                 "@cwd/@project_name/templates",
                 )

INSTALLED_APPS = (
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  # Uncomment the next line to enable the admin:
                  'django.contrib.admin',
                  # Uncomment the next line to enable admin documentation:
                  # 'django.contrib.admindocs',
                  '@model_name',
                  )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
    }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
    }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
}
}
""",
'urls.py':
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Home page
    url(r'^$', '@model_name.views.home'),
                       
    # Admin documentation (uncomment to use)
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
    # Admin
    url(r'^admin/', include(admin.site.urls)),
                       
    #Element page
    url(r'^(?P<element_url>[a-zA-Z0-9_]+)/$', '@model_name.views.element_page'),
    )
""",
'wsgi.py':
'''
"""
WSGI config for @project_name project.
    
This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.
    
Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
    
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "@project_name.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
''',
'tests.py':
'''
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
    
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        "Tests that 1 + 1 always equals 2."
        self.assertEqual(1 + 1, 2)
''',
'admin.py':
'''
from django.contrib import admin
from @model_name.models import @model_name

class @model_nameAdmin(admin.ModelAdmin):
    fields = ['url','views', @field_name_list]
    list_display = ('url','views','created', 'last_viewed', @field_name_list)
    search_fields = ['url']

admin.site.register(@model_name, @model_nameAdmin)
''',
'models.py':
'''
from django.db import models
from django.forms import ModelForm


class @model_name(models.Model):
    url = models.CharField(max_length=50,primary_key=True)
    views = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(auto_now=True)
    
    @field_declarations
    
    def __unicode__(self):
        return self.url

class @model_nameForm(ModelForm):
    class Meta:
        model = @model_name
        exclude = ('views', 'created', 'last_viewed', @hidden_field_list)

''',
'views.py':
'''
from django.http import HttpResponse, HttpResponseRedirect
from @model_name.models import @model_name, @model_nameForm
from django.forms import ModelForm, Form
from django.shortcuts import render_to_response, render
from django.http import Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse

def home(request):
    if request.method == 'POST': # If the form has been submitted...
        form = @model_nameForm(request.POST) # A form bound to the POST data
        if form.is_valid() and not "/" in form.cleaned_data['url']: # All validation rules pass
            # Process the data in form.cleaned_data
            element = @model_name(
                                  url = form.cleaned_data['url'].lower().replace(' ','-'),
                                  views = 0,
                                  @field_assignments
                                  )
            element.save()
            return HttpResponseRedirect('/' + element.url) # Redirect after POST
    else:
        form = @model_nameForm() # An unbound form
    
    return render(request, '@model_name/home.html', {
                  'form': form,
                  })

def element_page(request, element_url):
    try:
        element = @model_name.objects.get(pk=element_url.lower())
    except @model_name.DoesNotExist:
        raise Http404
    
    element.views = element.views + 1
    element.save()
    return render_to_response('@model_name/element_page.html', {'@model_name': element})

''',
'element_page.html':
'''
<!DOCTYPE html><html><head>
    <title>{{@model_name.@primary_field}} - @project_name_text</title>
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap-combined.min.css" rel="stylesheet">
    <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js"></script>
    <style>div{margin-left:auto;margin-right:auto}</style>
</head>
<body style="text-align:center; margin-right:80px; margin-left:80px; margin-top:20px; background-color:#707070">
<div class="container-fluid">
    <div class="row-fluid">
        <!--Header content-->
    </div>
    <div class="row-fluid">
        <div class="span12">
            <div class="hero-unit" style="background-color:white">
                <h1>{{@model_name.@primary_field}}</h1>
                <p>@site_url/{{@model_name.url}}</p>
            </div>
        </div>
    <div class="row-fluid">
        <div class="well well-small span12" style="background-color:white">
            @field_table
        </div>
    </div>
    <div class="row-fluid">
        <div class="span12">
            <p>Made using Pop-up Web App Builder<i class="icon-leaf"></i></p>
            <p>{{@model_name.views}} page views</p>
        </div>
    </div>
</div>

</body></html>
''',
'home.html':
'''
<!DOCTYPE html><html><head>
    <title>@title</title>
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap-combined.min.css" rel="stylesheet">
    <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.2.1/js/bootstrap.min.js"></script>
    <style>div{margin-left:auto;margin-right:auto}</style>
</head>
<body style="text-align:center; margin-right:80px; margin-left:80px; margin-top:20px; background-color:#707070">
<div class="container-fluid">
    <div class="row-fluid">
    <!--Header content-->
    </div>
    <div class="row-fluid">
        <div class="span7">
            <div class="hero-unit" style="background-color:white">
                <h1>@title</h1>
                <p>@description</p>
            </div>
        </div>
        <div class="span5">
            <div class="hero-unit" style="background-color:white">
                <h3>Get Started in Seconds</h3>
                <form action="" method="post">{% csrf_token %}
                    {{ form.as_p }}
                    <input class="btn btn-large btn-primary" type="submit" value="Submit" />
                </form>
            </div>
        </div>
        <div class="row-fluid">
            <div class="span12">
                <p>Made using Pop-up Web App Builder<i class="icon-leaf"></i></p>
            </div>
        </div>
    </div>
</div>
</body></html>
''',
'script.sh':
'''#!/bin/bash
cd @project_name
python manage.py syncdb
''',
}



###################################################################################
# End of Django Templates
#
# Start of Django Project Setup
###################################################################################

CWD = os.getcwd()  # Current Working Directory

# file manipulation
def abspath(path_from_cwd):
    "Returns an absolute path"
    return CWD + '/' + path_from_cwd

def test_abspath(path_from_cwd):
    path = abspath(path_from_cwd)
    print path

def mkdir(path_from_cwd):
    "Makes a directory or overrides an existing directory"   
    path = abspath(path_from_cwd) # path to new directory
    if (os.path.isdir(path)):  # override if directory already exists 
        shutil.rmtree(path) 
    os.mkdir(path)  # make the directory

def test_mkdir():
    mkdir('testdir')
    mkdir('testdir/innertestdir')
    print "Expected true: " +  str(os.path.isdir(CWD + '/testdir/innertestdir/'))
    mkdir('testdir')
    print "Expected false: " + str(os.path.isdir(CWD + '/testdir/innertestdir/'))

def write_to_file(path_from_cwd, content):
    "Writes to a file in directory path, overrides if file already exists"
    path = abspath(path_from_cwd)
    file = open(path, 'w')
    file.write(content)

def test_write_to_file(path_from_cwd):
    write_to_file(path_from_cwd, "Hello World")
        
def file_mainpulation_tests():
    "tests mkdir, write_to_file, and abspath"
    test_mkdir()
    test_write_to_file('testdir/helloworld.txt')
    test_abspath('testdir')

# django file creation
#
# django file system (for reference)
# mysite/
#     manage.py
#     mysite/
#         __init__.py
#         settings.py
#         urls.py
#         wsgi.py
#     myapp/
#        __init__.py
#        admin.py
#        models.py
#        tests.py
#        views.py
#     templates/
#            myapp/
#                home.html
#                element_page.html
#

def create_django_project(site, form_fields):
    "Creates the file system to hold the django project"

    field_name_list = '' # all field names in variable form
    hidden_field_list = '' # all hidden field names in variable form
    for field in form_fields:
        field_name_list = field_name_list + "'" + field['field_name'] + "', "
        if not field['displayed']:
            hidden_field_list = hidden_field_list + field['field_name'] + ', '

    project_name = site['project_name']
    project_name_text = site['project_name_text']
    site_url = site['site_url']
    model_name = site['model_name']
    model_name_text = site['model_name_text']
    title = site['homepage_title']
    description = site['app_description']
    primary_field = site['primary_field']    

    
    # /mysite/
    path_from_cwd = project_name
    mkdir(path_from_cwd)
    create_manage_py(path_from_cwd, project_name)
    
    # /mysite/mysite/
    path_from_cwd = project_name + '/' + project_name
    mkdir(path_from_cwd)
    create_init_py(path_from_cwd)
    create_settings_py(path_from_cwd, project_name, model_name)
    create_urls_py(path_from_cwd, model_name)
    create_wsgi_py(path_from_cwd, project_name)
    
    # /mysite/myapp
    path_from_cwd = project_name + '/' + model_name
    mkdir(path_from_cwd)
    create_init_py(path_from_cwd)
    create_admin_py(path_from_cwd, model_name, field_name_list)
    create_models_py(path_from_cwd, model_name, form_fields, hidden_field_list)
    create_tests_py(path_from_cwd)
    create_views_py(path_from_cwd, model_name, form_fields)

    # /mysite/templates
    path_from_cwd = project_name + '/templates'
    mkdir(path_from_cwd)

    # /mysite/templates/myapp
    path_from_cwd = project_name + '/templates/' + model_name
    mkdir(path_from_cwd)
    create_element_page_html(path_from_cwd, site_url, model_name, primary_field, form_fields)
    create_home_html(path_from_cwd, title, description)

    # /
    path_from_cwd = ''
    create_script_sh(path_from_cwd, project_name)
    subprocess.call(['./script.sh'])
    os.remove(abspath('script.sh'))

def test_create_django_project():
    create_django_project('testproj', 'testmodel')

def create_manage_py(path_from_cwd, project_name):
    "Creates manage.py"
    content = DJANGO_TEMPLATES['manage.py']
    content = content.replace('@project_name', project_name)
    write_to_file(path_from_cwd + '/manage.py',content)

def create_init_py(path_from_cwd):
    "Creates __init__.py"
    write_to_file(path_from_cwd + '/__init__.py', '')

def create_settings_py(path_from_cwd, project_name, model_name):
    "Creates settings.py"
    content = DJANGO_TEMPLATES['settings.py']
    content = content.replace('@cwd', CWD)
    content = content.replace('@project_name', project_name)
    content = content.replace('@model_name', model_name)
    secret_key = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
    content = content.replace('@secret_key', secret_key)
    write_to_file(path_from_cwd + '/settings.py', content)

def create_urls_py(path_from_cwd, model_name):
    "Creates urls.py"
    content = DJANGO_TEMPLATES['urls.py']
    content = content.replace('@model_name', model_name)
    write_to_file(path_from_cwd + '/urls.py', content)

def create_wsgi_py(path_from_cwd, project_name):
    "Creates wsgi.py"
    content = DJANGO_TEMPLATES['wsgi.py']
    content = content.replace('@project_name', project_name)
    write_to_file(path_from_cwd + '/wsgi.py', content)

def create_admin_py(path_from_cwd, model_name, field_name_list):
    "Creates admin.py"
    content = DJANGO_TEMPLATES['admin.py']
    content = content.replace('@model_name', model_name)
    content = content.replace('@field_name_list', field_name_list)
    write_to_file(path_from_cwd + '/admin.py', content)

def create_models_py(path_from_cwd, model_name, form_fields, hidden_field_list):
    "Creates models.py"
    content = DJANGO_TEMPLATES['models.py']
    content = content.replace('@model_name', model_name)
    content = content.replace('@field_declarations', get_field_declarations(form_fields))
    content = content.replace('@hidden_field_list', hidden_field_list)
    write_to_file(path_from_cwd + '/models.py', content)

def create_tests_py(path_from_cwd):
    "Creates tests.py"
    write_to_file(path_from_cwd + '/tests.py', DJANGO_TEMPLATES['tests.py'])

def create_views_py(path_from_cwd, model_name, form_fields):
    "Creates views.py"
    content = DJANGO_TEMPLATES['views.py']
    content = content.replace('@model_name', model_name)
    content = content.replace('@field_assignments', get_field_assignments(form_fields))
    write_to_file(path_from_cwd + '/views.py', content)

def create_element_page_html(path_from_cwd, site_url, model_name, primary_field ,form_fields):
    "Creates element_page.html"
    content = DJANGO_TEMPLATES['element_page.html']
    content = content.replace('@site_url', site_url)
    content = content.replace('@model_name', model_name)
    content = content.replace('@primary_field', primary_field)
    content = content.replace('@field_table', get_field_table(model_name, form_fields))
    write_to_file(path_from_cwd + '/element_page.html', content)

def create_home_html(path_from_cwd, title, description):
    "Creates home.html"
    content = DJANGO_TEMPLATES['home.html']
    content = content.replace('@title', title)
    content = content.replace('@description', description)
    write_to_file(path_from_cwd + '/home.html', content)

def create_script_sh(path_from_cwd, project_name):
    "Creates script.sh and makes it executable"
    content = DJANGO_TEMPLATES['script.sh']
    content = content.replace('@project_name', project_name)
    write_to_file(path_from_cwd + 'script.sh', content)
    os.chmod(abspath('script.sh'), stat.S_IRWXU)

def get_field_table(model_name, form_fields):
    "Returns an html table with all displayable feilds and their values"
    content = '<table class="table table-striped table-bordered">'
    for field in form_fields:
        if field['displayed']:
            content = content + '<tr><td>' + field['field_name_text'] + '</td><td>{{' + model_name + '.' + field['field_name'] + '}}</td></tr>'
    content = content + '</table>'
    return content

def get_field_assignments(form_fields):
    "Returns a list of fields being assigned using the POST variable"
    content = ''
    for field in form_fields:
        content = content + field['field_name'] + " = form.cleaned_data['" + field['field_name'] + "'],\n"
    return content

def get_field_declarations(form_fields):
    "Returns a list of field declarations"
    type_map = {
        'True-False':'BooleanField(default=False',
        'Short Text (<150 characters)':'CharField(max_length=150,',
        'Email':'EmailField(',
        'Long Text (>150 characters)':'TextField(',
        'Integer':'IntegerField(',
        'Price':'DecimalField(max_digits=10, max_decimal=2,',
        'Floating-Point Number':'FloatField(',
        'True-False-Unknown':'NullBooleanField(',
        'IP Address':'IPAddressField(',
        'URL':'URLField(',
        'Date':'DateField(',
        'Time':'TimeField(',
    }
    content = ''
    for field in form_fields:
        content = content + field['field_name'] + ' = models.' + type_map[field['field_type']]
#        if field['optional']:
#            content = content + 'blank=True'
        content = content + ')\n    '
    return content


##################################################################################
# End of Django Project Setup
#
# Start of TKinter form
##################################################################################

site_data = {}

fields_dict = [] #list of field dictionaries
fields = []
numOfFields = 0
primaries = []


#creates a one line text field with a label. returns textfield entry
def makeTextFieldGrid(parent, caption, r, c, **options):
    Label(parent, text=caption).grid(row=r, column=c)#pack(side=TOP)
    entry = Entry(parent, **options)
    return entry

#creates a one line text field with a label. returns textfield entry
def makeTextField(parent, caption, **options):
    Label(parent, text=caption).pack(side=TOP)
    entry = Entry(parent, **options)
    return entry

#creates a multiple line text field with a label. returns textfield
def makeBigTextField(parent, caption, **options):
    Label(parent, text=caption).pack(side=TOP)
    text = Text(parent, **options)
    return text

#deletes an entire field row by removing each item in the last field row by
#removing it from grid
def deleteField():
    global numOfFields
    if numOfFields>1:
        for i in fields[numOfFields-1][0:len(fields[numOfFields-1])-2]:
            #-3 for the var's not displayed
            i.grid_remove()
        del fields[numOfFields-1]
        numOfFields = numOfFields-1

#displays one field row by placing each item in field row on grid
def displayField(fieldArray):
    global numOfFields
    for index in range(len(fieldArray)-2): #2 for the only information vars
        fieldArray[index].grid(row=numOfFields, column = index)

#adds one new field row
def newFieldArray():
    global numOfFields
    numOfFields=numOfFields+1
    fieldArray = []
    
    #adds Field Label
    label = Label(fieldFrame, text = "Field")
    fieldArray.append(label) #fieldArray[0]
    
    #Field Choices for drop down menu
    possiblechoices=['Date',
                     'Email',
                     'Floating-Point Number',
                     'Integer',
                     'IP Address',
                     'Long Text (>150 characters)',
                     'Price',
                     'Short Text (<150 characters)',
                     'Time',
                     'True-False',
                     'True-False-Unknown',
                     'URL']
    
    #sets up field selection drop down menu
    firstEntry = StringVar() 
    firstEntry.set("Date")
    option = OptionMenu(fieldFrame, firstEntry, *possiblechoices)
    fieldArray.append(option) #fieldArray[1]
    
    #
    fieldnamelabel = Label(fieldFrame, text = "Field Name")
    fieldname = StringVar()
    fieldBox = Entry(fieldFrame, textvariable = fieldname)
    fieldArray.append(fieldnamelabel) #fieldArray[2]
    fieldArray.append(fieldBox) #fieldArray[3]
    
    displayedvar = IntVar()   #####
    radio2 = Checkbutton(fieldFrame, text = "hidden", variable=displayedvar)
    fieldArray.append(radio2)   #fieldArray[4]
    
    
    fieldArray.append(firstEntry) #fieldArray[5]  #info var
    fieldArray.append(displayedvar) #fieldArray[6] #info var
    
    displayField(fieldArray)
    return fieldArray


def addField():
    fields.append(newFieldArray())
    #print "length of fields ", len(fields)


#creates individual field dictionary based off of a given field row
def extractFieldInfo(index):
    field_data = {}
    string=fields[index][3].get()
    field_data['field_name_text']=string
    string2=string.lower().replace(' ','_')
    field_data['field_name']=string2
    field_data['field_type'] = fields[index][5].get()
    hiddenvalue=fields[index][6].get()
    if hiddenvalue == 0:
        field_data['displayed'] = True
    else:
        field_data['displayed'] = False
    return field_data #dictionary

def validateField(index, i, type): #index=from loop i=3 type = 'field_name'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = fields[index][i].get()
    if len(string)<3 or string[0] not in alphabet or '-' in string:
        #print "error with field name!"
        return FALSE
    return TRUE

def allFieldValidate():
    for i in range(len(fields)):
        if validateField(i, 3, 'field_name') == FALSE:
            return FALSE
    return TRUE


#when you press the first submit button
def submitfirst():
    global primaries
    errorLabel.config(text="")
    if validate(projectName.get(), 'project_name') == FALSE:
        errorLabel.config(text="Error with Project Name")
    elif validate(modelName.get(), 'model_name') == FALSE:
        errorLabel.config(text="Error with Model Name")
    elif validateURL(siteURL.get(), 'site_url') == FALSE:
        errorLabel.config(text="Error with Site URL")
    elif allFieldValidate() == FALSE:
        errorLabel.config(text="Error with Field Name")
    else:
        errorFrame.destroy()

        for i in range(len(fields)):
            if i < len(fields_dict):
                fields_dict[i] = extractFieldInfo(i)
            else:
                fields_dict.append(extractFieldInfo(i))

        if numOfFields>=1:
            primaries.append(makeElement(primaryFrame, "Primary Field"))
        submitFrame2.pack(side=BOTTOM)#
        primaryFrame.pack(side=BOTTOM)#
        bottomFrame.pack(side=BOTTOM)
        errorFrame2.pack(side=BOTTOM)
        titleNameBox.focus()
        submitButton1.config(state="disabled")
        deleteFieldButton.config(state="disabled")
        addFieldButton.config(state="disabled")

#when you press the first submit button
def submitsecond():
    global primaries
    errorLabel2.config(text="")
    if titleName.get() == '':
        errorLabel2.config(text="Title required.")
    elif descriptionBox.get(1.0, END) == '\n':
        errorLabel2.config(text="Description required.")
    else:
        site_data['homepage_title'] = titleName.get()
        site_data['app_description'] = descriptionBox.get(1.0, END)
        if len(primaries) >= 1:
            site_data['primary_field'] = primaries[0].get()

        submitButton2.config(state="disabled")
        create_django_project(site_data, fields_dict)
        root.destroy()

def makeElement(parent, caption):
    global numbOfFields
    possibleChoices = []
    for i in range(numOfFields):
        possibleChoices.append(fields_dict[i]['field_name_text'])

    Label(parent, text=caption).grid(row = 0, column = 0)#.pack(side=TOP)
    primary = StringVar() #####
    primary.set(possibleChoices[0])
    primaryField = OptionMenu(parent, primary, *possibleChoices)
    primaryField.grid(row = 0, column = 1)##pack(side=TOP)
    return primary

def validate(string, type):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(string) < 3 or not string[0] in alphabet:
        return FALSE
    else:
        site_data[type+'_text'] = string
        string2 = string.lower().replace(' ', '_')
        string2 = string2.lower().replace('-', '_')
        site_data[type] = string2
        return TRUE

def validateURL(string, type):
    if len(string)==0:
        return FALSE
    string = string.replace('http://', '')
    string = string.replace('https://', '')
    site_data[type]=string
    return TRUE


######################################

root = Tk()
root.title("Pop-Up Web App Builder")

canvas = Canvas(root, width = 600, height = 5, bg = 'black')

###########ERROR FRAME################ (destroyed after validation)

errorFrame = Frame(root, pady=5)
errorLabel = Label(errorFrame, text="")
errorLabel.pack(side=BOTTOM)
errorFrame.pack()

############TOP HALF##################

topFrame = Frame(root, pady = 20)
topFrame.pack(side=TOP)

#field frame packed on, objects on frame on grid
fieldFrame = Frame(root)
fieldFrame.pack(side=TOP)

#sets up box for projectName and creates projectName variable
projectName = StringVar()
projectNameBox = makeTextFieldGrid(topFrame, "Project Name: ", 0, 0, textvariable = projectName)
projectNameBox.grid(row=1, column=0)#pack(side=TOP)

#sets up box for siteURL and creates siteURL variable
siteURL = StringVar()
siteURLBox = makeTextFieldGrid(topFrame, "Site URL: ", 0, 1, textvariable = siteURL)
siteURLBox.grid(row=1, column=1)#pack(side=TOP)

#sets up box for model Name and creates model name variable
modelName = StringVar()
modelNameBox = makeTextFieldGrid(topFrame, "Model Name: ", 0, 2, textvariable = modelName)
modelNameBox.grid(row=1, column=2)#pack(side=TOP)


#Adds first field
addField()

#sets up frame for buttons
buttonFrame=Frame(root, pady = 20)
buttonFrame.pack(side=TOP)

#Add field Button
addFieldButton = Button(buttonFrame, text = "Add Field", command = addField)
addFieldButton.grid(row = 0, column = 0)

#delete field Button
deleteFieldButton = Button(buttonFrame, text = "Delete Field", command = deleteField)
deleteFieldButton.grid(row = 0, column = 1)

#Submit field button
submitButton1 = Button(buttonFrame, text = "Submit", command = submitfirst)
submitButton1.grid(row = 0, column = 2)

projectNameBox.focus()

########BOTTOM HALF##############

errorFrame2 = Frame(root, pady=5)
errorLabel2 = Label(errorFrame2, text="")
errorLabel2.pack(side=BOTTOM)

bottomFrame = Frame(root)

#sets up box for titleName and creates titleName variable
titleName = StringVar()
titleNameBox = makeTextField(bottomFrame, "Homepage Title: ", textvariable = titleName)
titleNameBox.pack(side=TOP)

#description = StringVar()
descriptionBox = makeBigTextField(bottomFrame, "App Description:", height =4, wrap=WORD, bd=2, relief = RIDGE)
descriptionBox.pack(side=TOP)

primaryFrame = Frame(root)

submitFrame2 = Frame(root, pady = 10)

#Submit field button
submitButton2 = Button(submitFrame2, text = "Submit", command = submitsecond)
submitButton2.pack(side=RIGHT)

##################################

#puts everything on canvas
canvas.pack()
root.mainloop()


##################################################################################
# End of TKinter form
##################################################################################
