from flask import Flask, url_for, render_template, request, json

with open('earthquakes.json') as json_earthquakes:
    earthquakes = json.load(json_earthquakes)

    
app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    return render_template('page1.html')

def get_earthquake_amount():
    # returns abount of earthquakes per countrie or us state
    earthquake_state = {}
    CA_earthquake = 0
    state = ""
    for x in earthquakes:
        if x['location']['name'] in earthquake_state:
            state = x['location']['name']
            i = earthquake_state[state]
            i += 1
            earthquake_state[state] = i# finish looping through and adding missing spots
            # if california in earthquake_state add 1 to california
            # else add california to the dictornary and add one 
        else:
            state = x['location']['name']
            earthquake_state[state] = 1
            
    # return earthquake_state
    quake_keys = earthquake_state.keys()
    top_state = ""
    a = 0
    top_five = earthquake_state['Burma']
    for x in earthquake_state:
        if earthquake_state[x] > top_five:
            top_five = earthquake_state[x]
            top_state = quake_keys[a]
            a += 1
    return top_state
print(get_earthquake_amount())


if __name__=="__main__":
    app.run(debug=True)