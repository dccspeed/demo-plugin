from .transpiler import DemoTranspiler

class DemoFactory():
    @staticmethod
    def get_transpiler(config):
        return DemoTranspiler(config)
