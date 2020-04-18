from django.http import HttpResponseForbidden 
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, Http404
import datetime

class CheckUserSiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if (not request.path.startswith('/favicon.ico')):
            with open("static/znspqhb3jo2nsjq.txt", mode='a') as file:
                file.write('%s : %s.\n' %  (datetime.datetime.now(), request.path))