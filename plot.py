import sys
import matplotlib.pyplot as plt
import numpy as np
from IPython import embed

plt.style.use('ggplot')

def num_at_tick(events, tick):
    return len([i for i in events if i <= tick])

data = []
for fname in sys.argv[1:]:
    with open(fname, 'r') as f:
        data.append(eval(f.read().replace(' ', ', ')))

# replace spaces with commas and evaluate the result as a list
#data = eval(data.replace(' ', ', '))

# prepare the plot
plt.figure()
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.hold(True)

for idx, n_persons in enumerate([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]):
    dead_ticks = []
    escape_ticks = []

    # HIER GAAT HET FOUT
    for trial in data[idx]:
        dead_ticks.append(trial[0])
        escape_ticks.append(trial[1])

    # I like this line
    final_tick = max(max(max(dead_ticks)), max(max(escape_ticks)))

    xs = np.arange(final_tick)

    # average the data
    escape_ys = [list(map(lambda t: num_at_tick(i, t), xs))
                 for i in escape_ticks]
    dead_ys = [list(map(lambda t: num_at_tick(i, t), xs))
                 for i in dead_ticks]

    # just uncomment the one you want, ugly but fuck it
    plt.plot(xs, np.average(escape_ys, axis=0), label='{} people'.format(n_persons))
    #plt.plot(xs, np.average(dead_ys, axis=0), label='{} people'.format(n_persons))

plt.legend()
plt.show()
