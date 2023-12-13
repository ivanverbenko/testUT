def add_url_to_context(request):
    url = request.GET.get('url')  # Получаем значение 'url' из GET-параметра запроса или из другого места
    return {'url': url}