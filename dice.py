import streamlit as st
import numpy as np

def roll_dice(num_dice, sides):
  """
  Simulates rolling multiple dice with a specified number of sides.
  """
  rolls = [np.random.randint(1, sides) for _ in range(num_dice)]
  total = sum(rolls)
  return rolls, total

# Title and instructions
st.title("Interactive Dice Roller")
st.write("Choose the type of dice and roll!")

# Select dice type
dice_types = {
    "Standard D6": 6,
    "D8": 8,
    "D10": 10,
    "D12": 12,
    "D20": 20,
}
selected_type = st.selectbox("Choose your dice:", list(dice_types.keys()))
sides = dice_types[selected_type]

# Number of dice input
num_dice = st.number_input("Number of dice (1-10):", min_value=1, max_value=10)

# Roll button and results
if st.button("Roll!"):
  rolls, total = roll_dice(num_dice, sides)
  st.write(f"You rolled: {rolls}")
  st.write(f"Total: {total}")

