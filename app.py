from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        response = request.form["response"]
        intgang = random.randint(1, 4)
        if "intgangPrev" in request.form:
            intgangPrev = int(request.form["intgangPrev"])
            if intgangPrev == intgang:
                if intgang == 4:
                    intgang = 1
                else:
                    intgang += 1
        else:
            intgangPrev = 0

        if intgang == 1:
            reply = "That's interesting! Tell me more!"
        elif intgang == 2:
            reply = "Wow! That's amazing, how did that make you feel?"
        elif intgang == 3:
            temp = response.lower().split()[-1].strip(".")
            temp = temp.replace(temp[0], temp[0].upper())
            reply = "{}? That's interesting, tell me more!".format(temp)
        elif intgang == 4:
            reply = "I see, why do you think that is?"

        return render_template_string(template, response=response, reply=reply, intgangPrev=intgang)
    return render_template_string(template, response="", reply="", intgangPrev=0)

template = """
<!doctype html>
<html lang="en">
  <head>
    <title>Chat with Ronald</title>
    <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        font-family: Arial, sans-serif;
      }
      .container {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Hi all! I'm Ronald! Tell me what's going on in your life!</h1>
      <form method="post">
        <input type="text" name="response" value="{{ response }}">
        <input type="hidden" name="intgangPrev" value="{{ intgangPrev }}">
        <input type="submit" value="Submit">
      </form>
      <p>{{ reply }}</p>
    </div>
  </body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)