from django.db import models
from django.contrib.auth.models import User

class Block(models.Model):
    name = models.CharField(max_length=50, verbose_name="Blok Adı")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Blok"
        verbose_name_plural = "Bloklar"

class Apartment(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name="Blok")
    number = models.CharField(max_length=10, verbose_name="Daire Numarası")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Daire Sahibi")
    is_occupied = models.BooleanField(default=True, verbose_name="Dolu mu?")
    
    def __str__(self):
        return f"{self.block.name} - {self.number}"
    
    class Meta:
        verbose_name = "Daire"
        verbose_name_plural = "Daireler"

class Dues(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name="Daire")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tutar")
    due_date = models.DateField(verbose_name="Son Ödeme Tarihi")
    is_paid = models.BooleanField(default=False, verbose_name="Ödendi mi?")
    payment_date = models.DateField(null=True, blank=True, verbose_name="Ödeme Tarihi")
    
    def __str__(self):
        return f"{self.apartment} - {self.amount} TL"
    
    class Meta:
        verbose_name = "Aidat"
        verbose_name_plural = "Aidatlar"

class Expense(models.Model):
    title = models.CharField(max_length=200, verbose_name="Harcama Başlığı")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tutar")
    date = models.DateField(verbose_name="Harcama Tarihi")
    description = models.TextField(verbose_name="Açıklama")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    
    def __str__(self):
        return f"{self.title} - {self.amount} TL"
    
    class Meta:
        verbose_name = "Harcama"
        verbose_name_plural = "Harcamalar"
