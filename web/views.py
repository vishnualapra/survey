from django.shortcuts import render,loader
from django.http import HttpResponse
from master import models

# Create your views here.
def index(request):
    files = []
    temp ='web/login.html'
    msg = ""
    if request.method == 'POST' and 'name' in request.POST:
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            try:
                user = models.Participants.objects.get(email=email)
                request.session['id'] = user.id
                request.session['name'] = user.full_name
                request.session['email'] = user.email
                if user.is_completed is True:
                    msg = "already_completed"
                    temp ='web/login.html'
                else:
                    fls = models.Files.objects.filter(status=True)
                    for i in fls:
                        try:
                            f = models.UserFiles.objects.get(file_details_id=i.id)
                        except:
                            f = models.UserFiles()
                            f.participant_id = user.id
                            f.file_details_id = i.id
                            f.save()
                    files = models.UserFiles.objects.filter(participant_id=user.id)
                    msg = "not_completed"
                    temp = 'web/index.html'

            except:
                user = models.Participants()
                user.full_name = name
                user.email = email
                user.save()
                fls = models.Files.objects.filter(status=True)
                for i in fls:
                    f = models.UserFiles()
                    f.participant_id = user.id
                    f.file_details_id = i.id
                    f.save()
                files = models.UserFiles.objects.filter(participant_id=user.id)
                request.session['id'] = user.id
                request.session['name'] = user.full_name
                request.session['email'] = user.email
                msg = "started"
                temp = 'web/index.html'


        except:
            msg = "error"
            temp ='web/login.html'
        request.session['username'] = 'vishnu'
    template = loader.get_template(temp)
    return HttpResponse(template.render({'files':files,'msg':msg},request))