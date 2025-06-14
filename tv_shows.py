# Import libraries
import numpy as np
import pandas as pd
from apyori import apriori

# Load the dataset
dataset = pd.read_csv('tv_shows.csv', header=None)
transactions = []
for i in range(0, dataset.shape[0]):
    transactions.append([str(dataset.values[i, j])
                        for j in range(0, dataset.shape[1])])

# Apply the Apriori algorithm
rules = apriori(transactions=transactions, min_support=0.003,
                min_confidence=0.2, min_lift=3, min_length=2, max_length=2)

# Convert the rules to a list
results = list(rules)

# Function to inspect the results


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))


# Show the results in a DataFrame
resultsinDataFrame = pd.DataFrame(inspect(results), columns=[
                                  'Left Hand Side', 'Right Hand Side', 'Supports', 'Confidence', 'Lift'])

print(resultsinDataFrame.nlargest(n=10, columns='Lift'))

# The Results of Recommendation System
# Left Hand Side Right Hand Side  Supports  Confidence       Lift
# 8               Fringe            Lost  0.003096    0.379747  11.392405
# 9      Game of thrones         Vikings  0.004850    0.279762   8.290192
# 4              The 100            Dark  0.004644    0.416667   4.673032
# 10  Person of Interest       Mr. Robot  0.006914    0.429487   3.926161
# 7       Rick And Morty      Family Guy  0.009185    0.276398   3.864779
# 3         Breaking Bad        The Wire  0.004231    0.253086   3.849933
# 0      Game of thrones      12 Monkeys  0.003818    0.220238   3.757231
# 6             Punisher      Family Guy  0.004644    0.260116   3.637114
# 2                Arrow        The Wire  0.005779    0.221344   3.367068
# 5      Game of thrones      Family Guy  0.004025    0.232143   3.245980
