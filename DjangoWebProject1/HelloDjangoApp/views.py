#Makes an HTTP request and retuns an HTTP response in views.py

#importing packages (?) for use in functions
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
#Functions listed below

#def index(request): #Defines a view named index
#    now = datetime.now() #datetime imported above, calling for now

#    html_content = "<html><head><title>Hello, Django!</title></head>" 
        #Begins html content, assigns head and title to Hello Django and closes it
#    html_content += "<body><Strong>Hello django!</strong> on " + now.strftime("%A, %d, %B, %Y at %X")
        #begins body, in strong font, hello Django, displays time
        #now is the variable we initialized to the current time, strftime is the formatting library
        #structure is var.operator(?) 
#    html_content += "</body></html>"
        #closes out body and html script

#    return HttpResponse(html_content) #HttpResponse pulled from library above


#only dynamic part of code is now.strftime, all else is static and can be templated
#can replace entire code body as a template, with variables shown by {{ content }}
# Then when calling, use static code template and pass variables
    #add to installed apps list in main settings file

def index(request): #function definition
    now=datetime.now()

    return render( #Calling render function w/ args request, template, context
           request,
           "index.html", #reference to index tempalte would be file path, but in same folder.
           {
               'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d, %B, %Y at %X")
           }
    )

#Using the template from index.html and filling in data for content
#render helper function is for interfacing with page templates. request, index.html and content are all arguments in render
#request is calling to the path of the template
#NOTE: content is enclosed in {} and the entire call past render is enclosed in () as they are args to the render function