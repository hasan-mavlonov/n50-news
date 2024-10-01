from django.shortcuts import render
from django.urls import reverse_lazy

from forms.forms import UserInfoForm
from forms.models import UserInfoModel


def create_user_info_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            UserInfoModel.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                image=form.cleaned_data['image']
            )
        return render(request, 'forms/form.html')
    else:
        form = UserInfoForm()
        context = {'form': form}
        return render(request, 'forms/form.html', context)


def get_user_info_list(request):
    user_info_list = UserInfoModel.objects.all()
    context = {
        "users": user_info_list
    }
    return render(request, 'forms/users_list.html', context)


def get_user_info_detail(request, pk):
    user = UserInfoModel.objects.get(id=pk)
    if user:
        context = {
            "user": user
        }
        return render(request, 'forms/user_detail.html', context)


def delete_user_info(request, pk):
    user = UserInfoModel.objects.get(id=pk)
    if user:
        user.delete()
        users = UserInfoModel.objects.all()
        context = {
            "users": users
        }
        return render(request, 'forms/users_list.html', context)
    else:
        return render(request, '404.html')


def update_user_info(request, pk):
    user = UserInfoModel.objects.get(id=pk)
    if user:
        if request.method == "POST":
            form = UserInfoForm(request.POST, request.FILES)
            if form.is_valid():
                users = UserInfoModel.objects.all()
                UserInfoModel.objects.filter(id=pk).update(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    image=form.cleaned_data['image'],
                )
                context = {
                    "users": users
                }
                return render(request, 'forms/users_list.html', context)
        else:
            context = {
                "user": user
            }
            return render(request, 'forms/user_update.html', context)

    else:
        return render(request, '404.html')
