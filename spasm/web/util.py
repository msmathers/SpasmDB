import time
import re

def escape(value, field=None):
    if field in ['added','created','date']:
        return time.strftime('%Y-%m-%d %H:%M:%S',value)
    elif hasattr(value,'replace'):
        return value.replace("'","''")
    else:
        return value

def safe_str(s):
    return s
