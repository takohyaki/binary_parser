import matplotlib.pyplot as plt

def plot_scatterplot(dataframe, x_column, y_column, color_column=None, title='', xlabel='', ylabel=''):
    if color_column:
        plt.scatter(dataframe[x_column], dataframe[y_column], c=dataframe[color_column], cmap='plasma', s=1)
        plt.colorbar(label=color_column)
    else:
        plt.scatter(dataframe[x_column], dataframe[y_column], s=1)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
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
