# main.py
import sys
import os

# Подключение пути к библиотеке
lib_path = os.path.abspath("./lib/postgresql")
sys.path.append(lib_path)

print(f"PostgreSQL submodule loaded from: {lib_path}")
