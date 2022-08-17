import clustering_code
import os

def clean_t_dataset():
    try:
        os.remove('Dataset_to_plot.csv')
    except:
        pass

def get_movie_name():
    input_movie = input("Enter the movie name: ")
    movies = clustering_code.cluster_everything(input_movie)
    if type(movies) == int:#for return 0
        pass
    else:
        print(movies)

get_movie_name()