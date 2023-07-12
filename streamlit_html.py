import streamlit as st
import streamlit.components.v1 as components

# Render HTML/CSS code
html_code = '''
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-image: url("https://reemsbucket.s3.us-west-2.amazonaws.com/background.jpeg");
      background-repeat: no-repeat;
      background-size: cover;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .text-input {
      width: 300px;
      padding: 10px;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <input type="text" class="text-input" placeholder="Enter your text" id="user_input">
  <script>
    var userInput = document.getElementById('user_input');
    userInput.addEventListener('input', function() {
      // Retrieve the user input and update Streamlit's text_input widget
      var text = userInput.value;
      Streamlit.setComponentValue(text);
    });
  </script>
</body>
</html>
'''

# Display the HTML code
component_value = components.html(html_code, height=200)

# st.text_input("Enter your text", value=component_value, key='text_input')
