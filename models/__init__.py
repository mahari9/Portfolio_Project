#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("EF_TYPE_STORAGE")

if storage_t == "db":
    from models.storage_engine.database import DataBase
    storage = DataBase()
elif storage_t == "file":
    from models.storage_engine.file_storage import FileStorage
    storage = FileStorage()
else:
    raise ValueError("Invalid storage type. Choose 'db' or 'file' for EF_TYPE_STORAGE environment variable.")

storage.reload()