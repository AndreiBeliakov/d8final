from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_not_author"] = not self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    editor_group = Group.objects.get(name='editor')
    if not request.user.groups.filter(name='editor').exists():
        editor_group.user_set.add(user)
    return redirect('/account/')

@login_required
def subscribe_me(request):
    return redirect(request.GET.get('path_info'))

