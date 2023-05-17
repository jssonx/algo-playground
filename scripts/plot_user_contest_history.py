import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math

URL = 'https://leetcode.com/graphql'
QUERY = '''
query($username: String!) {
    userContestRankingHistory(username: $username) {
        attended
        trendDirection
        problemsSolved
        totalProblems
        finishTimeInSeconds
        rating
        ranking
        contest {
            title
            startTime
        }
    }
}
'''

def fetch_data(url, query, variables):
    try:
        response = requests.post(url, json={'query': query, 'variables': variables})

        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'Request failed with status code: {response.status_code}'}
    except requests.exceptions.RequestException as e:
        return {'error': f'Request failed: {str(e)}'}

def fetch_user_contest_ranking_history(username):
    variables = {'username': username}
    data = fetch_data(URL, QUERY, variables)
    if 'error' in data:
        return None
    return data['data']['userContestRankingHistory']

def plot_graph(contest_titles, ratings, rankings):
    x = range(len(contest_titles))
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, ratings, marker='o', color='darkgreen', alpha=0.9, linewidth=2, markersize=5, markeredgecolor='black')

    ax.set_xticks(x)
    ax.set_title('Ratings')
    ax.set_facecolor('white')
    for i in range(len(rankings)):
        ax.text(x[i], ratings[i], f'{rankings[i]}', ha='center', va='bottom', fontsize=8)
    
    min_rating = math.floor(min(ratings) / 100) * 100
    max_rating = math.ceil(max(ratings) / 100) * 100
    color_regions = [(i, i+100) for i in range(min_rating, max_rating, 100)]
    colors = ['red', 'orange', 'yellow', 'green', 'purple', 'pink', 'blue']
    for i, region in enumerate(color_regions):
        color = colors[i % len(colors)]
        ax.fill_between(x, region[0], region[1], color=color, alpha=0.1)

    plt.tight_layout()
    plt.savefig(f'./images/ratings.png')

def plot_user_contest_rating_history(user_contest_ranking_history):
    attended_contests = [ranking_history for ranking_history in user_contest_ranking_history if ranking_history['attended']]
    contest_titles = [contest['contest']['title'] for contest in attended_contests]
    ratings = [contest['rating'] for contest in attended_contests]
    rankings = [contest['ranking'] for contest in attended_contests]
    plot_graph(contest_titles, ratings, rankings)

def main():
    username = "0xjsson"
    user_contest_ranking_history = fetch_user_contest_ranking_history(username)
    if user_contest_ranking_history is not None:
        plot_user_contest_rating_history(user_contest_ranking_history)
    else:
        print("Failed to fetch user contest ranking history")

if __name__ == "__main__":
    main()