import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from palmerpenguins import load_penguins
import seaborn as sns

# Add page option for the overall app.
ui.page_opts(title="Shellenberger App with Histogram Plot", fillable=True)

with ui.sidebar():
    ui.input_slider("number_of_bins", "Number of Bins", 1, 100, 30)
    ui.input_select(
        "sex",
        "Which sex would you like to render?",
        ["male", "female"],
    )


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_point: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_point)
    plt.hist(random_data_array, input.number_of_bins(), density=True, color="skyblue")


@render.plot(alt="Blank title")
def draw_scatterplot():
    penguins = load_penguins()
    penguins = penguins[penguins['sex'] == input.sex()]
    sns.scatterplot(
        data=penguins,
        x='bill_length_mm',
        y='bill_depth_mm',
        hue='island',
    )
    plt.xlabel("Bill Length")
    plt.ylabel("Bill Depth")
    plt.title("Bill Length vs. Depth")
