# instead of f(x) use log_func(f, x)
def log_func(fxn, input, fxn_name=None, note=None):
  if fxn_name == None:
    fxn_name = fxn.__name__
  output = fxn(input)
  print(f'DEBUG: {fxn_name}({input}) => {output}')
  if note != None:
    print('DEBUG: ' + note)
  return output