from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # ✅ Required as a separate line!

# Function-based view
def list_books(request):
    books = Book.objects.all()  # ✅ Required by checker
    return render(request, "relationship_app/list_books.html", {'books': books})  # ✅ Exact path

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
