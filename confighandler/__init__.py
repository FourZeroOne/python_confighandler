import configparser
import errno
import io
import logging
import os
import json

LOGGER = logging.getLogger(__name__)


class ConfigHandler():
    def __init__(self, schema_file_name: str = None, schema: dict = None, use_env_as_fallback: bool = False, all_required: bool = False):
        self.schema_file_name = schema_file_name
        self.schema = schema
        self.use_env_as_fallback = use_env_as_fallback
        self.all_required = all_required
        self.fallback = {}

    def parse(self, config_file: str):
        if self.schema_file_name:
            schema_path = os.path.join(self.schema_file_name)
            if not os.path.exists(schema_path):
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), schema_path)
            with open(schema_path) as f:
                self.schema = json.load(f)

            if len(self.schema) == 0:
                raise Exception('Schema file is empty.')

        if self.use_env_as_fallback:
            if not self.schema:
                raise Exception('In order to use the fallback feature set the schema info.')
            self.create_env_fallback()

        config_file_path = os.path.join(config_file)
        if not os.path.exists(config_file_path):
            if not self.fallback:
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT),
                    config_file_path + '. Config not found and env fallback is not active.'
                )
            return self.get_config_from_fallback()

        return self.get_config(config_file_path)

    def create_env_fallback(self):
        self.fallback = {}
        for section in self.schema:
            for key in self.schema[section]:
                key_name = section + '.' + key
                self.fallback[key_name] = os.environ.get(key_name)

    def get_config_value(self, config, key_name):
        section, key = key_name.split('.')
        if section in config.sections():
            if key in config[section]:
                return config[section][key]

        if key_name in self.fallback:
            return self.fallback[key_name]

        return None

    def get_config(self, config_file_path):
        configs = {}
        config = configparser.ConfigParser()
        config.read(config_file_path)

        if not self.schema:
            for section in config.sections():
                for key in config[section]:
                    configs[section + '.' + key] = config[section][key]
            return configs

        not_found = []
        for key in self.fallback:
            value = self.get_config_value(config, key)
            if value is None and self.all_required:
                not_found.append(key)
            configs[key] = value

        if len(not_found) > 0:
            raise Exception('Some variables are not set: {}'.format(
                ', '.join(not_found))
            )

        return configs

    def get_config_from_fallback(self):
        configs = {}
        not_found = []
        for key in self.fallback:
            if self.fallback[key] is None and self.all_required:
                not_found.append(key)

        if len(not_found) > 0:
            raise Exception('Some variables are not set: {}'.format(
                ', '.join(not_found))
            )

        return self.fallback