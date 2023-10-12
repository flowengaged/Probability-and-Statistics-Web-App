import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    st.title('Probability and Statistics Web App')
    st.write('Use this app to analyze data, perform simulations, and visualize results.')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        
        # Dynamically select a column name
        column_name = st.selectbox("Select the column to visualize", data.columns)
        
        # Perform analysis on data here
        visualize_data(data, column_name)

    perform_simulation()

def perform_simulation():
    num_trials = st.number_input('Number of Trials', min_value=1, max_value=10000, value=1000)
    
    # Example: Simulating coin flips
    outcomes = np.random.choice(['Heads', 'Tails'], size=num_trials)
    unique, counts = np.unique(outcomes, return_counts=True)
    results = dict(zip(unique, counts))
    
    # Visualization of Simulation Results
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(results.keys(), results.values(), color=['skyblue', 'lightgreen'])
    ax.set_xlabel('Outcome', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.set_title('Simulation Results', fontsize=16)
    ax.grid(axis='y', alpha=0.75)
    
    # Display counts above bars
    for rect in ax.patches:
        height = rect.get_height()
        ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                    xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
    
    st.pyplot(fig)

def visualize_data(data, column_name):
    if column_name not in data.columns:
        st.error(f"The column name '{column_name}' does not exist in the data.")
        st.stop()
    
    # Visualization
    fig, ax = plt.subplots(figsize=(14, 8))  # Further increased figure size
    n, bins, patches = ax.hist(data[column_name], bins=30, alpha=0.75, color='skyblue', edgecolor='black')
    ax.set_xlabel(column_name, fontsize=16)
    ax.set_ylabel('Frequency', fontsize=16)
    ax.set_title(f'Histogram of {column_name}', fontsize=18)
    ax.grid(axis='y', alpha=0.75)
    
    # Display data values on histogram
    for i, rect in enumerate(ax.patches):
        height = rect.get_height()
        if height > 0:  # Only annotate if there is data
            ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                        xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', 
                        fontsize=10, rotation=45)  # Incremented fontsize
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()







