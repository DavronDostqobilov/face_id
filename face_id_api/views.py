from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from .models import Result,User
import json
import datetime
# import requests
# # Create your views here.

def result_add(request: HttpRequest):
    if request.method=='POST':
        data_post = request.body.decode('utf-8')
        data_post = json.loads(data_post)
        name = data_post['name']
        date=data_post['date']
        x = datetime.datetime(date)
        print(name,date)
        user_full_name = User.objects.get(name=name)
    
        entry = Result.objects.filter(name=name).first()
        if entry:
            entry_date = entry.date
        else:
            entry_date = None

        if entry_date==None or (entry_date.hour!=x.hour and entry_date.day==x.day):
            save_data = Result.objects.create(
                name = name,
                full_name = user_full_name,
                date=datetime.datetime.now(),
                comment='Entered'
                )
            save_data.save() 
            return JsonResponse({"status":"200"})    
        else:
            return JsonResponse({'Method': "error"})