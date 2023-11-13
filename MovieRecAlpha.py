import pandas as pd
import warnings

warnings.simplefilter("ignore")

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

corrMatrix = movieRatings.corr(method='pearson', min_periods=100)

u_movie=[]
u_rate=[]
x=''
movlist=movies['title'].values.tolist()
while x!='done':
    x=input('enter movie name or done: ')
    if x=='done':
        break
    elif x not in movlist:
        print('unavailable')
    else:
        y=int(input('rating: '))
        u_movie.append(x)
        u_rate.append(y)
import pandas as pd
data = {'movies':u_movie,'rating':u_rate}
ratings = pd.DataFrame.from_dict(data)
ratings.head()

simmovies = pd.Series()
for i in range(0, len(u_movie)):
    print ("Adding sims for " , u_movie[i] , "...")
    sims = corrMatrix[u_movie[i]].dropna()
    sims = sims.map(lambda x: x * u_rate[i])
    simmovies = simmovies.append(sims)
    
print ("sorting...")
simmovies.sort_values(inplace = True, ascending = False)

simmovies = simmovies.groupby(simmovies.index).sum()
simmovies.sort_values(inplace = True, ascending = False)
simmovies.head(10)

filteredSims = simmovies.drop(u_movie)
filteredSims.head(10)
