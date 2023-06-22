from django.shortcuts import render

# Create your views here.
def update_notice(request):
    return render(request, 'update_notice/update_notice.html')