from django import template
from django.utils.safestring import mark_safe

from toko.models import Category

register = template.Library()


@register.simple_tag
def categories():
    produk_produk_items = Category.objects.filter(is_active=True).order_by('nama_produk')
    produk_produk_items_li = ""
    for i in produk_produk_items:
        produk_items_li += """<li><a href="/category/{}">{}</a></li>""".format(i.slug, i.nama_produk)
    return mark_safe(produk_items_li)

@register.simple_tag
def categories_mobile():
    produk_produk_items = Category.objects.filter(is_active=True).order_by('nama_produk')
    produk_produk_items_li = ""
    for i in produk_produk_items:
        produk_produk_items_li += """<li class="item-menu-mobile"><a href="/category/{}">{}</a></li>""".format(i.slug, i.nama_produk)
    return mark_safe(produk_produk_items_li)


@register.simple_tag
def categories_li_a():
    produk_items = Category.objects.filter(is_active=True).order_by('nama_produk')
    produk_items_li_a = ""
    for i in produk_items:
        produk_items_li_a += """<li class="p-t-4"><a href="/category/{}" class="s-text13">{}</a></li>""".format(i.slug,
                                                                                                         i.nama_produk)
    return mark_safe(produk_items_li_a)


@register.simple_tag
def categories_div():
    """
    section banner
    :return:
    """
    produk_items = Category.objects.filter(is_active=True).order_by('nama_produk')
    produk_items_div = ""
    item_div_list = ""
    for i, j in enumerate(produk_items):
        if not i % 2:
            produk_items_div += """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.gambar, j.slug, j.nama_produk)
        else:
            produk_items_div_ = """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.gambar, j.slug, j.nama_produk)
            item_div_list += """<div class="col-sm-10 col-md-8 col-lg-4 m-l-r-auto">""" + produk_items_div + produk_items_div_ + """</div>"""
            produk_items_div = ""

    return mark_safe(item_div_list)