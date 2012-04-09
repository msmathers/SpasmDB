import time
from datetime import datetime

def escape(value, field=None):
    if value is None:
        return "NULL"
    elif isinstance(value, bool):
        return "1" if value else "0"
    elif field in ['added','created','date']:
        _format = '%Y-%m-%d %H:%M:%S'
        if isinstance(value, datetime):
            value = value.strftime(_format)
        else:
            value = time.strftime(_format, value)
    elif hasattr(value,'replace'):
        value =  value.replace("'","''")
    return "'%s'" % value

def safe_str(s):
    return s
