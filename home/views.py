from django.shortcuts import render
from math import ceil
# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from home.models import products
from  django.contrib.auth.models import User 
from django.contrib.auth import logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from  django.contrib import messages
# Create your views here.
def home(request): 
    return render(request,'home.html')
def cart(request):
    return render(request,'cart.html')
def search(request):
    return render(request,'search.html')


def singleproduct(request,slug):
    
    single = products.objects.filter(slug=slug).first()
     
    
    prod = products.objects.filter(sub_category=single.sub_category)
    subheading = products.objects.filter(category=single.category)
    
    removelis = [single.product_name]
    new_list = []
    newcat = []
    #filtering single product from our sub catagiory set
    for i in prod:
        if not i.product_name in removelis:
            new_list.append(i)
    #filtering single product from our sub catagiory set            
    for s in subheading:
        if not s.product_name in removelis:
            newcat.append(s)
    #filtering sub catagiory  product from our catagiory set
    for q in new_list:
        if q in newcat:
            newcat.remove(q)
    
    context = {'single' : single,"prod":new_list,"catagory":newcat}
    return render(request,'singleproduct.html',context)
def tracker(request):
    product = products.objects.all()
    print(product)
    n = len(product)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': product}
    return render(request, 'tracker.html', params)

    
        

    return render(request,'tracker.html',context)
def user(request):
    product= products.objects.all()
    allProds=[]
    catprods= products.objects.values('sub_category', 'id')
    cats= {item["sub_category"] for item in catprods}
    for cat in cats:
        prod=products.objects.filter(sub_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"tracker.html", params)

    

    
def contact(request):
    return render(request,'contact.html')

def productss(request):
    dataa = products.objects.all()
          
    context = {'dataa' : dataa}
        
    return render(request,'products.html',context)




#api
def login(request):
    if request.method == 'POST':
       loginuser = request.POST['loginuser'] 
       loginPassword= request.POST['loginPassword']
       user = authenticate(username=loginuser,password=loginPassword)
       if user is not None:
            auth_login(request,user)
            messages.success(request,"sucessfully login")
            return redirect('home')
       else:
           messages.error(request,'invalid username')
           return redirect('login')
  
    return render(request,'login.html')
def logouts(request):
    logout(request)
    messages.success(request,'successfully logout')
    return redirect('home')
    



def signin(request):
    if request.method == 'POST':
       user = request.POST['signupuser'] 
       email = request.POST['signupemail']
       signupfname = request.POST['signupfname']
       signupsname = request.POST['signupsname']
       pass1 = request.POST['inputPassword1']
       pass2 = request.POST['inputPassword2']
       if len(user) > 10:
            messages.error(request,"user name should be less than 10 characters")
            return redirect('home')
            
       if pass1 != pass2:
            messages.error(request,"passwoard should be match")
            return redirect('home')

       if not user.isalnum():
            messages.error(request,"username must be in alphabhates and numaric")
            return redirect('home')



       myuser = User.objects.create_user(user,email,pass1)
       
       myuser.first_name= signupfname
       myuser.last_name = signupsname
       myuser.save()
       messages.success(request,"your account has been successfully created")
       return redirect('login')
       
    else:
        return render(request,'signinpage.html')  
