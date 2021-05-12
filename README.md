# splines
Simple implementations of cubic Bezier curves and interpolation, higher order Bezier curves, and B-splines. 2D and 3D support

# Usage
All functions require numpy, matplotlib imported as shown:

```python
import numpy as np
import matplotlib.pyplot as plt
```

The CtrlPoint class must be used to wrap control points. These are just objects containing tuples of points, making them easy to construct and pass.

Some functions, such as the 3D variants, may require the corresponding 2D function. These dependencies are stated at the top of the file. Example usage for the functions included in each file are included as commented code at the bottom.
