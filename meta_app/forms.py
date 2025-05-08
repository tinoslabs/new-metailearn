from django import forms
from .models import   Contact, Testimonial, Partners, TeamMembers, Blog, Service, CourseModel, CourseFAQ



class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
        
class CoachingFAQForm(forms.ModelForm):
    class Meta:
        model = CourseFAQ
        fields = ['course_program', 'question', 'answer']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'designation', 'rating', 'message', 'image']
        
class PartnersForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamMembers
        fields = '__all__'
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'