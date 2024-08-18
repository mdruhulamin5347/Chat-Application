from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from datetime import datetime
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from notifications.signals import notify



def HOME(request):
    return render(request,'home.html')


# @login_required
def ToDoList(request,username):
    if request.method == 'POST':
        work_time = request.POST.get('work_time')
        work_name = request.POST.get('work_name')
        if not work_time:
            messages.warning(request,'required work time')
        elif not work_name:
            messages.warning(request,'required work name')
        else:
            if To_do_list.objects.filter(work_time=work_time).exists():
                messages.warning(request,'work time allready exists!')
            else:
                user = User.objects.get(username=username)
                obj = To_do_list(work_time=work_time,work_name=work_name,username=user)
                obj.save()
                messages.success(request,'Successfully data submited!')
                return redirect('task_view', username=user.username)
    return render(request,'work_input.html')




def WorkView(request,username):
    user=User.objects.get(username=username)
    obj = To_do_list.objects.filter(username=user).order_by('work_time')
    context={
        'obj':obj,
        'user':user,
    }
    return render(request,'task_view.html',context)




def Update(request,id,username):
    user=User.objects.get(username=username)
    obj = To_do_list.objects.get(id=id)
    if request.method == 'POST':
        work_time = request.POST.get('work_time')
        work_name = request.POST.get('work_name')
        obj.work_time =work_time
        obj.work_name = work_name
        obj.save()
        messages.success(request,'Successfully data updated!')
        return redirect('task_view',username=user.username)
    if isinstance(obj.work_time, str):
        obj.work_time = datetime.strptime(obj.work_time, '%H:%M')
    formatted_work_time = obj.work_time.strftime('%H:%M') if obj.work_time else ''
    
    context = {
        'obj': {
            'work_time': formatted_work_time,
            'work_name': obj.work_name,
        }
    }
    return render(request, 'update.html', context)




def Delete(request,id,username):
    user=User.objects.get(username=username)
    obj = To_do_list.objects.get(id=id)
    obj.delete()
    messages.success(request,'Successfully data deleted!')
    return redirect('task_view',username=user.username)



# def mark_as_done(request, id, username):
#     user = User.objects.get(username=username)
#     obj = get_object_or_404(To_do_list, id=id, username=user)

#     if request.method == 'POST':
#         done_bol = 'Done' in request.POST
#         obj.done_bol = done_bol
#         obj.save()

#     return redirect('task_view', username=user.username)

    


def mark_as_done(request, id):
    user = request.user
    if request.method == 'POST':
        task = get_object_or_404(To_do_list, id=id)
        # Toggle the done_bol status
        task.done_bol = not task.done_bol
        task.save()
        return redirect('task_view', user)
    return redirect('task_view', user)






def success_day_view(request, username):
    user = User.objects.get(username=username)
    total_done_count = To_do_list.objects.filter(username=user).filter(done_bol=True).count()
        
    print(total_done_count)

    total_objects = To_do_list.objects.filter(username=user).count()
    if total_done_count:
        percentage_score = (total_done_count / total_objects) * 100
    else:
        percentage_score=None
    success_day_instance, created = Success_day.objects.get_or_create(username=user)
    success_day_instance.percentage_score = percentage_score
    success_day_instance.done_count = total_done_count
    success_day_instance.save()


    context = {
        'user': user,
        'total_done_count': total_done_count,
        'percentage_score': percentage_score,
        'total_objects':total_objects,
    }
    return render(request, 'success.html', context)







