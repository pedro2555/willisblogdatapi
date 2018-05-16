#!/bin/bash python
# -*- coding: utf-8 -*-

import os

LEGACY_HOST = os.environ.get('LEGACY_HOST', '')
LEGACY_PORT = os.environ.get('LEGACY_PORT', 3306)
LEGACY_USER = os.environ.get('LEGACY_USER', '')
LEGACY_PASS = os.environ.get('LEGACY_PASS', '')
LEGACY_DB = os.environ.get('LEGACY_DB', '')

DOMAIN = {}
