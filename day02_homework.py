small = True
green = True

if small and green:
    print('완두콩')
elif small and not green:
    print('체리')
elif not small and not green:
    print('호박')
else:
    print('수박')