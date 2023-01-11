from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Articles, Informed
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DocsList(ListView):
    paginate_by = 3
    model = Articles
    template_name = 'docs/docs_home.html'
    context_object_name = 'docs'

    def get_queryset(self):
        return Articles.objects.order_by('-date').filter(is_published=True)



# def docs_home(request):
#     docs = Articles.objects.order_by( '-date')
#     # docs = Articles.objects.order_by('-date')[:3] для вывода трех записей с помощью среза
#     return render(request, 'docs/docs_home.html', {'docs': docs})


class DocsDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'docs/details_view.html'
    context_object_name = 'article'
    allow_empty = False


# class DocsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
class DocsUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'docs/docs_edit.html'
    form_class = ArticlesForm

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.group == self.request.group


class DocsDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('docs_home')
    template_name = 'docs/docs_delete.html'

class DocsCreateView(CreateView):
    form_class = ArticlesForm
    template_name = 'docs/create.html'
    success_url = reverse_lazy('docs_home')


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('docs_home')
#         else:
#             error = 'Форма была неверной'
#
#     form = ArticlesForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'docs/create.html', data)

class UserInformedList(ListView):
    paginate_by = 3
    model = Informed
    template_name = 'index.html'


    def get_queryset(self):
        return Informed.objects.order_by('user', 'status_informed').filter(is_published=True)