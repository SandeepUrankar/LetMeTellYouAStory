# Import Statements
import html
import pickle
import time
import webbrowser


# Global Variables
global stories
stories = dict()
global categories 
categories = set()


def load_data():
    with open('files/saved_stories.pkl', 'rb') as f:
        global stories 
        stories = pickle.load(f)
    for i in stories.keys():
        global categories
        categories.add(stories[i]['Category'])
    categories = list(categories)


def display_story(category):
    titles = []
    for i in stories.keys():
        if(stories[i]['Category'] == category):
            titles.append(stories[i]['Title'])
    i = 0
    print('Choose a story -')
    for title in titles:
        print(f'{i} - {title}')
        i += 1
    title_selected = int(input())
    title_selected = titles[title_selected]
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
    
    html_content = "<html> <head> <title> Story </title> <body>"+ (stories[bookno]['content']).replace('\n','<br>')+ "</body> </html>"

    html_content.format(stories[bookno]['content'])

    with open('files/index.html','w') as html_file:
        html_file.write(html_content)
        print('Opening Story in browser.')
    webbrowser.open_new_tab('files/index.html')


def main():
    load_data()
    print('Choose the category of story which you want to read...')
    i = 0
    for cat in categories:
        print(f'{i} - {cat}')
        i += 1
    category_choosed = int(input())
    category_choosed = categories[category_choosed]
    print()
    print(category_choosed, 'it is !')
    display_story(category_choosed)
    


main()