from pure_pagination import Paginator, PageNotAnInteger


def page_turn(request, all_data, per_page=5):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_data, per_page=per_page, request=request)
    # per_page 每页条数

    data = p.page(page)
    return request, data
