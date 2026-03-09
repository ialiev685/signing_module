import sys

pycades_path = r"/cryptopro/pycades/pycades-main/build"
sys.path.append(pycades_path)

import pycades  # type: ignore
from pycades_types import Pycades
from typing import cast


pycades_engine = cast(Pycades, pycades)
