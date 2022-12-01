from django.shortcuts import render, redirect
from AdminApp.models import Category, Product, UserInfo
from UserApp.models import MyCart
# Create your views here.


def homepage(request):
    # fetch all records from category table
    cats = Category.objects.all()
    cakes = Product.objects.all()
    return render(request, 'homepage.html', {"cats": cats, "cakes": cakes})


def login(request):
    if(request.method == "GET"):
        return render(request, "login.html", {})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        user = UserInfo.objects.get(uname=uname, password=password)
        try:
            user = UserInfo.objects.get(uname=uname, password=password)
        except:
            return redirect(login)
        else:
            # Create the session
            request.session["uname"] = uname
            return redirect(homepage)


def signout(request):
    request.session.clear()
    return redirect(homepage)


def signup(request):
    if(request.method == "GET"):
        return render(request, 'signup.html', {})
    else:
        uname = request.POST['uname']
        password = request.POST['password']
        email = request.POST['email']
        user = UserInfo(uname, password, email)
        user.save()
        return redirect(homepage)


def ShowCakes(request, id):
    cats = Category.objects.all()
    id = Category.objects.get(id=id)
    cakes = Product.objects.filter(cat=id)
    return render(request, "homepage.html", {"cats": cats, "cakes": cakes})


def ViewDetails(request, id):
    cake = Product.objects.get(id=id)
    return render(request, "ViewDetails.html", {"cake": cake})


def addToCart(request):
    if(request.method == 'POST'):
        if("uname" in request.session):
            # add to cart
            #User and Product
            cakeid = request.POST["cakeid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            cake = Product.objects.get(id=cakeid)
            user = UserInfo.objects.get(uname = user)
            #check for duplicates
            try:
                cart=MyCart.objects.get(cake=cake,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.cake = cake
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)

        else:
            return redirect(login)
def ShowAllCartItems(request):
    if(request.method=='GET'):
        uname=request.session['uname']
        user=UserInfo.objects.get(uname=uname)
        cartitems=MyCart.objects.filter(user=user)
        total=0
        for item in cartitems:
            total += (item.qty)*(item.cake.price)
        
        request.session["total"] = total
        return render(request,"ShowAllCart.html",{"items":cartitems})
    else:
        pass