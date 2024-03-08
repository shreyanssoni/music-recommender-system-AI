from flask import Flask, render_template, request
# from Recommender import Recommender
import pickle
import numpy as np

app = Flask(__name__)

# recommendations = pickle.load(open('recommendations.pkl','rb'))

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/recommend' ,methods=['post'])
def recommend(): 
    user_input = request.form.get('user_input')

    # class Recommender:
    #     def __init__(self, metric, algorithm, k, data, decode_id_song):
    #         self.metric = metric
    #         self.algorithm = algorithm
    #         self.k = k
    #         self.data = data
    #         self.decode_id_song = decode_id_song
    #         self.data = data
    #         self.model = self._recommender().fit(data)
    
    #     def make_recommendation(self, new_song, n_recommendations):
    #     # print(1)
    #         recommended = self._recommend(new_song=new_song, n_recommendations=n_recommendations)
    #         print("... Done")
    #         return recommended 
    
    #     def _recommender(self):
    #     # print(2)
    #         # return NearestNeighbors(metric=self.metric, algorithm=self.algorithm, n_neighbors=self.k, n_jobs=-1)
    
    #     def _recommend(self, new_song, n_recommendations):
    #     # print(3)
    #     # Get the id of the recommended songs
    #         recommendations = []
    #         recommendation_ids = self._get_recommendations(new_song=new_song, n_recommendations=n_recommendations)
    #     # print("These are the recommendation ids: " , recommendation_ids
    #     # print("This is the return value " , recommendation_ids)
    #     # return the name of the song using a mapping dictionary
    #         recommendations_map = self._map_indeces_to_song_title(recommendation_ids)
    #     # print("this is the return value", recommendations_map)
    #     # Translate this recommendations into the ranking of song titles recommended
    #     # print(7)
    #         for i, (idx, dist) in enumerate(recommendation_ids):
    #             if(idx in recommendations_map):
    #                 recommendations.append(recommendations_map[idx])
    #         return recommendations

                 
    #     def _get_recommendations(self, new_song, n_recommendations):
    #     # print(4)
    #     # Get the id of the song according to the text
    #         recom_song_id = self._fuzzy_matching(songname=new_song)
    #     # Start the recommendation process
    #         print(f"Starting the recommendation process for {new_song} ...")
    #     # recom_song_id = self.data[recom_song_id].reshape(1, -1)
    #     # Return the n neighbors for the song id
    #         distances, indices = self.model.kneighbors(self.data[recom_song_id], n_neighbors=n_recommendations+1)
    #         return sorted(list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())), key=lambda x: x[1])[:0:-1]
    
    #     def _map_indeces_to_song_title(self, recommendation_ids):
    #     # print(5)
    #     # get reverse mapper
    #         return {songid: song_title for song_title, songid in self.decode_id_song.items()}
    
    #     def _fuzzy_matching(self, songname):
    #     # print(6)
    #         match_tuple = []
    #     # get match
    #         for title, idx in self.decode_id_song.items():
    #             ratio = fuzz.ratio(title.lower(), songname.lower())
    #             if ratio >= 60:
    #                 match_tuple.append((title, idx, ratio))
    #     # sort
    #         match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
    #         if not match_tuple:
    #             print(f"The recommendation system could not find a match for {songname}")
    #             return
    #         return match_tuple[0][1]

if __name__ == '__main__':
    app.run(debug=True)