from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Advertisement as advert
import random


"""class Advertisement(View):
    advertisements = advert.objects.all()
    count = 0

    def get(self, request):

        return render(request, 'advertisement/advertisements.html',
                      {'advertisements': Advertisement.advertisements, 'count': Advertisement.count})

    def post(self, request):
        Advertisement.count += 1
        return HttpResponse('New advertisement was successfully created\n')"""


class Categories(View):
    categories = [
        'Cleaning',
        'Teaching',
        'Repair',
        'Accounting'
    ]

    def get(self, request):

        return render(request, 'advertisement/categories.html', {'categories': Categories.categories})


class Contacts(TemplateView):
    template_name = 'advertisement/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_number'] = '+75555555555'
        context['email'] = 'notorious@gmail.com'
        context['title'] = 'Contacts'

        return context


class Regions(View):
    regions = [
            'Central Bohemia',
            'South Moravian',
            'Olomouc',
            'Vysocina',
            'Pardubice',
        ]

    def get(self, request):
        return render(request, 'advertisement/regions.html', {'regions': Regions.regions})

    def post(self, request):
        return HttpResponse('Region was successfully created\n')


class About(TemplateView):
    template_name = 'advertisement/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = "Do The Math"
        context['description'] = "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium," \
                      " totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae " \
                      "dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugi" \
                      "t, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro " \
                      "quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non " \
                      "numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim" \
                      " ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid" \
                      " ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse," \
                      " quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?" \
                      " At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum" \
                      " deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non" \
                      " provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et " \
                      "dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum" \
                      " soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere" \
                      " possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et " \
                      "aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et" \
                      " molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis" \
                      " voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

        return context


class Main_Page(View):
    def get(self, request):
        title = 'Main Page'
        return render(request, 'advertisement/index.html', {'categories': Categories.categories,
                                                             'title': title,
                                                             'regions': Regions.regions})


class RandomAdvert(View):
    def get(self, request):
        random.seed()
        advertisement=advert.objects.filter(id=random.randint(1, advert.objects.count()))

        return render(request, 'advertisement/advertisements.html',
                      {'advertisements': advertisement})


class AdvertisementListView(ListView):
    model = advert
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = advert.objects.all()


class AdvertisementDetailView(DetailView):
    model = advert
    template_name = 'advertisement/advertisement_detail.html'
    context_object_name = 'advertisement'


