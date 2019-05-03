import threading

class BankAccount(object):
  def __init__(self):
    self.lock = threading.Lock()
    self.balance = None

  def get_balance(self):
    with self.lock:
      if self.balance is None:
        raise ValueError('Account is not open')
      return self.balance

  def open(self):
    with self.lock:
      if self.balance is not None:
        raise ValueError('Account is already open')
      self.balance = 0

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Invalid amount')
    with self.lock:
      if self.balance is None:
        raise ValueError('Account is not open')
      self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Invalid amount')
    with self.lock:
      if self.balance is None:
        raise ValueError('Account is not open')
      if self.balance < amount:
        raise ValueError('Insufficient funds')
      self.balance -= amount

  def close(self):
    with self.lock:
      if self.balance is None:
        raise ValueError('Account is not open')
      self.balance = None

# vim:ts=2:sw=2:expandtab
