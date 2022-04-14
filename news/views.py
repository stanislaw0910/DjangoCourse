from django.http import HttpResponseRedirect
from .forms import NewsForm, CommentForm
from django.views import View
from django.shortcuts import render
from .models import News, Comments
from django.views.generic import ListView, DetailView, UpdateView


class IndexNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news_list'
    queryset = News.objects.order_by('-created')


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['comments'] = Comments.objects.filter(news=pk)
        context['comment_form']=CommentForm()
        return context

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated and comment_form.cleaned_data['text']:
            Comments.objects.create(news_id=pk, username=request.user.username,
                                    user_id=request.user.id, text=comment_form.cleaned_data['text'])
        elif comment_form.is_valid():
            comment_form.cleaned_data['username'] = comment_form.cleaned_data['username'] + ' (anonymous)'
            Comments.objects.create(news_id=pk, **comment_form.cleaned_data)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class NewsCreateView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news/create_news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news')
        return render(request, 'news/create_news.html', context={'news_form': news_form})


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/update_news.html'
