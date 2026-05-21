#!/usr/bin/env python3

# Aviso ao usuário
# Este script gerencia grande parte do Bit-OS, mudar isto provavemente vai quebrar tudo.

import pyfuse3

class bvfso(pyfuse3.Operations):
    