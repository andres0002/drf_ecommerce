# py
import re
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# third
# own

def validar_pk_numerico(pk):
    try:
        return int(pk), None
    except (ValueError, TypeError):
        return None, Response(
            {'error': 'El ID debe ser numérico.'},
            status=status.HTTP_400_BAD_REQUEST
        )

SLUG_REGEX = re.compile(r'^[-a-zA-Z0-9_]+$')

def validar_slug(slug):
    if not isinstance(slug, str) or not SLUG_REGEX.match(slug):
        return None, Response(
            {'error': 'El slug es inválido.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    return slug, None