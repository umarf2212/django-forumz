from django.shortcuts import render
from django.http import HttpResponse
from .models import Dreamreal
from .forms import LoginForm
# Create your views here.
#admin password is 1234qwer
def hello(request):
	return HttpResponse("ma nigga ma nigga ma nig..")

def hello2(request):
	myname = request.GET.get('name', '')
	return render(request, "hello.html", {"name": myname})

def article(request, articleId):
	txt = "Displaying Article Number : %s" %articleId
	return HttpResponse(txt)


def crudops(request):

	#creating an entry
	dreamreal = Dreamreal(
		website = "www.polo.com",
		mail = "sorex@polo.com",
		name = "sorex",
		phonenumber = "0123456789"
	)

	#dreamreal.save()

	#Read all entries
	objs = Dreamreal.objects.all()
	res = 'Stuff: <br>'
	for i in objs:
		res += i.name + "<br>"
	
	return HttpResponse(res)

	#read a specific entry
	#sorex = Dreamreal.objects.all().filter(name="sorex")
	#res += "<br>"+sorex.name

	#Delete an entry
	#sorex.delete() #deletes first entry

	"""#Update
				dreamreal2 = Dreamreal(
					website = "www.polo.com",
					mail = "sorex@polo.com",
					name = "sorex2",
					phonenumber = "0123456789"
				)
				dreamreal2.save()
				dreamreal2 = Dreamreal.objects.get(name="sorex")
				dreamreal2.name = "thierry"
				dreamreal2.save()"""

def login(request):
	username = "not logged in"
	data2 = request.POST
	
	if (request.method == "POST"):
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			username = MyLoginForm.cleaned_data['username']
	else:
		MyLoginForm = LoginForm()

	return render(request, 'loggedin.html', {'username': username, 'data2': data2})
