import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scholarly import scholarly

import os

search_query = scholarly.search_author('Steven A Cholewiak')
author = next(search_query)
scholarly.pprint(author.fill(sections=['basic', 'citation_indices', 'co-authors']))