from django.shortcuts import render
from django.core.paginator import Paginator
from .models import NewNews

per_page = 3


def newnews_list(request):
    global per_page
    # получаем все посты
    posts = NewNews.objects.all().order_by('-created_at') # и отсортируем по дате
    if request.method == 'POST':
        per_page = request.POST.get('page_len')

    # создаем пагинатор
    paginator = Paginator(posts, per_page)  # per_page постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_obj = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'newnews.html', {'page_obj': page_obj})

# python manage.py runserver
