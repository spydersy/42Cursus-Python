import time

# Colors definition:
OKBLUE_COLOR = '\033[94m'
OKGREEN_COLOR = '\033[92m'
ENDC_COLOR = '\033[0m'
BOLD_COLOR = '\033[1m'

loading_bar = 'ETA: {}{:.2f}s{} [{}{:.0f}%{}][{}{}>{}{}] {}{}/{}{} | elapsed time {}{:.2f}s{}'
loading_bar_size = 32
def ft_progress(lst):
    start_time = time.time()
    for element in lst:
        percentage = (element / len(lst)) * 100
        try:
            eta = ((100 - percentage) * (time.time() - start_time)) / percentage
        except ZeroDivisionError:
            eta = 0
        loaded_bar = '=' * int((percentage * int(loading_bar_size)) / 100)
        empty_bar = ' ' * (loading_bar_size - int(percentage * loading_bar_size / 100) - 1)
        print(loading_bar.format(OKBLUE_COLOR,
                                 eta,
                                 ENDC_COLOR,
                                 BOLD_COLOR,
                                 percentage,
                                 ENDC_COLOR,
                                 OKGREEN_COLOR,
                                 loaded_bar,
                                 ENDC_COLOR,
                                 empty_bar,
                                 BOLD_COLOR,
                                 element + 1,
                                 len(lst),
                                 ENDC_COLOR,
                                 BOLD_COLOR,
                                 time.time() - start_time,
                                 ENDC_COLOR), end="\r")
        yield element

# Test00
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

# # Test01
# listy = range(10000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
#     time.sleep(0.005)
# print()
# print(ret)