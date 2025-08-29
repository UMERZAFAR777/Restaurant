from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from food.models import Food,Section
from django.db.models import Q
from party.models import Party
from professional_chef.models import Professional_Chef
from birthday_table.models import Birthday_table
from gallery.models import Gallery
from contactus.models import Contact






def index(request):
    section = Section.objects.all()
    gallery = Gallery.objects.all()
    food = Food.objects.all()
    f_search = None
    if request.method == "GET":
        st = request.GET.get('search')
        if st:
            # Search terms ko split kar ke har ek pe filter lagayenge
            search_terms = st.split()
            query = Q()
            for term in search_terms:
                query &= Q(food_name__icontains=term)  # 'AND' condition for more accurate results
            f_search = Food.objects.filter(query)

    party = Party.objects.all()
    professional_chef  = Professional_Chef.objects.all()
    data = {
        'section': section,
        'food': food,
        'f_search': f_search,
        'party':party,
        'professional_chef':professional_chef,
        'gallery':gallery,

    }

    return render(request, 'index.html', data)






def login_user(request):
    if request.method == "POST":
        identifier = request.POST.get('username')  
        password = request.POST.get('password')

        user = authenticate(request, username=identifier, password=password)

        if user is None:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username/Email or Password.')
            return redirect('login')

    return render(request, 'login.html')

def logout_user(request):
    logout(request,)
    messages.success(request,'You have been logged out........!')
    return redirect ('login')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(email = email).exists():
            messages.success (request,'Email Already Taken......!')
            return redirect ('register')

        if User.objects.filter(username = username).exists():
            messages.success (request,'Username Already Taken......!')
            return redirect ('register')
        
        if password != password2:
            messages.success (request,'Both password must be same sir......!')
            return redirect ('register')
        
        user = User(username = username , email = email)
        user.set_password(password)
        user.save()

        messages.success (request,'Registered Successfully......!')

        return redirect ('login')



    return render (request,'register.html')





def book_table(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people = request.POST.get("people")
        message = request.POST.get("message")

       
        Birthday_table.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            people=people,
            message=message
        )

        messages.success(request, "Thank you! We've received your booking. We will confirm it within 15 to 30 minutes and reach out to you via phone or email.")

        return redirect('/#book-a-table')

    
def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        title = request.POST.get("title")
        description = request.POST.get("description")

        Contact.objects.create(
            name=name,
            email=email,
            title=title,
            description=description
        )
        messages.success(request, "Thank you for contacting us! 🙏 We have received your message and our team will get back to you shortly.")
        return redirect ("/#contact")
