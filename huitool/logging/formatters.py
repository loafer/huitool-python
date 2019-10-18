import logging
import json


class JsonFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt, style):
        super().__init__(fmt, datefmt, style)
        self.datefmt = datefmt

    def format(self, record):
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        s = self.formatMessage(record)
        record_dict = json.loads(s)

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        stack_trace = ''
        if record.exc_text:
            stack_trace = record.exc_text
        if record.stack_info:
            if stack_trace[-1:] != "\n":
                stack_trace = stack_trace + "\n"
            stack_trace = stack_trace + self.formatStack(record.stack_info)

        if stack_trace:
            record_dict['stack_trace'] = stack_trace

        return json.dumps(record_dict)
