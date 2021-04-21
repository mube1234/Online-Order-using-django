from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from. import views
from .views import OrderApproveView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='homepage'),
    path('register/',views.registeration,name='register'),
    path('login/',views.user_login,name='login'),
    path('makeorder/',views.makeorder,name='orderpage'),
    path('homepageorder/<int:id>',views.homepageorder,name='homepageorder'),
    path('myorder/',views.myorder,name='myorder'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('customer/<str:id>', views.customerprofile, name='customer'),
    path('addnewproduct/', views.addnewproduct, name='addnewproduct'),
    #path('order-approve/<str:id>', views.order_approve, name='order-approve'),
    path('order/<int:pk>/approve/', OrderApproveView.as_view(), name='order-approve'),
    #path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('profile/', views.profile, name='profile'),
    path('addproductlist/', views.addproductlist, name='addproductlist'),
    path('editmakeorder/<int:id>', views.editmakeorder, name='editmakeorder'),
    path('deletemakeorder/<int:id>', views.deletemakeorder, name='deletemakeorder'),
    path('deleteorder/<int:id>', views.deleteorder, name='deleteorder'),
    path('password-change/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('suggestion/', views.give_suggeestion, name='suggestion'),
    path('suggestion/view',views.SuggestionListView.as_view(),name='view_suggestion'),
    path('logout/',views.user_logout,name='logout'),
]
if settings.DEBUG:#is used to load images from database to our browsers
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)