import matplotlib.pyplot as plt

# For a scatterplot
def plot_scatterplot(dataframe, x_column, y_column, title='', xlabel='', ylabel='', save_path=None):
    plt.scatter(dataframe[x_column], dataframe[y_column], s=1)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# For a histogram

def plot_histogram(dataframe, column, title='', xlabel='', ylabel='Frequency', bins=10, save_path=None):
    plt.hist(dataframe[column], bins=bins, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
