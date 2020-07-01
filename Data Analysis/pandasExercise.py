import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

data = sns.load_dataset("titanic")
data.to_excel("titanic.xlsx")
