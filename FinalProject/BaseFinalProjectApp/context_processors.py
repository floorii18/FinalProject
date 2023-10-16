from RegisterFinalProjectApp.models import Avatar

def avatar_context(request):
    try:
        avatar_url = Avatar.objects.filter(user=request.user.id)[0].image.url
    except IndexError:
        avatar_url = None
    return {'avatar_url': avatar_url}
