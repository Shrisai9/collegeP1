import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as ticker

# Function to load the Excel file and calculate standard deviations
def load_and_calculate():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    
    try:
        df = pd.read_excel(file_path)

        # Normalize district names
        df['DISTRICT'] = df['DISTRICT'].str.strip().str.lower()

        # Update urban and suburban lists to lowercase
        urban_districts = [district.lower() for district in ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Navi Mumbai']]
        suburban_districts = [district.lower() for district in ['Kolhapur', 'Jalgaon', 'Satara', 'Ahmednagar', 'Solapur']]

        # Check the unique districts in the dataset
        print("All Districts in Dataset:", df['DISTRICT'].unique())

        # Classifying each district as Urban or Suburban based on the lists
        df['Area Type'] = df['DISTRICT'].apply(
            lambda x: 'Urban' if x in urban_districts else ('Suburban' if x in suburban_districts else 'Unknown')
        )

        # Filter urban and suburban data
        urban_data = df[df['Area Type'] == 'Urban']
        suburban_data = df[df['Area Type'] == 'Suburban']

        # Debug: Check the classified data
        print("Urban Data:\n", urban_data)
        print("Suburban Data:\n", suburban_data)

        # Check if urban and suburban data are not empty
        if urban_data.empty or suburban_data.empty:
            messagebox.showerror("Error", "Urban or Suburban data is empty! Please check district classification.")
            return

        # Compute the standard deviation of TOTAL IPC CRIMES for urban and suburban areas
        urban_crime_rates = urban_data['TOTAL IPC CRIMES']
        suburban_crime_rates = suburban_data['TOTAL IPC CRIMES']

        # Calculate the standard deviation for urban and suburban crime rates
        urban_std = urban_crime_rates.std()
        suburban_std = suburban_crime_rates.std()

        # Display the results in the GUI
        urban_std_label.config(text=f"Urban Crime Rate Std: {urban_std:.2f}")
        suburban_std_label.config(text=f"Suburban Crime Rate Std: {suburban_std:.2f}")

        # Compare and update the comparison label
        if urban_std > suburban_std:
            comparison_label.config(text="Crime rates are more spread out in Urban areas.")
        else:
            comparison_label.config(text="Crime rates are more spread out in Suburban areas.")

        # Plot the bar chart comparing urban and suburban crime rates
        plot_comparison(urban_crime_rates, suburban_crime_rates)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {str(e)}")

# Function to plot the comparison between urban and suburban areas
def plot_comparison(urban_data, suburban_data):
    # Clear the previous plot
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    # Create a figure and plot the data
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Bar chart for mean crime rates comparison
    crime_means = [urban_data.mean(), suburban_data.mean()]
    crime_labels = ['Urban', 'Suburban']
    
    ax.bar(crime_labels, crime_means, color=['blue', 'green'])
    ax.set_title('Mean Crime Rate Comparison')
    ax.set_ylabel('Mean IPC Crime Rate')  # Updated label
    ax.set_ylim(0, max(crime_means) * 1.1)  # Set y-axis limit
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))  # Format y-axis values
    
    # Display the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main application window
root = tk.Tk()
root.title("Crime Rate Standard Deviation Comparison - Maharashtra")

# Label to indicate data source
data_source_label = tk.Label(root, text="Data related to Maharashtra", font=("Arial", 14))
data_source_label.pack(pady=5)

# Create a button to load the Excel file and calculate
load_button = tk.Button(root, text="Load Excel File and Calculate", command=load_and_calculate)
load_button.pack(pady=10)

# Labels to display the results
urban_std_label = tk.Label(root, text="Urban Crime Rate Std: N/A", font=("Arial", 12))
urban_std_label.pack(pady=5)

suburban_std_label = tk.Label(root, text="Suburban Crime Rate Std: N/A", font=("Arial", 12))
suburban_std_label.pack(pady=5)

# Label to display the comparison
comparison_label = tk.Label(root, text="Comparison: N/A", font=("Arial", 12))
comparison_label.pack(pady=10)

# Frame to hold the chart
chart_frame = tk.Frame(root)
chart_frame.pack(pady=20)

# Run the GUI event loop
root.mainloop()
