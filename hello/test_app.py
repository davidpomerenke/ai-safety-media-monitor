import os

import pandas as pd
import plotly.express as px
import writer as wf
from writer.core import WriterState
import pytest


class TestApp:
    @pytest.fixture(autouse=True)
    def before(self):
        import main

        os.chdir(os.path.dirname(__file__))
        self.app_state = wf.init_state(
            main.initial_state,
        )

        yield
