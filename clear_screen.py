print 'teste'

#def clear():

try:
    import os
    lines = os.get_terminal_size().lines
except AttributeError:
    lines = 130
print("\n" * lines)

print 'teste 2'
