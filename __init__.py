from __future__ import absolute_import, print_function, unicode_literals
from .Kontrol import Kontrol


def create_instance(c_instance):
    return Kontrol(c_instance)
