from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, EditUserProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as password_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Relation


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'You are registered successfully', 'success')
            return redirect("home:home")
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect("home:home")
            messages.error(request, 'Username or Password is wrong', 'danger')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "Ypu logged out successfully", "success")
        return redirect("home:home")


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        # posts = Post.objects.filter(user=user)
        # we can use backward relation instead
        posts = user.posts.all()
        # checking following relationship
        is_following = False
        following_relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if following_relation.exists():
            is_following = True
        return render(request, 'account/profile.html', {'user': user, 'posts': posts, "is_following": is_following})


class UserPasswordResetView(password_view.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy("account:password_reset_done")


class UserPasswordResetDoneView(password_view.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(password_view.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy("account:password_reset_complete")


class UserPasswordResetCompleteView(password_view.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        following_user = User.objects.get(id=user_id)
        following_relation = Relation.objects.filter(from_user=request.user, to_user=following_user)
        if following_relation.exists():
            messages.error(request, "You are following this user already", "danger")
        else:
            Relation(from_user=request.user, to_user=following_user).save()
            messages.success(request, "You are followed this user", "success")
        return redirect("account:user_profile", following_user.id)


class UserUnfollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        following_user = User.objects.get(id=user_id)
        following_relation = Relation.objects.filter(from_user=request.user, to_user=following_user)
        if following_relation.exists():
            following_relation.delete()
            messages.success(request, "You are unfollowed this user", "success")
        else:
            messages.error(request, "You are not following this user", "danger")
        return redirect("account:user_profile", following_user.id)


class EditProfileView(LoginRequiredMixin, View):
    form_class = EditUserProfileForm

    def get(self, request):
        form = self.form_class(instance=request.user.profile, initial={'email': request.user.email})
        return render(request, 'account/edit_profile.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, "profile updated successfully", "success")
        return redirect("account:user_profile", request.user.id)