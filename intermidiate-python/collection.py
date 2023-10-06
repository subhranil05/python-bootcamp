# Collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaabbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.elements())
print(list(my_counter.elements()))

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(2, -5)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)

from collections import defaultdict
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c'])

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(4)
d.extend([7,8,9])
d.extendleft([7,8,9])
print(d)