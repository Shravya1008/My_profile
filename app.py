from flask import Flask, request, render_template_string

app = Flask(__name__)

# 📄 Full Single-Page HTML Template
page_html = r'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Profile Page</title>
  <style>
    body {
      background-color: lightblue;
      font-family: Arial, sans-serif;
      padding: 20px;
    }

    h1 {
      text-align: center;
      color: darkblue;
    }

    img {
      display: block;
      margin: 20px auto;
      width: 200px;
      border-radius: 10px;
    }

    p {
      text-align: center;
      font-size: 18px;
    }

    form {
      width: 300px;
      margin: 30px auto;
      padding: 20px;
      background-color: #f0f0f0;
      border-radius: 10px;
    }

    input, textarea {
      width: 100%;
      padding: 8px;
      margin-top: 6px;
      margin-bottom: 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    input[type="submit"], button {
      display: block;
      margin: 15px auto 0;
      padding: 10px 20px;
      background-color: darkblue;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover, input[type="submit"]:hover {
      background-color: navy;
    }

    .response {
      text-align: center;
      font-weight: bold;
      color: green;
    }
  </style>
</head>
<body>

  <h1>Welcome to My Profile Page</h1>

  <img src="/static/My_Photo.jpg" alt="My_Photo">

  <p>Hello! I'm Shravya Sri. I'm a tech enthusiast who loves web development and design. Nice to meet you!</p>

  {% if submitted %}
    <p class="response">Thanks, {{ name }}! We'll reach out to you at {{ email }}.</p>
  {% endif %}

  <form method="POST">
    <label>Your Name:</label>
    <input type="text" name="name" required>

    <label>Email:</label>
    <input type="email" name="email" required>

    <label>Message:</label>
    <textarea name="message" rows="4" required></textarea>

    <input type="submit" value="Submit">
  </form>

  <button onclick="sayHello()">Say Hello</button>

  <script>
    function sayHello() {
      let name = prompt("What's your name?");
      if (name) {
        alert("Hello, " + name + "!");
      }
    }
  </script>

</body>
</html>
'''

# 🏠 Only One Route
@app.route('/', methods=['GET', 'POST'])
def home():
    name = email = ''
    submitted = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        submitted = True
    return render_template_string(page_html, name=name, email=email, submitted=submitted)

# 🚀 Start App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
