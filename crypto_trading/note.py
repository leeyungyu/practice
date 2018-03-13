from module.learning import *
from module.function import *

import pandas as pd

df = pd.DataFrame(load_csv(['ADA','TRX']))

print(df)