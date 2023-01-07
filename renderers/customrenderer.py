from ledwriter import ledwriter

"""
Base class that all custom renderers must subclass
"""
class custom_renderer:
    def render(self, start: int, end:int, writer: ledwriter):
        pass