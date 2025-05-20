# py
from datetime import timedelta
# django
from django.utils import timezone
from django.conf import settings
# drf
from rest_framework.authentication import TokenAuthentication
# third
# own

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    
    # calculo tiempo de expiración.
    def expires_in(self, token):
        time_elapse = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapse
        return left_time
    
    # validate si el token ya expired.
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)
    
    # si token ya esta expirado.
    def token_expire_handler(self, token, model, user):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            # logical de si el token ya expiro.
            token.delete()
            # se actualiza el token sin necesidad de cerrar las sessions.
            token = model.objects.create(user=user)
        return is_expire, token
    
    def authenticate_credentials(self, key):
        message, token, user = None, None, None
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
            user = token.user
        except model.DoesNotExist:
            message = 'Invalid token.'
            self.expired = True
        
        if token is not None:
            if not token.user.is_active:
                message = 'User inactive or deleted.'
        
            is_expired, token = self.token_expire_handler(token, model, user)
            if is_expired:
                message = 'Su Token ha expirado.'
        
        return (user, token, message, self.expired)