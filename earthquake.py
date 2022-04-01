from flask import Flask, url_for, render_template, request, json

with open('earthquakes.json') as json_earthquakes:
    earthquakes = json.load(json_earthquakes)
    print (earthquakes[0]['location']['name'])
    print (earthquakes[0]['location']['name'])
    
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
    for x in earthquakes:
        if x['location']['name'] in earthquake_state:
            earthquake_state[(x['location'])]# finish looping through and adding missing spots
            # if california in earthquake_state add 1 to california
            # else add california to the dictornary and add one 
        else
        if x['location']['name'] == 'California':
            CA_earthquake += 1
    return CA_earthquake
print (get_earthquake_amount())







if __name__=="__main__":
    app.run(debug=True)