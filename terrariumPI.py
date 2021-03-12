# -*- coding: utf-8 -*-
__version__ = '4.0.0'

from gevent import monkey
monkey.patch_all()

import gettext
gettext.install('terrariumpi', 'locales/')

import warnings
#warnings.simplefilter("ignore", ResourceWarning)

import terrariumLogging
logger = terrariumLogging.logging.getLogger(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from terrariumEngine import terrariumEngine

if __name__  == "__main__":
  with warnings.catch_warnings():
    warnings.simplefilter("ignore", ResourceWarning)
    terrariumEngine = terrariumEngine(__version__)
    # This keeps running until CRTL-C is entered or given
    terrariumEngine.stop()

  logger.info(f'Shutdown TerrariumPI {__version__} done. Bye bye ...')