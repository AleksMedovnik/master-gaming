from django.shortcuts import render
from .models import Post, Tag, Product
from django.db.models import Q


def post_lists(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(body__icontains=search_query)
        )
    else:
        posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})


def product_list(request):
    products = Product.objects.all()
    products_list = []
    for i in range(0, len(products), 3):
        products_list.append(products[i:i + 3])
    return render(request, 'blog/store.html', context={'products_list': products_list})


def product_detail(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(request, 'blog/store_detail.html', context={'product': product})

