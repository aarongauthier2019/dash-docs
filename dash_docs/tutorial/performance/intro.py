import dash_core_components as dcc

from dash_docs.tutorial.components import Syntax
from dash_docs import tools
from dash_docs import reusable_components


layout = [
    reusable_components.Markdown('''# Performance

The main performance limitation of dash apps is likely the callbacks in
the application code itself but transferring large amounts of data
or slow component rendering can also play a part in limiting performance.
Additionally, once our dash apps are in production, we can make sure that
resources are adequately distributed with various gunicorn configurations.

This chapter contains several recommendations for improving the performance
of your dash apps and will also go over how to use
[pyspy](https://github.com/benfred/py-spy) and the profiler built into your browser
to determine what's slowing your app down.

***
''')
]
