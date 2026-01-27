from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_image.get_absolute_url())      
    else:
        form = ImageCreateForm(initial={'url': request.GET.get('url')})
    return render(request, 'images/image/create.html', {'section': 'image', 'form': form})


@login_required
def image_detail(request, id , slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    print(image)
    return  render(request, 'images/image/detail.html', {'section': 'images', 'image': image})


@login_required
@require_POST
def image_like(request): 
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    print(action)
    print(image_id)

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})



@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, entrega la primera página
        images = paginator.page(1)
    except EmptyPage:
        if images_only:
            # Si la solicitud AJAX y la página están fuera de rango
            # devuelve una página vacía
            return HttpResponse('')
        # Si la página está fuera de rango, devuelve la última página de resultados
        images = paginator.page(paginator.num_pages)
    if images_only:
        return render(request, 'images/image/list_images.html', {'section': 'images', 'images': images})
    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})

        
