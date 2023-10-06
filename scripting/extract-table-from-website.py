import pandas as pd

simpson_list = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')

print(len(simpson_list))