import statistics

import numpy as np
import pandas as pd
import plotly.express as px
import writer as wf
from writer.core import WriterState


# STATE INIT

from data import get_data

data = get_data()

# vegalite spec
spec = {
    "mark": "bar",
    "data": {"values": data.reset_index().to_dict(orient="records")},
    "width": 400,
    "encoding": {
        "x": {
            "field": "index",
            "type": "temporal",
        },
        "y": {
            "field": "count",
            "type": "quantitative",
        },
    },
}


spec2 = {
    "mark": "line",
    "data": {"values": data.reset_index().to_dict(orient="records")},
    "width": 400,
    "encoding": {
        "x": {"field": "index", "type": "temporal"},
        "y": {"field": "sentiment", "type": "quantitative"},
        "color": {
            "condition": {"test": "datum.sentiment > 0", "value": "green"},
            "value": "red",
        },
    },
}

initial_state = wf.init_state(
    {
        "my_text": "Hello, world!!!",
        "my_chart": spec,
        "my_chart_2": spec2,
    }
)
