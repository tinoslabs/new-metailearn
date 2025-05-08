from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .models import  Contact, Testimonial, Partners, TeamMembers, Blog, Service,CourseModel, CourseFAQ
from .forms import  ContactForm, TestimonialForm, PartnersForm, TeamForm, BlogForm, ServiceForm, CourseForm
# Create your views here.
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse 
import os

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def index(request):
    course = CourseModel.objects.all().order_by('-id')
    testimonials = Testimonial.objects.all().order_by('-id')
    instructor = TeamMembers.objects.all().order_by('-id')
    blog = Blog.objects.all().order_by('-id')
    partner = Partners.objects.all().order_by('-id')
    return render(request,'index.html',{'course':course,'testimonials':testimonials,'instructor':instructor,'blog':blog,'partner':partner})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "There was an error logging in, try again...")
            return redirect('user_login')
    return render(request, 'authenticate/login.html', {'form': True})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('index')

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})

def admin_dashboard(request):
    return render(request,'admin_pages/admin_dashboard.html')





def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


# def courses(request):
#     course = CourseModel.objects.all().order_by('-id')
#     return render(request,'courses.html',{'course':course})

def courses(request):
    course = CourseModel.objects.all().order_by('-id')
    return render(request, 'courses.html', {'course': course})



def course_details(request, id):
    course = get_object_or_404(CourseModel, id=id)
    all_courses = CourseModel.objects.all()  # exclude current course if desired
    return render(request, 'course_details.html', {
        'course': course,
        'all_courses': all_courses
    })


def add_faq(request):
    course_programs = CourseModel.objects.all()

    if request.method == 'POST':
        program_id = request.POST.get('course_program')  # ✅ This must match form field name

        if not program_id:
            return render(request, 'admin_pages/add_faq.html', {
                'course_programs': course_programs,
                'error': 'Please select a valid course.'
            })

        try:
            course_program = CourseModel.objects.get(id=program_id)
        except CourseModel.DoesNotExist:
            return render(request, 'admin_pages/add_faq.html', {
                'course_programs': course_programs,
                'error': 'Selected course does not exist.'
            })

        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if question and answer:
            CourseFAQ.objects.create(
                course_program=course_program,
                question=question,
                answer=answer
            )
            return redirect('list_faq')  # ✅ Ensure this URL name exists

        return render(request, 'admin_pages/add_faq.html', {
            'course_programs': course_programs,
            'error': 'Please fill in both question and answer.'
        })

    return render(request, 'admin_pages/add_faq.html', {'course_programs': course_programs})


def update_faq(request, id):
    faq = get_object_or_404(CourseFAQ, id=id)
    course_programs = CourseModel.objects.all()

    if request.method == 'POST':
        program_id = request.POST.get('course_program')
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if program_id:
            try:
                faq.course_program = CourseModel.objects.get(id=program_id)
            except CourseModel.DoesNotExist:
                return render(request, 'admin_pages/update_faq.html', {
                    'faq': faq,
                    'course_programs': course_programs,
                    'error': 'Selected course does not exist.'
                })

        faq.question = question
        faq.answer = answer
        faq.save()
        return redirect('list_faq')  # Ensure this exists in your urls.py

    return render(request, 'admin_pages/update_faq.html', {
        'faq': faq,
        'course_programs': course_programs
    })




def delete_faq(request,id):
    faq = CourseFAQ.objects.get(id=id)
    faq.delete()
    return redirect('list_faq')

# List all FAQs
def list_faq(request):
    faqs = CourseFAQ.objects.select_related('course_program').all()
    return render(request, 'admin_pages/list_faq.html', {'faqs': faqs})


def course_faq(request):
    return render(request,'course_faq.html')



def cyber(request):
    return render(request,'cyber_security.html')



def blog(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request,'blog.html',{'blog':blog})


def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog-details.html', {'blog': blog})


def instructors(request):
    team_members = TeamMembers.objects.all()
    return render(request, 'instructors.html', {'team_members': team_members})


def instructor_det(request):
    return render(request,'instructor-details.html')


def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    return render(request, 'service-details.html', {
        'service': service,
       
    })

def services(request):
    service = Service.objects.all().order_by('-id')
    return render(request, 'services.html', {'service': service})

def service_det(request):
    return render(request,'service-details.html')



def login(request):
    return render(request,'login.html')



def reg(request):
    return render(request,'register.html')


def gallery(request):
    return render(request,'gallery.html')


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_course') 
    else:
        form = CourseForm()

    return render(request, 'admin_pages/add_course.html', {'form': form})


def view_course(request):
    course = CourseModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_course.html', {'course': course})


def update_course(request, id):
    course = get_object_or_404(CourseModel, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'admin_pages/update_course.html', {'form': form, 'course': course})


def delete_course(request,id):
    coaching = CourseModel.objects.get(id=id)
    coaching.delete()
    return redirect('view_course')


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'admin_pages/add_testimonial.html', {'form': form})

def list_testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'admin_pages/list_testimonials.html', {'testimonials': testimonials})

def update_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('list_testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'admin_pages/update_testimonial.html', {'form': form})

def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    return redirect('list_testimonials')



def add_partners(request):
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_partners') 
    else:
        form = PartnersForm()

    return render(request, 'admin_pages/add_partners.html', {'form': form})


def view_partners(request):
    logo = Partners.objects.all().order_by('-id')
    return render(request,'admin_pages/view_partners.html',{'logo':logo})


def update_partners(request,id):
    logos = get_object_or_404(Partners, id=id)
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_partners')
    else:
        form = PartnersForm(instance=logos)
    return render(request, 'admin_pages/update_partners.html', {'form': form, 'logos': logos})


def delete_partners(request,id):
    logos = Partners.objects.get(id=id)
    logos.delete()
    return redirect('view_partners')



def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_team') 
    else:
        form = TeamForm()

    return render(request, 'admin_pages/add_team.html', {'form': form})


def view_team(request):
    team = TeamMembers.objects.all().order_by('-id')
    return render(request,'admin_pages/view_team.html',{'team':team})


def update_team(request,id):
    team = get_object_or_404(TeamMembers, id=id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('view_team')
    else:
        form = TeamForm(instance=team)
    return render(request, 'admin_pages/update_team.html', {'form': form, 'team': team})


def delete_team(request,id):
    team = TeamMembers.objects.get(id=id)
    team.delete()
    return redirect('view_team')


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_service') 
    else:
        form = ServiceForm()

    return render(request, 'admin_pages/add_service.html', {'form': form})


def view_service(request):
    service = Service.objects.all().order_by('-id')
    return render(request,'admin_pages/view_service.html',{'service':service})


def update_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('view_service')
    else:
        form = ServiceForm(instance=service)  # <-- fixed from instance=blog

    return render(request, 'admin_pages/update_service.html', {'form': form, 'service': service})


def delete_service(request,id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('view_service')


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog') 
    else:
        form = BlogForm()

    return render(request, 'admin_pages/add_blog.html', {'form': form})


def view_blog(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog.html',{'blog':blog})


def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)  # <-- Was TeamMembers
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin_pages/update_blog.html', {'form': form, 'blog': blog})


def delete_blog(request,id):
    blog = TeamMembers.objects.get(id=id)
    blog.delete()
    return redirect('view_blog')

def about(request):
    team = TeamMembers.objects.all().order_by('-id')
    reviews = Testimonial.objects.all().order_by('-id')
    partners = Partners.objects.all().order_by('-id')
    return render(request, 'about.html',{'team':team,'reviews':reviews,'partners':partners})







def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comment = request.POST.get("comment")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            comment=comment
        )
        messages.success(request, "Thank you! Your message has been submitted.")
        return redirect('contact')

    testimonials = Testimonial.objects.all()
    return render(request, 'contact.html', {'testimonials': testimonials})

def contact_list(request):
    contact = Contact.objects.all().order_by('-id')
    return render(request, 'admin_pages/contact_list.html', {'contact': contact})

def delete_contact(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact_list')

def blog(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog.html', {'blog': blog})


def testimonials(request):
    return render(request,'testimonial.html')