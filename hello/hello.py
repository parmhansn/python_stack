from flask import Flask, render_template, request  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)
          				# Just for fun, print __name__ to see what it is

@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response.


@app.route('/dojo')        
                         
def Dojo():
    return 'Dojo!'


@app.route('/say/flask')
                         
def hi_flask():
	print("Handle this routing request")
	return 'Hi Flask!'


@app.route('/say/michael')
                         
def hi_michael():
	print("Handle this routing request")
	return 'Hi Michael'


@app.route('/say/john')
                         
def hi_john():
	print("Handle this routing request")
	return 'Hi John!'



@app.route('/repeat/<number>/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(number, name):
    print(name)
    print(number)
    return name*int(number)



@app.route('/success')
def success():
	print("-"*80, "Jello Success")

	return "success"




if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.






    