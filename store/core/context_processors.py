from store.core.models import SiteSettings


def site_settings(request):
    context = {}
    context['site_settings'], _ = SiteSettings.objects.get_or_create()
    return context