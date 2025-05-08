from django.urls import path
from . import views
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    
    path('user_login', views.user_login, name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    
    
     
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),
    
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    
    path('courses',views.courses,name='courses'),
    path('course_details/<int:id>/',views.course_details,name='course_details'),
    path('course_faq',views.course_faq,name='course_faq'),
    
    path('add_course',views.add_course,name='add_course'),
    path('view_course',views.view_course,name='view_course'),
    path('delete_course/<int:id>',views.delete_course,name='delete_course'),
    path('update_course/<int:id>',views.update_course,name='update_course'),
    
    
    path('add_faq', views.add_faq, name='add_faq'),
    path('update_faq/<int:id>', views.update_faq, name='update_faq'),
    path('delete_faq/<int:id>/', views.delete_faq, name='delete_faq'),
    path('list_faq/', views.list_faq, name='list_faq'),
    
    path('add_testimonial', views.add_testimonial, name='add_testimonial'),
    path('list_testimonials', views.list_testimonials, name='list_testimonials'),
    path('update_testimonial/<int:pk>/', views.update_testimonial, name='update_testimonial'),
    path('delete_testimonial/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
    
    path('add_partners', views.add_partners, name='add_partners'),
    path('view_partners', views.view_partners, name='view_partners'),   
    path('update_partners/<int:id>/', views.update_partners, name='update_partners'),
    path('delete_partners/<int:id>/', views.delete_partners, name='delete_partners'),
       
    path('add_team', views.add_team, name='add_team'),
    path('view_team', views.view_team, name='view_team'),   
    path('update_team/<int:id>/', views.update_team, name='update_team'),
    path('delete_team/<int:id>/', views.delete_team, name='delete_team'),
    
    
    path('add_blog', views.add_blog, name='add_blog'),
    path('view_blog', views.view_blog, name='view_blog'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
    
    path('add_service', views.add_service, name='add_service'),
    path('view_service', views.view_service, name='view_service'),
    path('update_service/<int:id>/', views.update_service, name='update_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    
    path('instructors', views.instructors, name='instructors'),
    
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    
    path('gallery', views.gallery, name="gallery"),
    
    
    path('blog-carousel',views.blog,name='blog-carousel'),
    path('blog',views.blog,name='blog'),
    path('blog_details/<int:id>/',views.blog_details,name='blog_details'),
    
    
    path('services',views.services,name='services'),
    path('service_details/<int:service_id>/',views.service_details,name='service_details'),
    
    path('service-details',views.service_det,name='service-details'),
    path('login',views.login,name='login'),
    path('register',views.reg,name='register'),
    path('instructor_det',views.instructor_det,name='instructor-details'),
    path('cyber_security',views.cyber,name='cyber_security'),

]