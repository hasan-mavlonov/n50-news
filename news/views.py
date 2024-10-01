from django.shortcuts import render
from news.form import ContactModelForm, NewsletterModelForm
from news.models import NewsModel, NewsCollectionModel


def home_page_view(request):
    if request.method == 'POST':
        form = NewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'newsletter_success.html')
        else:
            context = {"errors": form.errors}
            return render(request, 'index.html', context)
    else:
        carousel_news = NewsCollectionModel.objects.filter(type='carousel').first().news.all()
        most_viewed_news = NewsModel.objects.all().order_by('views_count')[:6]
        latest_news = NewsModel.objects.all().order_by('-id')[:6]

        context = {
            "carousel_news": carousel_news,
            "most_viewed_news": most_viewed_news,
            "latest_news": latest_news
        }
        return render(request, 'index.html', context)


def news_detail_page(request, pk):
    news = NewsModel.objects.filter(pk=pk)
    if news.exists():
        news = news.first()
        news.views_count += 1
        news.save()
        context = {"news": news}
        return render(request, 'news_detail.html', context)
    return render(request, '404.html')


def single_page_view(request):
    return render(request, 'news_detail.html')


def contact_page_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
        else:
            context = {"errors": form.errors}
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')


def category_page_view(request):
    return render(request, 'category.html')
