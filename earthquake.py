from flask import Flask, url_for, render_template, request, json, Markup

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
    # Sorts data amount of earthquakes in each state
    earthquake_state = {}
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
    # quake_keys = earthquake_state.keys()
    # returns the top 5 states 
    top_state = ['state1','state2','state3','state4','state5']
    top_five = [0] # int amount of earthquakes in the top states
    i = 0
    for top in top_state:
        for x in earthquake_state:
            if earthquake_state[x] in top_five:
                i += 0
            else:
                if earthquake_state[x] > top_five[i]:
                    # top_five = earthquake_state[x]
                    top_five.insert(i, earthquake_state[x])
                    # top_state = quake_keys[x]
                    # i += 1
        i += 1
    graph_points = ""
    i = 0
    for top in top_state:
        # { y: 300878, label: "Venezuela" },
        placehold = str(top_five[i])
        graph_points = graph_points + Markup('{ y: ' + placehold + ', label: "' + top_state[i] + '" }, ')
        i += 1
    graph_points = graph_points[:-2]
    print(graph_points)
    return graph_points
    # returns the top 5 states formated for the graph
print(get_earthquake_amount())



if __name__=="__main__":
    app.run(debug=True)