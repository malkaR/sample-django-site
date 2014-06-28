
INSTALLED_APPS = ()
TEMPLATE_CONTEXT_PROCESSORS = ()

try:
    from core_settings import *
except ImportError:
    pass 

try:
    from allauth_settings import *
except ImportError:
    pass

try:
    from dev_settings import *
except ImportError:
    pass