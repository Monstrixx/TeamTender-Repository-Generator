"""
TRG Pipeline
"""


class Pipeline:

    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def run(self):

        for step in self.steps:
            step()