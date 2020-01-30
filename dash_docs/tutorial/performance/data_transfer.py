import dash_core_components as dcc

from dash_docs.tutorial.components import Syntax
from dash_docs import tools
from dash_docs import reusable_components


layout = [
    reusable_components.Markdown('''# Data Transfer

Any time a callback is triggered, the data for all the `Input`
and `State` props defined in the callback is transferred from
the client's browser to your dash app. This could be a lot of
time if one of those `Input` props is a `dcc.Store` component
containing a large dataset.


''')
]
