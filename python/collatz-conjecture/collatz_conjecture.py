def collatz_steps(number):
  if number < 1:
    raise ValueError('Bad input')

  steps = 0
  while number != 1:
    if number % 2:
      number = number * 3 + 1
    else:
      number /= 2
    steps += 1
  return steps

# vim:ts=2:sw=2:expandtab
