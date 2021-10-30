def n_hardest(n, reading_wrong, writing_wrong, math_wrong): 
    import numpy as np
    import pandas as pd
    import os

    cwd = os.getcwd()

    base_link = 'https://raw.githubusercontent.com/thissop/misc-experiments/main/sat/curves/'

    sections = ('Reading', 'Writing','Math')

    links = [base_link+i for i in ('reading.csv', 'writing.csv', 'math.csv')]

    reading_df, writing_df, math_df = (pd.read_csv(link) for link in links)

    reading_correct = 52-reading_wrong
    writing_correct = 44-writing_wrong
    math_correct = 58-math_wrong

    reading_scores = list(reading_df['Raw Score'])
    reading_row = np.array(reading_df.iloc[reading_scores.index(reading_correct)])
    reading_average = 10*np.sum(reading_row[1:n+1])/n

    writing_scores = list(writing_df['Raw Score'])
    writing_row = np.array(writing_df.iloc[writing_scores.index(writing_correct)])
    writing_average = 10*np.sum(writing_row[1:n+1])/n

    math_scores = list(math_df['Raw Score'])
    math_row = np.array(math_df.iloc[math_scores.index(math_correct)])
    math_average = np.sum(math_row[1:n+1])/n

    results_row = [reading_average, writing_average, math_average]
    rounded_row = [round(i, -1) for i in results_row]

    return results_row, rounded_row

result = n_hardest(5,2,1,1)

print(result)