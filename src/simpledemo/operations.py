from gettext import gettext
from textwrap import dedent

from juicer.operation import Operation
class DataReader(Operation):
    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters,  named_inputs, named_outputs)

        self.has_code = len(named_outputs) >= 1
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        code = """ DataReader"""
        return dedent(code)

class UpperCase(Operation):
    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters,  named_inputs, named_outputs)

        self.has_code = len(named_outputs) >= 1
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        code = """ Upper Case"""
        return dedent(code)

class LowerCase(Operation):
    def __init__(self, parameters, named_inputs, named_outputs):
        Operation.__init__(self, parameters,  named_inputs, named_outputs)

        self.has_code = len(named_outputs) >= 1
        self.output = self.named_outputs.get(
            'output data', 'output_data_{}'.format(self.order))

    def generate_code(self):
        code = """ Lower Case """
        return dedent(code)

