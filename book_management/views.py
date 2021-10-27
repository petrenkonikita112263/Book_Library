from django.http import HttpResponse
from django.views.generic import FormView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views import View
from .forms import BookForm
from .models import Book


class BookRecordFormView(FormView):
    template_name = "book_management/book_form.html"
    form_class = BookForm
    success_url = "/book_management/entry_success"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully!")


class BookUpdateView(CreateView):
    model = Book
    fields = ["name", "author"]
    template_name = "book_management/book_form.html"
    success_url = "/book_management/entry_success"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_management/book_delete_form.html"
    success_url = "/book_management/delete_success"


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record deleted successfully!")


class BookRecordDetailView(DetailView):
    model = Book
    template_name = "book_management/book_detail.html"
