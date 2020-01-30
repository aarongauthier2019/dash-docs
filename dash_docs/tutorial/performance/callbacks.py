import dash_core_components as dcc

from dash_docs.tutorial.components import Syntax
from dash_docs import tools
from dash_docs import reusable_components


examples = {
    'memoization': tools.load_example(
        'tutorial/examples/performance_memoization.py'),
    'performance_flask_caching': tools.load_example(
        'tutorial/examples/performance_flask_caching.py'),
    'performance_flask_caching_dataset': tools.read_file(
        'tutorial/examples/performance_flask_caching_dataset.py')
}

layout = [
    reusable_components.Markdown('''
    

### Memoization

Since Dash's callbacks are functional in nature (they don't contain any state),
it's easy to add memoization caching. Memoization stores the results of a
function after it is called and re-uses the result if the function is called
with the same arguments.

To better understand how memoization works, let's start with a simple example.

'''),

    Syntax('''
import time
import functools32

@functools32.lru_cache(maxsize=32)
def slow_function(input):
    time.sleep(10)
    return 'Input was {}'.format(input)
    '''),

    reusable_components.Markdown('''

Calling `slow_function('test')` the first time will take 10 seconds.
Calling it a second time with the same argument will take almost no time
since the previously computed result was saved in memory and reused.

***

Dash apps are frequently deployed across multiple processes or threads.
In these cases, each process or thread contains its own memory, it doesn't
share memory across instances. This means that if we were to use `lru_cache`,
our cached results might not be shared across sessions.

Instead, we can use the
[Flask-Caching](https://pythonhosted.org/Flask-Caching/)
library which saves the results in a shared memory database like Redis or as
a file on your filesystem. Flask-Caching also has other nice features like
time-based expiry. Time-based expiry is helpful if you want to update your
data (clear your cache) every hour or every day.

Here is an example of `Flask-Caching` with Redis:
'''),

    Syntax(examples['performance_flask_caching'][0]),

    reusable_components.Markdown('''

***

Here is an example that **caches a dataset** instead of a callback.
It uses the FileSystem cache, saving the cached results to the filesystem.

This approach works well if there is one dataset that is used to update
several callbacks.

'''),

    Syntax(examples['performance_flask_caching_dataset']),
]
