#!/usr/bin/python3
"""This is a new module"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
dictionary = storage.reload()