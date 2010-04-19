import vineyard.engines.BaseEngines 
import inspect

class AfterEffectsEngine(vineyard.engines.BaseEngines.RenderEngine):
    "After Effects Plugin"
    
    def __init__(self):
        vineyard.engines.BaseEngines.RenderEngine.__init__(self, version="1.0", name="After Effects Engine", filename=inspect.stack()[0][1])
        
AfterEffectsEngine()
