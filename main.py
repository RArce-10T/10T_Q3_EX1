# Conditional statements in python
from pyscript import display, document


def weather_update(e):
  weather = lower(document.getElementById('input1').value)

  if weather == 'raining': 
    display(f'Bring an umbrella', target='output')
  else:
    display(f'Wear your sunglasses', target='output')
