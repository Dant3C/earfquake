from flask import Flask, url_for, render_template, request, json, Markup

with open('earthquakes.json') as json_earthquakes:
    earthquakes = json.load(json_earthquakes)


app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
@app.route("/")
def render_main():
    return render_template('home.html')
@app.route("/page1")
def render_page1():

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
    # returns the top 5 states
    top_state = ['']
    top_five = [0] # int amount of earthquakes in the top states
    i = 0
    for top in top_state:
        for x in earthquake_state: # x is name of state str
            if earthquake_state[x] in top_five:
                i += 0
            else:
                if earthquake_state[x] > top_five[i]:
                    top_five.insert(i, earthquake_state[x])
                    top_state.insert(i, x)
        i += 1
    graph_points = ""
    i = 0
    for top in "state000":
        # { y: 300878, label: "Venezuela" },
        placehold = str(top_five[i])
        graph_points = graph_points + Markup('{ y: ' + placehold + ', label: "' + top_state[i] + '" }, ')
        i += 1
    graph_points = graph_points[:-2]
    # returns the top 5 states formated for the graph
    return render_template('page1.html', graph_quake = graph_points)


@app.route("/page2")
def render_page2():
    return render_template('page2.html')
def list_of_states():
    state_list = []
    state_current = ""
    for x in earthquakes:
        if x['location']['name'] in state_list:
            pass
            # if california in earthquake_state add 1 to california
            # else add california to the dictornary and add one
        else:
            state_list.append(x['location']['name'])

    # liststates = list_of_states()
    form_options = ""
    # <option value="Internet Explorer">
    for opp in state_list:
        form_options = form_options + Markup('<option value="' + opp + '">')
    return form_options
@app.route("/state_facts")
def render_state_facts():
    selected = request.args['browser']
    s_facts = {} #dictornary
    i = 1
    for quakes in earthquakes:
        if quakes['location']['name'] == selected:
            s_facts['Earthquake ' + str(i)] = [quakes['location']['full'], quakes['time']['full'], quakes['impact']['magnitude']]
            i += 1
    s_facts_string = ''
    i = 1
    print(s_facts)
    for s in s_facts:
        s_facts_string = s_facts_string + s + '; ' + s_facts[s][0] + ' ' + s_facts[s][1]+ ' Magnitude: ' + str(s_facts[s][2]) + Markup('<br>')
        print(s_facts[s][0])
        # format this idk how im gonna do this
    return render_template('state_facts.html',html_facts = s_facts_string, state = selected)
@app.route("/page3")
def render_page3():

    return render_template('page3.html', stateOptions = list_of_states(), quake_facts = "facts")



if __name__=="__main__":
    app.run(debug=True)
