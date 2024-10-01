from django.urls import path

from news.views import home_page_view, contact_page_view, category_page_view, single_page_view, news_detail_page

app_name = 'news'

urlpatterns = [
    path('contact/', contact_page_view, name='contact'),
    path('single/', single_page_view),
    path('category', category_page_view),
    path('<int:pk>', news_detail_page, name='news_detail_page'),
    path('', home_page_view, name='home'),
]
