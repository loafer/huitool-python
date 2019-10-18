import logging

class ContextFilter(logging.Filter):
    def __init__(self, name, extra={}):
        super().__init__(name)
        self.extra = extra

    def filter(self, record):
        for key in self.extra:
            setattr(record, key, self.extra[key]) 
        return True
