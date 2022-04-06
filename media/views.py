import codecs

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm, CheckFileForm


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name+' ' + str(file.size)+'b', status=200)
    else:
        upload_file_form = UploadFileForm()

        context = {
                'form': upload_file_form
            }
        return render(request, 'media/upload.html', context=context)


def check_file(request):
    if request.method == 'POST':
        check_file_form = CheckFileForm(request.POST, request.FILES)
        words = ['Это', 'слово', 'нельзя', 'использовать', 'Lorem']
        if check_file_form.is_valid():
            file = request.FILES['file']
            with file.open() as f:
                for chunk in f.chunks():
                    for i in words:
                        if i in str(chunk):
                            return HttpResponse(content='Файл не прошел проверку' + ' (' + i + ')', status=200)
                        elif i == words[-1]:
                            return HttpResponse(content='Всё хорошо', status=200)
    else:
        check_file_form = CheckFileForm()

        context = {
                'form': check_file_form
            }
        return render(request, 'media/upload.html', context=context)
