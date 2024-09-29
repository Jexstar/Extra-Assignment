import matplotlib.pyplot as plt
def q02():

    # Data for the histogram
    values = [5, 2, 5, 3, 4, 1]
    labels = ['25-44', 'Under 18', '45-64', '18-24', '65-84', '85 or older']

    # Bins for the histogram
    bins = range(len(values) + 1)

    # Create the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(range(len(values)), bins=bins, weights=values, linewidth=0.9, edgecolor='white')

    # Set the x-ticks to match the labels
    plt.xticks(ticks=[i + 0.5 for i in range(len(labels))], labels=labels)

    # Show the plot
    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\WS6510582\\" + 'q02.png'
    plt.savefig(path)
