# Import necessary libraries
import streamlit as st
import random

# Define function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Define the main function to generate passwords
def generate_password(length):
    # Define the character set
    character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-"
    
    # Generate password using specified length and characters from the character set
    password = ''.join(random.sample(character_set, length))
    
    return password

# Create the Streamlit UI
def main():
    # Set title and description
    st.title("Random Password Generator")
    st.write("This app generates a random password based on the length you specify.")

    # Add a slider to allow users to choose the length of the password
    password_length = st.slider("Select password length:", min_value=6, max_value=20, value=12, step=1)

    # Add a button to trigger password generation
    if st.button("Generate Password"):
        # Call the function to generate the password
        password = generate_password(password_length)
        
        # Display the generated password
        st.success(f"### Your random password is: \n ### {password}")

# Run the main function
if __name__ == "__main__":
    main()
