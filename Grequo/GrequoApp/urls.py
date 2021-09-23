from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="IndexPage"),
    path("signup", views.userauthenticate, name="UserLogin"),
    path("logout", views.userlogout, name="UserLogout"),
    path("contactus", views.contactushandle, name="ContactUS"),
    path("aboutus", views.aboutus, name="AboutUs"),
    path('post/<int:post_id>', views.handlepost, name='GetUserPost'),
    path('post/delete/<int:id>', views.deletepost, name='DeletePost'),
    path('post/like/<int:post_id>', views.likepost, name='LikePost'),
    path('post/dislike/<int:post_id>', views.dislikepost, name='DislikePost')
]
