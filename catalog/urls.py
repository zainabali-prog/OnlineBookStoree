from django.urls import path
from . import views

urlpatterns = [

    path('', views.newindex, name='newindex'),
    path('books', views.BookListView.as_view(), name='books'),
    path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('borrowed/', views.LoanedBooksByAllUsersListView.as_view(), name='all-borrowed'),
    
    path('contact.html', views.contact, name='contact'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('thankyou.html', views.thankyou, name='thankyou'),
    path('login.html', views.login, name='login'),
    path('update_item', views.updateItem, name='update_item'),
   
]
