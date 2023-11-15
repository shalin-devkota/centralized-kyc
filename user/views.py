from django.shortcuts import render,HttpResponse

# Create your views here.
def get_email_view(request):
    return render (request,"user/get_email_view.html")

def verify_email(request):
    email = request.POST.get("email")
    print(email)
    return HttpResponse("nice")
