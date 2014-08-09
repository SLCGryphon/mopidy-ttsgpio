from __future__ import unicode_literals

import logging
import os

import pygst
pygst.require('0.10')
import gst
import gobject

from mopidy import config, ext


__version__ = '0.1.0'


logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-TtsGpio'
    ext_name = 'ttsgpio'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        # TODO: Comment in and edit, or remove entirely
        #schema['username'] = config.String()
        #schema['password'] = config.Secret()
        return schema

    def setup(self, registry):

        from .frontend import TtsGpio
        registry.add('frontend', TtsGpio)

        from .tts_gpio_backend import TtsGpioBackend
        registry.add('backend', TtsGpioBackend)