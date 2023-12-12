import numpy as np
from functions.get_pca import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def get_plot_data(X, y, loc, size=(5, 3)):
    X_red = dimension_reduction(X)

    fig, ax = plt.subplots(figsize=size)
    plt.style.use('dark_background')

    # Convert class labels to meaningful class names
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    class_labels = dict(zip(le.classes_, le.transform(le.classes_)))

    # Check if the input is a Pandas DataFrame
    if hasattr(X, 'iloc'):
        for label in np.unique(y):
            indices = np.where(y_encoded == class_labels[label])[0]
            ax.scatter(X.iloc[indices, 0], X.iloc[indices, 1], label=label)
    else:  # Assume NumPy array
        for label in np.unique(y):
            indices = np.where(y_encoded == class_labels[label])[0]
            ax.scatter(X[indices, 0], X[indices, 1], label=label)

    # Add legend
    ax.legend(title='Class')

    plt.xlabel('X')
    plt.ylabel('Y')

    loc.pyplot(fig)
