""" Python Functions """

def display_info(*args, instructor="Harry", **kwargs):
  return [args, instructor, kwargs]

print( display_info(1, 2, 3, last_name="Manchanda", job="Engineer") )
