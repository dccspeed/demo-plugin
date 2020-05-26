from juicer.transpiler import Transpiler

from .operations import DataReader, LowerCase, UpperCase
import os
class DemoTranspiler(Transpiler):
    def __init__(self, configuration):
        super(DemoTranspiler, self).__init__(configuration,
                os.path.abspath(os.path.dirname(__file__)))
   
    def _assign_operations(self):
        ops = {
            'data-reader': DataReader,
            'demo::lower_case': LowerCase,
            'demo::upper_case': UpperCase,
        }
        self.operations.update(ops)

    def get_code_template(self):
        return "templates/operation.tmpl"
