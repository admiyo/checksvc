import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from checksvc.forms import ServiceForm

import requests 


class HomePageView(View):
    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Service Connectivity Test</title>
            </head>
            <body>
              <form action="service"> 
              <label for="servce_url">Service URL: </label>
              <input type="text"  name="service_url"/>
              <input type="submit" />
              </form>
            </body>
            </html>
        ''' )
        return HttpResponse(response_text)

def render_services_page(service_url, status_code):
    return textwrap.dedent('''\
    <html>
    <head>
    <title>Service Test</title>
    </head>
    <body>
    <dl>
    <dt>URL</dt><dd>%s</dd>
    <dt>response code</dt><dd>%d</dd>
    </dl>
    <a href="addsvc">Add a new service</a>
    <a href="/">Service List</a>
    </body>
    </html>
    ''' % (service_url, status_code))
    
    

class ServicePageView(View):

    def get(self, request, *args, **kwargs):
        service_url =  request.GET.get("service_url")
        # sending get request and saving the response as response object
        r = requests.get(url = service_url)
            
        # extracting data in json format 
        data = r.json() 
        response_text = render_services_page(service_url, r.status_code)

        return HttpResponse(response_text)

    
def gen_list():
    return '<udl><li><a href="#">something</a></li></ul>'

class ServiceListView(View):

    
    def dispatch(request, *args, **kwargs):
        URL = "https://api.github.com"
        # sending get request and saving the response as response object 
        r = requests.get(url = URL) 
        # extracting data in json format 
        data = r.json() 
        
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Service Test</title>
            </head>
            <body>%s
            <a href="addsvc">Add a new service</a>
            </body>
            </html>
        ''' % gen_list())
        return HttpResponse(response_text)
