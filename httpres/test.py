from django.http import HttpResponse
import time
def httpres(req):
    time.sleep(10)
    return HttpResponse('<h1>heheda</h1>')
~
