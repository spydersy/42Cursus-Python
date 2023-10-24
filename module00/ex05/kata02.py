# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)
kata02_output = '{:0>2d}/{:0>2d}/{} {:0>2d}:{:0>2d}'

print(kata02_output.format(kata[1], kata[2], kata[0], kata[3], kata[4]))