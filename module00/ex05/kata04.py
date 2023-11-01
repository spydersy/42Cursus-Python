# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)
kata04_output = 'module_{:0>2d}, ex_{:0>2d} : {:.2f}, {:.2e}, {:.2e}'

print(kata04_output.format(kata[0], kata[1], kata[2], kata[3], kata[4]))