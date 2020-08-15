# python_confighandler

Wrapper for ChainMap.

## Strings
On a string ConfigHandler checks if it can load+parse a file. If not it tries to parse the string (JSON).

Example:

```python
import os
from confighandler import ConfigHandler

defaults = {"color": "blue", "user": "guest"}
}

configs = ConfigHandler('{"color": "red"}', 'settings.json', os.environ, defaults)
print(configs.get('color'))
```

## Ideas
Implementation of different string handler for different config types (yaml, configuration language, ...)