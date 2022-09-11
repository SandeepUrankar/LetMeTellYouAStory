# Import Statements
import datetime
import pickle
import webbrowser
from flask import Flask

# Global Variables
global stories
stories = dict()
global recos
recos = dict()
global categories 
categories = set()
global app
app = Flask(__name__)


# Function to create logs.
def create_log(data):
    global log
    log = open("logs.txt", "a")
    log.write(str(datetime.datetime.now()) + "\t" + data + "\n")


# This function loads the stories and their recommendations into the dict DS
def load_data():
    create_log('Loading the data.')
    with open('files/saved_stories.pkl', 'rb') as f:
        global stories 
        stories = pickle.load(f)
    with open('files/saved_recomendations.pkl', 'rb') as f:
        global recos 
        recos = pickle.load(f)
    for i in stories.keys():
        global categories
        categories.add(stories[i]['Category'])
    categories = list(categories)
    create_log('Done loading the data.')



# When http://127.0.0.1:5000/{reco} is opened in the browser while the flask
# server is turned on, the argument will be passed to this function and the
# stories requested is displayed.
@app.route("/<bookno>")
def display_web(bookno):
    html =  '<html> <head><style>{margin: 0;}#title{text-align: center;font-size: 2rem;padding: 1rem;}#story{text-align: center;}</style> <title>'+ (stories[bookno]['Title']) +"</title> </head> <body> <p id='title'>"+(stories[bookno]['Title'])+"</p><p id='story'>" +(stories[bookno]['content']).replace('\n','<br>')+ "</p><br><p>Recomended to read</p>"#</body> </html>"
    create_log('Displaying the story with '+stories[bookno]['Title']+' title in the browser with its recommendations.')
    for reco in recos[bookno]:
        link = f'http://127.0.0.1:5000/{reco}'
        html += f'<a href={link}>'+stories[reco]['Title']+'</a><br>'
    return html


# This method displays the category of stories and let the user to pick the
# category and displays different stories present in that category and the 
# chosen story is displayed in the browser.
def display_story(category):
    titles = []
    for i in stories.keys():
        if(stories[i]['Category'] == category):
            titles.append(stories[i]['Title'])
    i = 0
    create_log(f'Displaying the story titles present in {category} category.')
    print('Choose a story -')
    for title in titles:
        print(f'{i} - {title}')
        i += 1
    title_selected = int(input())
    title_selected = titles[title_selected]
    create_log(f'Chosen title of the story is {title_selected}.')
    print()
    print(title_selected, 'right away!')
    bookno = ''
    for i in stories.keys():
        if(stories[i]['Title'] == title_selected):
            bookno = i
    print('Author - ',stories[bookno]['Author'])
    # print(stories[bookno]['content'])
    # story = stories[bookno]['content'].split('\n')
    # for line in story:
    #     print(line,end='')
    #     input()
    #     # time.sleep(0.5)
    print(bookno)
    webbrowser.open_new_tab(f'http://127.0.0.1:5000/{bookno}')
    app.run()

    # html_content = '<html> <head><link rel="stylesheet" href="style.css"> <title>'+ (stories[bookno]['Title']) +"</title> </head> <body> <p id='title'>"+(stories[bookno]['Title'])+"</p><p id='story'>" +(stories[bookno]['content']).replace('\n','<br>')+ "</p></body> </html>"

    # html_content.format(stories[bookno]['content'])

    # with open('files/index.html','w') as html_file:
    #     html_file.write(html_content)
    #     print('Opening Story in browser.')
    # webbrowser.open_new_tab('files/index.html')


# Main functions
def main():
    load_data()
    print('Choose the category of story which you want to read...')
    create_log('Displaying the different categories.')
    i = 0
    for cat in categories:
        print(f'{i} - {cat}')
        i += 1
    category_choosed = int(input())
    category_choosed = categories[category_choosed]
    create_log(f'Chosen category is {category_choosed}.')
    print()
    print(category_choosed, 'it is !')
    display_story(category_choosed)


main()