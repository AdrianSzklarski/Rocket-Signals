import numpy as np
import matplotlib.pyplot as plt

from types import SimpleNamespace
from typing import Callable

def imports():
    return SimpleNamespace(np=np,
                           Callable=Callable,
                           plt=plt)