from django.shortcuts import render, redirect
from .models import Message
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms
import random



def message_featured(request):
    messages = Message.objects.all()
    random_message = random.choice(messages)
    return render(request, 'messages/message_featured.html', {'random_message': random_message})

# def message_sent(request):
#     messages = Message.objects.all().order_by('date')
#     return render(request, 'messages/message_sent.html', {'messages': messages })

def message_sent(request):    
    user_messages = Message.objects.filter(author=request.user).order_by('-date')
    return render(request, 'messages/message_sent.html', {'user_messages': user_messages})

def message_detail(request, slug):
    #return HttpResponse(slug)
    message = Message.objects.get(slug=slug)
    return render(request, 'messages/message_detail.html', {'message': message})


@login_required(login_url="/accounts/login/")
def message_create(request):
    if request.method == 'POST':
        form = forms.CreateMessage(request.POST, request.FILES)
        if form.is_valid():
            # save message to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('messages2:list')
    else:
        form = forms.CreateMessage()
    return render(request, 'messages/message_create.html', {'form': form})


