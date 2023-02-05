from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 
                 'excludes': [],
                 'include_files': [('resources','resources')]}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'if_a_tree_falls')
]

setup(name='if_a_tree_falls',
      version = '1.0',
      description = '',
      options = {'build_exe': build_options},
      executables = executables)
