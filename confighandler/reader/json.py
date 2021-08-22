import os
from confighandler import ConfigHandler

if os.path.exists('settings.json') and os.path.exists('settings_default.json'):
    CONFIG = ConfigHandler('settings.json', os.environ, 'settings_default.json')
    __OS_CONFIG = ConfigHandler('settings.json', 'settings_default.json')
    for entry in __OS_CONFIG:
        os.environ[entry.upper()] = __OS_CONFIG[entry]
else:
    CONFIG =  ConfigHandler(os.environ)
