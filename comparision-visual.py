import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot data from selected columns
def plot_data(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], alpha=0.5)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot of {y_column} vs {x_column}')
    st.pyplot()

# Main function for the Streamlit app
def main():
    st.title('CSV File Upload and Plotting App')

    # File upload and processing
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### Sample of the dataset:")
        st.write(df.head())

        # Select columns for plotting
        columns = df.columns.tolist()
        x_column = st.selectbox("Select X-axis column", columns)
        y_column = st.selectbox("Select Y-axis column", columns)

        # Plotting
        plot_data(df, x_column, y_column)

# Execute the main function
if __name__ == '__main__':
    main()
