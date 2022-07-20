from doctest import testfile
from email.mime import image
from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from .models import CategoryModel, PhotoModel, ProfileModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView,CreateView,DetailView
from django.urls import reverse_lazy

from .forms import ProfilePageForm,AddPhotoGamesForm


class HomeView(TemplateView):

    template_name = 'minhagaleria/home.html'

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('minhagaleria:home')

    return render(request, 'minhagaleria/login.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('minhagaleria/home')

    context = {'form': form, 'page': page}
    return render(request, 'minhagaleria/register.html', context)


@login_required(login_url='login')
def gallery(request,pk):

    user = request.user
    categories = CategoryModel.objects.all()
    image_all = PhotoModel.objects.filter(id=6)
    image_objeto = PhotoModel.objects.all()
    category_pessoa = CategoryModel.objects.filter()
    context = {'categories': categories,'image_objeto':image_objeto,'image_all':image_all}
    return render(request, 'minhagaleria/gallery.html', context)

@login_required(login_url='login')
def gallery_test(request):

    user = request.user
    categories = CategoryModel.objects.all()

#images variables
    image_all = PhotoModel.objects.all()
    image_person = PhotoModel.objects.filter(category_name_id =1)
    image_venue = PhotoModel.objects.filter(category_name_id =2)
    image_object = PhotoModel.objects.filter(category_name_id =3)
    image_location = PhotoModel.objects.filter(category_name_id =4)

    teste_all =  image_all
    teste_location = image_location
    teste_object = image_object
    context = {'categories': categories,'image_all':image_all,'image_venue':image_venue,'image_object':image_object,
    'image_location':image_location,'teste_all':teste_all,'teste_location':teste_location,
    'teste_object':teste_object}
    return render(request, 'minhagaleria/gallery_test.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):

    photo_list =[]
    question = "TESTE"
    photo = PhotoModel.objects.get(id=pk)
    photo_list.append(photo)
    for pic in photo_list:
        if pic.category_name_id==2:
            question = " Você se lembra desse evento ? "
   

    return render(request, 'minhagaleria/photo.html', {'photo': photo,'photo_list':photo_list,'question':question,})

class AddPhotoGamesView(CreateView):

  
    model = PhotoModel
    form_class = AddPhotoGamesForm
    template_name = 'minhagaleria/add_photogames.html'
    success_url = reverse_lazy('minhagaleria:gallery_test')
    #categories = CategoryModel.objects.all()
     
  
    #def form_valid(self, form):
        #form.instance.user = self.request.user
        #return super().form_valid(form)


class CreateProfilePageView(CreateView):

    model = ProfileModel
    form_class = ProfilePageForm
    template_name = 'minhagaleria/create_user_profile_page.html'
    success_url = reverse_lazy('minhagaleria/login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    model = ProfileModel
    template_name = 'minhagaleria/show_user_profile.html'

    def get_context_data(self,*args,** kwargs):
    
        context = super(ShowProfilePageView,self).get_context_data(*args,** kwargs)
        page_user = get_object_or_404(ProfileModel, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context