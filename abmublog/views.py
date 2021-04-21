from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import DeleteView, UpdateView, ListView

from .forms import *
def registeration(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                group=Group.objects.get(name='user')
                user.groups.add(group)
                messages.success(request,'Account created Successfully for '+' '+username)
                return redirect('register')
        context={'form':form}
        return render(request,'abmublog/registration.html',context)
@login_required(login_url='login')
def addnewproduct(request):
    post=MakeOrder.objects.all()
    form=MakeOrderForm(initial={'author':request.user})
    if request.method=='POST':
        form=MakeOrderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context={'form':form,'posts':post}
    return render(request,'abmublog/addnewproduct.html',context)
def user_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                messages.info(request,'Username or password is incorrect')

        context={}
        return render(request,'abmublog/login.html',context)
@login_required(login_url='login')
def makeorder(request):
    form = Orderform(initial={'name':request.user})
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created Successfully')
            return redirect('orderpage')
    context = {'form': form}
    return render(request, 'abmublog/makeorder.html', context)
def editmakeorder(request,id):
    order=get_object_or_404(MakeOrder,id=id)
    if request.method=='POST':
        form=EditMakeOrderForm(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'post updated successfully')
            return redirect('addnewproduct')
    else:
        form=EditMakeOrderForm(instance=order)
    context={'form':form}
    return render(request,'abmublog/editmakeorder.html',context)
def deletemakeorder(request,id):
    order=get_object_or_404(MakeOrder,id=id)
    order.delete()
    messages.success(request, 'order deleted successfully')
    return redirect('addnewproduct')
def deleteorder(request,id):
    order=get_object_or_404(Order,id=id)
    if request.user==order.name:
        return HttpResponse("you cannot delete your own order")
    order.delete()
    messages.success(request,'order deleted successfully')
    return redirect('dashboard')

@login_required(login_url='login')
def homepageorder(request,id):
    product=MakeOrder.objects.get(id=id)
    form = Orderform(initial={'name': request.user,
                              'type':product.type,
                               'title':product.title,
                               })
    if request.method == "POST":
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Order created Successfully')
            return redirect('myorder')
    context = {'product': product,'form':form}
    return render(request, 'abmublog/homepageorder.html', context)
@login_required(login_url='login')
def myorder(request):
    orders=Order.objects.filter(name=request.user)
    order_count=orders.count()
    context={'orders':orders,'order_count':order_count}
    return render(request,'abmublog/myorder.html',context)
@login_required(login_url='login')
def dashboard(request):
    customers=Profile.objects.all()
    orders=Order.objects.all()
    total_customers=customers.count()
    total_ordes=orders.count()
    Delivered=orders.filter(status='Delivered').count()
    Pending=orders.filter(status='Pending').count()
    context={
             'orders':orders,
             'customers':customers,
             'total_ordes':total_ordes,
            'total_customers':total_customers,
             'Delivered':Delivered,
             'Pending':Pending
}
    return render(request,'abmublog/dashboard.html',context)
@login_required(login_url='homepage:login')
def customerprofile(request,id):
    customer = User.objects.get(id=id)
    profiles = Profile.objects.get(id=id)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer,
               'orders': orders,
               'profiles':profiles,
               'order_count': order_count}

    return render(request, 'abmublog/customer.html', context)
#delete view for orders
# class OrderDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
#     model=Order
#     success_url = '/'
#     def test_func(self):
#         order=self.get_object()
#         if self.request.user !=order.name:
#             return True
#         return False

# def order_approve(request,id):
#     order=get_object_or_404(Order,id=id)
#     if request.method=='POST':
#         form=OrderUpdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('order-page')
#     else:
#         form=OrderUpdateForm()
#     context={'form':form}
#     return render(request, 'abmublog/order_form.html',context)
class OrderApproveView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Order
    fields = ['status']
    success_url = '/'
   #with using of order_form templates

    # to check current user is the author of the post
    def test_func(self):
        order=self.get_object()
        if self.request.user!=order.name:
            return True
        return False
@login_required(login_url='login')
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account is updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'abmublog/profile.html',context)
@login_required(login_url='login')
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'password changed successfully')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'abmublog/change_password.html',{'form':form})
def forgot_password(request):
    return render(request,'abmublog/forgot_password.html')
class ProductListView(ListView):
    model = MakeOrder
    template_name = 'abmublog/index.html'
    context_object_name = 'products'
    ordering = ['-date_posted']
    paginate_by = 2
    def get_queryset(self):
        products = MakeOrder.objects.all().order_by('-date_posted')
        query = self.request.GET.get('q')
        if query:
            products = self.model.objects.filter(Q(title__icontains=query)|
                                                 Q(type__name__icontains=query))

        return products
@login_required(login_url='login')
def addproductlist(request):
    form = AddProductForm()
    if request.method=='POST':
        form=AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'product added Successfully')
            return redirect('addproductlist')

    context = {'form': form}
    return render(request, 'abmublog/addproductlist.html', context)
@login_required(login_url='login')
def give_suggeestion(request):
    form = SuggestForm(initial={'user':request.user})
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'suggestion sent successfully ')
            return redirect('suggestion')
    context = {'form': form}
    return render(request, 'abmublog/suggestion.html', context)
class SuggestionListView(ListView):
    model=Suggestion
    template_name = 'abmublog/view_suggestion.html'
    context_object_name = 'suggestion'
    paginate_by = 6
    ordering = ['-timestamp']
def user_logout(request):
    logout(request)
    return redirect('homepage')
