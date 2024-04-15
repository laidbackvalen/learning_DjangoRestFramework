# Views are where you define the logic for handling HTTP requests and generating responses. With Django REST Framework, you can use class-based views or function-based views.

from django.http import HttpResponse, JsonResponse
def home_page(request):
   print("Home Page Requested")
   friends=["valen", "rajubhai", "patel"]
   return JsonResponse(friends, safe=False)
#    return HttpResponse("This is home page") 
