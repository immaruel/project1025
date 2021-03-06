from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

#Create your views here.
from .models import *
from .forms import CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group

from .filters import ItemFilter

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# from .filters import OrderFilter

def exer(request):
    context = {}
    return render(request, 'app/exer.html',context)

# 메인 페이지2
def home(request):
    print("asdasdasdsadasdsadasd")
    print(request.user)
    try :
        customer = Customer.objects.get(user=request.user)
        context  = {'check' : login_check(request),'name': customer.name}
    except:
        context  = {'check' : '2','name': '로그인이 필요합니다.'}
    return render(request, 'app/index.html',context)
    
def login_check(request):
    context = {}
    if(str(request.user) == "AnonymousUser"):
        context = '2'
    elif(str(request.user) == "admin"):
        context = '3'
    else: 
        context = '1'
    return context

# 메인 페이지1
def opening(request):
	context = {'check' : login_check(request),'name': str(request.user) }
	return render(request, 'app/opening.html',context)


# # 산하 추가 로그인 후 모습
# def index_login(request,pk_test):
#     customer = Customer.objects.get(id=pk_test)
    
#     context = {'customer':customer,
#     'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/index_login.html',context)

# 상품보기
def search(request):
    customer = Customer.objects.all()

    # 산추
    item=Item.objects.all()
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user), 'item':item }
    
    return render(request, 'app/search.html',context)

# 상품만들기

def make(request):
    customer = Customer.objects.get(user=request.user)
    item = Item.objects.all()
    str1 = []
    list=customer.zzim_list.split(',')
    new_list = []
    string1=""
        #중복제거
    for v in list:
        if v not in new_list:
            new_list.append(v)
        #중복제거한 것 다시 찜리스트에 넣기
    for v in new_list:
        string1 += v+','
    customer.zzim_list=string1
    customer.save()
    # item = Item.objects.get(customer=customer)

    
    temp = customer.zzim_list.split(',')
    arr1=[]
    for i in temp:
        try:
            str2 = Item.objects.get(name=i)
            arr =["../../static/img/"+str(str2.image).split('/')[3],i,str2.price]
            arr1.append(arr)
        except:
            pass

    # for i in arr1:
    #     print(i)
    arr2 = arr1
    temp1 = []
    temp2 = []
    for i in arr1:
        ar=[]
        for v in i:
            ar.append(v)
        if ("세트") in ar[1]:
            temp1.append(ar)
    
    for i in arr1:
        ar=[]
        for v in i:
            ar.append(v)
        if not (("세트") in ar[1]):
            temp2.append(ar)
            
    print(temp2)
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user),'itemss':temp2 }
    return render(request, 'app/make.html',context)

# 랭킹
def rank(request):
    customer = Customer.objects.all()
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user) }
    return render(request, 'app/rank.html',context)

# 회원가입
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, '계정생성완료' + user)

			return redirect('login')
	context = {'form':form, 'check' : login_check(request),'name': str(request.user) }
	return render(request, 'app/register.html',context)
    
# 로그인
def loginPage(request):
   # if request.user.is_authenticated:
   #    return redirect('home')
   # else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)  

         if user is not None:
            login(request, user)
            return redirect('home')
         else:
            messages.info(request,'아이디 혹은 비밀번호가 잘못입력되었습니다!')
      context  = {'check' : login_check(request),'name': str(request.user) }
      return render(request, 'app/login.html',context)

# 로그아웃
def logoutUser(request):
    logout(request)
    return redirect('login')
#찜
def zzim(request):
 
    asd = Customer.objects.get(user=request.user)
    asd.zzim_list +=  "," + request.GET.get('name',None)
    asd.save()
    str1 = asd.zzim_list.split(',')
    print(str1)
    # zzim=int(1004)
    

    return redirect('../mypage')
#2 

def myPage(request):
    customer = Customer.objects.get(user=request.user)
    item = Item.objects.all()
    str1 = []
    list=customer.zzim_list.split(',')
    new_list = []
    string1=""
        #중복제거
    for v in list:
        if v not in new_list:
            new_list.append(v)
        #중복제거한 것 다시 찜리스트에 넣기
    for v in new_list:
        string1 += v+','
    customer.zzim_list=string1
    customer.save()
    # item = Item.objects.get(customer=customer)

    
    temp = customer.zzim_list.split(',')
    arr1=[]
    for i in temp:
        try:
            str2 = Item.objects.get(name=i)
            arr =["../../static/img/"+str(str2.image).split('/')[3],i,str2.price]
            arr1.append(arr)
        except:
            pass

    # for i in arr1:
    #     print(i)
    arr2 = arr1
    temp1 = []
    temp2 = []

    print("lllll")
    for i in arr1:
        ar=[]
        for v in i:
            ar.append(v)
        if ("세트") in ar[1]:
            temp1.append(ar)
    
    
    print(temp1)
    print("11111111")
    print("2222222")
    for i in arr1:
        ar=[]
        for v in i:
            ar.append(v)
        if not (("세트") in ar[1]):
            temp2.append(ar)
    
    
    print(temp1)
    print("2222222")
    # 산추 zzim추가했다가 지움
    context = {'customer':customer,'check':login_check(request), 
    'name':str(request.user),'simage':str1, 'item':item,'array':temp2,'array1':temp1}
    return render(request, 'app/mypage.html',context)

def listDelete(request):
    print("3333333333333333")
    list1= request.GET.get("name")
    print(list1)
    customer = Customer.objects.get(user=request.user)
    array= customer.zzim_list.split(',')

    str1 =""
    for i in array:
        if not list1 in i:
            str1 += i + ","
    customer.zzim_list =str1
    customer.save()
    return redirect('../mypage')

# def createOrder(request):
# 	context = {}
# 	return render(request, 'app/order_form.html',context)

# def updateOrder(request):
# 	context = {}
# 	return render(request, 'app/dashboard.html',context)

# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')
# 	context = {'item':order}
# 	return render(request, 'app/delete.html',context)


# # My Page(로그인시 이모티콘 누르면 회원 개인페이지로 이동)
# def mypage(request):
# 	context = {1, 2, 3}
# 	return render(request, 'app/mypage.html',{"hi":context})

# # mypage_cart
# def cart(request):
#     context = {'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/mypage_cart.html',context)


# # mypage_history
# def history(request):
#     context = {'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/mypage_history.html',context)

# # mypage_modify
# def modify(request):
#     context = {'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/mypage_modify.html',context)

# # mypage_rank
# def myrank(request):
#     context = {'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/mypage_rank.html',context)

# # mypage_save
# def save(request):
#     context = {'check' : login_check(request),'name': str(request.user) }
#     return render(request, 'app/mypage_save.html',context)

# mypage_search
def make_search(request):
    context = {'check' : login_check(request),'name': str(request.user) }
    return render(request, 'app/make_search.html',context)


# pay
def pay(request):
    context = {'check' : login_check(request),'name': str(request.user) }
    return render(request, 'app/pay.html',context)



# # mypage_cart
# def cart(request):
#     context = {1, 2, 3}
#     return render(request, 'app/mypage_cart.html',{"hi":context})


# birthday
def birthday(request):
    customer = Customer.objects.all()

    # 산추
    item=Item.objects.all()
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user), 'item':item }
    
    return render(request, 'app/birthday.html',context)


# tgday
def tgday(request):
    customer = Customer.objects.all()

    # 산추
    item=Item.objects.all()
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user), 'item':item }
    
    return render(request, 'app/tgday.html',context)


# moving
def moving(request):
    customer = Customer.objects.all()

    # 산추
    item=Item.objects.all()
    context = {'customer':customer,'check' : login_check(request),'name': str(request.user), 'item':item }
    
    return render(request, 'app/moving.html',context)