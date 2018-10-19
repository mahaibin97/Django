from django.contrib import admin
from typing import Any

from .models import Question
from .models import *

admin.site.register(Question)
admin.site.register(Choice)

