# file: todo_project/ipfilter_middleware/middleware.py

from django.core.exceptions import PermissionDenied
from django.conf import settings


class IPFilterMiddleware:

   def __init__(self, get_response):
      self.get_response = get_response
      # One-time configuration and initialization.

   def __call__(self, request):
      # Code to be executed for each request before
      # the view (and later middleware) are called.

      allowed_ip_addresses = settings.IPFILTER_MIDDLEWARE['ALLOWED_IP_ADDRESSES']
      client_ip_address = request.META.get('REMOTE_ADDR')
      print(f'** client ip address: {client_ip_address}')

      if not client_ip_address in allowed_ip_addresses:
            raise PermissionDenied

      response = self.get_response(request)

      # Code to be executed for each request/response after
      # the view is called.

      response['X-IP-FILTER'] = 'IP FILTER BY KEA'

      return response