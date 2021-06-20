import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Method to plot barchart from the dictionary variable
def plot_barchart(new_dict, columns):
    df = pd.DataFrame(new_dict.items(), columns=columns)

    sns.barplot(x = columns[0],
                y = columns[1],
                data = df)

    # Show the plot
    plt.show()

