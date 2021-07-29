def add_element(current, new):
  if len(current) > 0:
    current += ', ' + new
  else: 
    current += new
  
  return current

def locate_handler(file, locate):
  selected_elements = ''

  for element in file:
    if element['address']['state'] == locate:
      selected_elements = add_element(selected_elements, element['name'])

  return selected_elements

def less_or_equal_handler(file, limit):
  selected_elements = ''
  for element in file:
    if element['price_hourly'] <= int(limit):
      selected_elements = add_element(selected_elements, element['name'])

  return selected_elements

def more_or_equal_handler(file, limit):
  selected_elements = ''
  for element in file:
    if element['price_hourly'] >= int(limit):
      selected_elements = add_element(selected_elements, element['name'])

  return selected_elements
