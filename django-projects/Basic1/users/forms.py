from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# 使用者註冊表單，繼承自 Django 的 UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))  # 自定義 Email 欄位，使用 Bootstrap 樣式和占位符
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))  # 自定義名字欄位
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))  # 自定義姓氏欄位

    class Meta:
        model = User  # 指定表單對應的模型為 User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # 指定表單包含的欄位

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# 定義 UserProfileForm 表單，用於用戶個人資料的查看和更新
class UserProfileForm(forms.ModelForm):
    # 表單的 Meta 類別，用於指定表單的模型和欄位
    class Meta:
        model = UserProfile  # 指定表單對應的模型為 UserProfile
        fields = ['phone', 'address']  # 定義表單顯示的欄位，僅包含 phone 和 address 欄位
        # 可根據需求在此添加或修改顯示的欄位

    # 初始化表單，讓每個欄位在前端顯示時具有預設樣式
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # 設定每個欄位的樣式，方便在前端進行顯示調整
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': '輸入電話號碼'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': '輸入地址'})