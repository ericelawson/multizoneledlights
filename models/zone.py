from models.color import color
from renderers.rainbow import rainbow_renderer
from renderers.customrenderer import custom_renderer
from ledwriter import ledwriter

class zone:
    renderer_impl: custom_renderer | None = None

    def __init__(self, name: str, start: int, end: int, color: color, renderer: str = ''):
        self.name = name
        self.start = start
        self.end = end
        self.color = color
        self.renderer = renderer

        if renderer:
            print('renderer found')
            """
            NOTE: ALL RENDERERS WILL NEED TO BE ADDED BELOW 
            Lookup the appropriate renderer, and create the instance in renderer_impl.
            A renderer will be initialized with the zone in the constructor, and will simply have a single defined render() method.
            Renderers will track their state internally and will be completely encapsulated.
            """
            if renderer == 'rainbow':
                print('loading rainbow renderer')
                self.renderer_impl = rainbow_renderer()
                
            
    def render(self, writer: ledwriter):
        """
        A zone should know how to render itself.
        If a zone has a static color, then render the color.
        If a zone has a renderer, then run the next iteration of the renderer.   
        """     
        
        if self.renderer_impl != None:
            #handle renderer rendering here for custom effects
            self.renderer_impl.render(self.start, self.end, writer)
            
        else:
            # this zone is a static color - render as such
            for i in range(self.start, self.end + 1):
                writer.setPixel(i, self.color.getTuple())
                print('setting color for led [' + str(i) + '] to ' + str(self.color.getTuple())) 




