from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Food, Pet, UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'กรอกชื่อผู้ใช้',}),
            'first_name': forms.TextInput(attrs={'placeholder': 'กรอกชื่อ',}),
            'last_name': forms.TextInput(attrs={'placeholder': 'กรอกนามสกุล',}),
            'email': forms.TextInput(attrs={'placeholder': 'กรอกที่อยู่อีเมล',}),
            'password1': forms.TextInput(attrs={'placeholder': 'กรอกรหัสผ่าน',}),
            'password2': forms.TextInput(attrs={'placeholder': 'กรอกรหัสผ่านอีกครั้ง',}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='ชื่อผู้ใช้',widget = forms.TextInput(attrs={'placeholder': 'กรอกชื่อผู้ใช้', 'class': 'w-full px-3 py-2 border rounded-md text-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'กรอกรหัสผ่าน','class': 'w-full px-3 py-2 border rounded-md text-sm'}) ,label='รหัสผ่าน')

    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number']

        labels = {
            'phone_number': 'หมายเลขโทรศัพท์', 
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'กรอกหมายเลขโทรศัพท์', 'class': 'w-full px-3 py-2 border rounded-md text-sm'}),
        }

class AddPointsForm(forms.Form):
    phone_number = forms.CharField(
        label='เบอร์โทรศัพท์',
        widget=forms.TextInput(attrs={'placeholder': 'กรอกเลขที่สมาชิก', 'class': 'w-full px-3 py-2 border rounded-md text-sm'})
    )
    points_to_add = forms.IntegerField(
        label='คะแนนที่ต้องการเพิ่ม',
        widget=forms.TextInput(attrs={'placeholder': 'กรอกคะแนนที่ต้องการเพิ่ม', 'class': 'w-full px-3 py-2 border rounded-md text-sm'})
    )

class AddPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
    
        widgets = {
        'date_time':forms.TextInput(attrs={'type': 'datetime-local'})
        }

        labels = {
            'name' : 'ชื่อ',
            'age' : 'อายุ',
            'profile' : 'รูป',
            'sex' : 'เพศ',
            'breed' : 'สายพันธุ์',
            'desc' : 'คำอธิบาย',
            'date_time': 'วัน-เวลา', 
            'appear' : 'แสดง',
        }

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

        labels = {
            'name' : 'ชื่ออาหาร',
            'price' : 'ราคา',
            'img' : 'รูปอาหาร',
            'stock' : 'มีสินค้า',
            'suggested' : 'เมนูแนะนำ',
        }