from djamgo.forms import Form
from .models import Flight


class EntryFields(models.ModelForm): 
   class Meta: 
      model = Flight
      fields = __all__
  