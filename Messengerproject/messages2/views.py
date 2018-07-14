from django.shortcuts import render, redirect
from .models import Message
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms

import random
# from django.db.models.aggregates import Count
# from random import randint


# def message_list2(request):
#     count = self.aggregrate(count=Count('id'))['count']
#     random_index = randint(0, count - 1)
#     return self.all

#     random.choice(Model.objects.all())


# class message_random(models.Manager):
#     def random(self):
#         count = self.aggregate(count=Count('id'))['count']
#         random_index = randint(0, count - 1)
#         return self.all()[random_index]


# def message_list(request):
#     messages = random.choice(Message.objects.all())#.order_by('date')
#     return render(request, 'messages/message_list.html', {'messages': messages})#, {'messages': messages})


def message_list(request):
    messages = Message.objects.all()
    random_message = random.choice(messages)
    return render(request, 'messages/message_list.html', {'random_message': random_message})#{'random_message': random_message})

#     items = Product.objects.all()

# # change 3 to how many random items you want
# random_items = random.sample(items, 3)
# # if you want only a single random item
# random_item = random.choice(items)


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
