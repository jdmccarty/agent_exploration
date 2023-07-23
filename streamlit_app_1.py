import streamlit as st
import graphviz as gv

# Create a Digraph object
flowchart = gv.Digraph()

# Add nodes
flowchart.node('A', 'Step 1')
flowchart.node('B', 'Step 2')
flowchart.node('C', 'Step 3')
flowchart.node('D', 'Step 4')
flowchart.node('E', 'Step 5')

# Add edges
flowchart.edges(['AB', 'BC', 'CD', 'DE'])

# Save the flowchart as a png image
flowchart.format = 'png'
flowchart.render('flowchart')

# Display the flowchart image in Streamlit
st.image('flowchart.png')

