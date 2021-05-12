# About

This set of functions was constructed as a final project for a computational mathematics course. Included are simple implementations of Cubic spline interpolation, arbitrary degree Bezier curves, as well as B-Splines. There is support for both 2D and 3D computation and plotting. The functions are built to work easily with matplotlib.

# Usage
All functions require numpy to work, and matplotlib to visualize. It must be imported as follows, assuming no edits to the functions:

```python
import numpy as np
import matplotlib.pyplot as plt
```

The CtrlPoint class must be used to wrap control points. These are just objects containing tuples of points, making them easy to construct and pass.

Some functions, such as the 3D variants, may require the corresponding 2D function. These dependencies are stated at the top of the file. Example usage for the functions is included as commented code at the bottom.
