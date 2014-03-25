from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')




# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/_word_filter')
def word_filter():
    #get text from template
    a = request.args.get('a', 0, type=str)
    result=[]
    result=filter(a)
    return jsonify(result=result)

def filter(a):
    
    storefile = []

    z=a
    #split the input string
    y=a.split()

    storefile=y

    temp = storefile
    #make a hash for replacement
    replacements = {
		'maverick':'********', 
		'ranger':'******',
		'rocket':'******',
		'king':'****', 
		'heat':'****',
		'chicago':'*******',
		'bear':'****',
		'wizard':'******',
		'seattle':'*******',
		'atlanta':'*******',
		'miami':'*****',
		'austin':'******',
		'boston':'******',
		'pittsburgh':'**********',
		'saint':'*****',
		'hawk':'****'
	}

    #replace the input string
    for src, target in replacements.iteritems():
        z=z.replace(src,target)



    z=z.split()
    result=[]
    i=0

    #check for other conditions, like if only half of the word is replaced with *
    for line in y:
        if( line in replacements):
            
            temp=replacements[line]
            result.append(temp)
	    
        else:
            
            if (z[i].count('*')==len(z[i])):
                result.append(z[i])
            else:
                result.append(line)
        i = i+1
    #return the result
    return result



if __name__ == '__main__':
    app.run(
        debug=True
    )
