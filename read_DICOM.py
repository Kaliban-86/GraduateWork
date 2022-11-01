import os
from math import floor

from PySide2 import QtCore, QtWidgets, QtGui

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from pydicom import dcmread, read_file
from pydicom.pixel_data_handlers.util import apply_modality_lut

from editor import EditorToolBox