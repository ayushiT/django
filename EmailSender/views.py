from django.http import HttpResponse

from django.core.mail import send_mail
from django.shortcuts import render
import sys
def home(request):
	return render(request,'home.html')
def Email(request):
	print(request.GET)
	MailTo=request.GET.get('mailTo')
	print("Mail to id",MailTo)
	
	Subject=request.GET.get('sub')
	print(Subject)
	
	send_mail(
    Subject,
    'learning django from beginning',
    'ayushitripathi800@gmail.com',
    [MailTo])
	
	return HttpResponse("<html><body>Hi There,Email Sent</body></html>")


    