# Import base settings
from .base import *

# Local settings
try:
    from .local import *
except:
    pass


# Production settings
try:
    from .production import *
except:
    pass
