from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.contrib.auth import logout
from .models import Block, Apartment, Dues, Expense
from .forms import BlockForm, ApartmentForm, DuesForm, ExpenseForm

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    blocks = Block.objects.all()
    total_dues = Dues.objects.filter(is_paid=False).count()
    total_expenses = Expense.objects.all().aggregate(total=models.Sum('amount'))['total'] or 0
    total_income = Dues.objects.filter(is_paid=True).aggregate(total=models.Sum('amount'))['total'] or 0
    
    context = {
        'blocks': blocks,
        'total_dues': total_dues,
        'total_expenses': total_expenses,
        'total_income': total_income,
    }
    return render(request, 'core/home.html', context)

# Block CRUD
@login_required
def block_list(request):
    blocks = Block.objects.all()
    return render(request, 'core/block_list.html', {'blocks': blocks})

@login_required
def block_detail(request, pk):
    block = get_object_or_404(Block, pk=pk)
    apartments = block.apartment_set.all()
    return render(request, 'core/block_detail.html', {
        'block': block,
        'apartments': apartments
    })

@login_required
def block_create(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blok başarıyla oluşturuldu.')
            return redirect('core:block_list')
    else:
        form = BlockForm()
    return render(request, 'core/block_form.html', {'form': form, 'title': 'Yeni Blok Ekle'})

@login_required
def block_update(request, pk):
    block = get_object_or_404(Block, pk=pk)
    if request.method == 'POST':
        form = BlockForm(request.POST, instance=block)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blok başarıyla güncellendi.')
            return redirect('core:block_detail', pk=block.pk)
    else:
        form = BlockForm(instance=block)
    return render(request, 'core/block_form.html', {'form': form, 'title': 'Blok Düzenle'})

@login_required
def block_delete(request, pk):
    block = get_object_or_404(Block, pk=pk)
    if request.method == 'POST':
        block.delete()
        messages.success(request, 'Blok başarıyla silindi.')
        return redirect('core:block_list')
    return render(request, 'core/block_confirm_delete.html', {'block': block})

# Apartment CRUD
@login_required
def apartment_list(request):
    apartments = Apartment.objects.all()
    return render(request, 'core/apartment_list.html', {'apartments': apartments})

@login_required
def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    dues = apartment.dues_set.all().order_by('-due_date')
    return render(request, 'core/apartment_detail.html', {
        'apartment': apartment,
        'dues': dues
    })

@login_required
def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Daire başarıyla oluşturuldu.')
            return redirect('core:apartment_list')
    else:
        form = ApartmentForm()
    return render(request, 'core/apartment_form.html', {'form': form, 'title': 'Yeni Daire Ekle'})

@login_required
def apartment_update(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Daire başarıyla güncellendi.')
            return redirect('core:apartment_detail', pk=apartment.pk)
    else:
        form = ApartmentForm(instance=apartment)
    return render(request, 'core/apartment_form.html', {'form': form, 'title': 'Daire Düzenle'})

@login_required
def apartment_delete(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    if request.method == 'POST':
        apartment.delete()
        messages.success(request, 'Daire başarıyla silindi.')
        return redirect('core:apartment_list')
    return render(request, 'core/apartment_confirm_delete.html', {'apartment': apartment})

# Dues CRUD
@login_required
def dues_list(request):
    dues = Dues.objects.all().order_by('-due_date')
    return render(request, 'core/dues_list.html', {'dues': dues})

@login_required
def dues_create(request):
    if request.method == 'POST':
        form = DuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aidat başarıyla oluşturuldu.')
            return redirect('core:dues_list')
    else:
        form = DuesForm()
    return render(request, 'core/dues_form.html', {'form': form, 'title': 'Yeni Aidat Ekle'})

@login_required
def dues_update(request, pk):
    dues = get_object_or_404(Dues, pk=pk)
    if request.method == 'POST':
        form = DuesForm(request.POST, instance=dues)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aidat başarıyla güncellendi.')
            return redirect('core:dues_list')
    else:
        form = DuesForm(instance=dues)
    return render(request, 'core/dues_form.html', {'form': form, 'title': 'Aidat Düzenle'})

@login_required
def dues_delete(request, pk):
    dues = get_object_or_404(Dues, pk=pk)
    if request.method == 'POST':
        dues.delete()
        messages.success(request, 'Aidat başarıyla silindi.')
        return redirect('core:dues_list')
    return render(request, 'core/dues_confirm_delete.html', {'dues': dues})

# Expense CRUD
@login_required
def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'core/expense_list.html', {'expenses': expenses})

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Harcama başarıyla oluşturuldu.')
            return redirect('core:expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'core/expense_form.html', {'form': form, 'title': 'Yeni Harcama Ekle'})

@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Harcama başarıyla güncellendi.')
            return redirect('core:expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'core/expense_form.html', {'form': form, 'title': 'Harcama Düzenle'})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Harcama başarıyla silindi.')
        return redirect('core:expense_list')
    return render(request, 'core/expense_confirm_delete.html', {'expense': expense})
