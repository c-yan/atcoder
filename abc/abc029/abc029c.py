def print_passwords(n):
  def print_passwords_impl(n, s):
    if len(s) == n:
      print(s)
      return
    else:
      print_passwords_impl(n, s + 'a')
      print_passwords_impl(n, s + 'b')
      print_passwords_impl(n, s + 'c')
  print_passwords_impl(n, '')


N = int(input())

print_passwords(N)
