import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page option for the overall app.
ui.page_opts(title="Shellenberger App with Histogram Plot", fillable=True)

with ui.sidebar():
    ui.input_slider("number_of_bins", "Number of Bins", 1, 100, 30)


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_point: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_point)
    plt.hist(random_data_array, input.number_of_bins(), density=True, color="skyblue")
