from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('dklabyrinthe.py', base=base)
]

setup(name='DonkeyTD',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
