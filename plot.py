import sys
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

def num_at_tick(events, tick):
    return len([i for i in events if i <= tick])

with open(sys.argv[1], 'r') as f:
    data = f.read()

# replace spaces with commas and evaluate the result as a list
data = eval(data.replace(' ', ', '))

dead_ticks = [trial[0] for trial in data]
escape_ticks = [trial[1] for trial in data]

# I like this line
final_tick = max(max(max(dead_ticks)), max(max(escape_ticks)))

xs = np.arange(final_tick)

# average the data over the five trials
escape_ys = [list(map(lambda t: num_at_tick(i, t), xs))
             for i in escape_ticks]
dead_ys = [list(map(lambda t: num_at_tick(i, t), xs))
             for i in dead_ticks]

plt.plot(xs, np.average(escape_ys, axis=0), label='Escaped')
plt.plot(xs, np.average(dead_ys, axis=0), label='Dead')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend()
plt.show()
