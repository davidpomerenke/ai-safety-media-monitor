import statistics

import numpy as np
import pandas as pd
import plotly.express as px
import writer as wf
from writer.core import WriterState


# STATE INIT


initial_state = wf.init_state(
    {
        "my_text": "Hello, world!!!",
        "my_chart": "chart",
    }
)
