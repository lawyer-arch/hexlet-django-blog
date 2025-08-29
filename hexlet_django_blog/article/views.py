from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(View):
    def get(self, request, tags=None, article_id=None, *args, **kwargs):
        if tags is None and article_id is None:
            home_page = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
            return redirect(home_page)
        else:
            formatted_text = f"Статья номер {article_id}. Тег {tags}"
            return render(
                request, 
                'article/index.html', 
                context={'article_title': formatted_text}
            )

