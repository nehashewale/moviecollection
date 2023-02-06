
from django.core.cache import caches


COUNTER_CACHE_KEY = "hits"

def request_counter(get_response):
    def middleware(request):
        cache = caches['default']
        try:
            cache.incr(COUNTER_CACHE_KEY)
        except ValueError:
            cache.set(COUNTER_CACHE_KEY, 1)
        response = get_response(request)
        return response
    return middleware

def get_counter():
    cache = caches['default']
    return cache.get(COUNTER_CACHE_KEY)

def reset_counter():
    cache = caches['default']
    cache.set(COUNTER_CACHE_KEY, 0)
    return 
