'''
in order to find 3 or more consecutive identical numbers inside a string
using python3.8 regex and walrus operator (:=).
'''

import re
import time

start_time = time.time()


def f3omcin(string):
    '''
    find_3_or_more_consecutive_identical_numbers
    '''
    regex = r"([\d])\\1\\1+"
    target = re.compile(regex)
    if string is None:
        return False
    return None if not (
        num_str := re.search(
            target,
            string)) else num_str.group()


print(f3omcin('1111a'))

print(f"finshed in {time.time()-start_time}")
