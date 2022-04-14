import datetime
from _csv import reader
from decimal import Decimal


from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView

from .forms import UploadPriceForm
from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'goods/items_list.html', {'items_list': items})


def upload_prices(request):
    if request.method=='POST':
        form = UploadPriceForm(request.POST, request.FILES)
        if form.is_valid():
            date_time = datetime.datetime.now().strftime("%d%m%Y-%H-%M-%S")
            new_file_name = date_time + '_' + request.FILES['file'].name
            price_file = request.FILES['file'].read()
            price_str = price_file.decode('utf-8').strip('\n').split('\n')
            csv_reader = reader(price_str, delimiter=":", quotechar='"')
            updated, item_count, added_codes = 0, Item.objects.count(), []
            for row in csv_reader:
                if not Item.objects.filter(code=row[1]):
                    added_codes.append(row[1])
                elif Item.objects.filter(code=row[1]).get().price == Decimal(row[2]):
                    pass
                else:
                    updated += 1
                Item.objects.filter(code=row[1]).update_or_create(name=row[0], code=row[1],
                                                                  defaults={'price': Decimal(row[2])})
            not_updated = item_count - updated
            added_codes = ' '.join(added_codes)
            if added_codes:
                added_codes = 'артикулы товаров, которых не было в базе данных: ' + added_codes
            else:
                added_codes = ''
            fs = FileSystemStorage()
            fs.save(new_file_name, request.FILES['file'])
            return HttpResponse(content='количество обновленных товаров - ' + str(updated) + '\n' +
                                          ' количество необновленных товаров - ' + str(not_updated) + '\n' +
                                          added_codes
                                , status=200)
    else:
        form=UploadPriceForm()
        context = {'form': form}
        return render(request, 'goods/upload.html', context=context)

class ItemDetail(DetailView):
    model = Item
    template_name = 'goods/items_detail.html'
    context_object_name = 'item'