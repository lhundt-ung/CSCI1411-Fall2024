import json

class covidresult(object):
    """A Covid Result

    Attributes:
        state: A string with Name of state
        positive: A string representing positive case numbers
        date: A String representing a Date
    """

    def __init__(self, state,positive,date):
        """Return an covidresult object with the following attributes"""
        self.state = state
        self.positive = positive
        self.date = date






