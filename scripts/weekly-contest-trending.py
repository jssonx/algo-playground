import requests
import matplotlib.pyplot as plt
import math

def fetch_user_contest_ranking_history(username):
    url = 'https://leetcode.com/graphql'
    query = '''
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
    variables = {'username': username}
    try:
        response = requests.post(url, json={'query': query, 'variables': variables})
        if response.status_code == 200:
            data = response.json()
            return data['data']['userContestRankingHistory']
        else:
            print('Request failed with status code:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Request failed:', str(e))
        return None

def plot_user_contest_rating_history(user_contest_ranking_history):
    attended_contests = [ranking_history for ranking_history in user_contest_ranking_history if ranking_history['attended']]
    contest_titles = [contest['contest']['title'] for contest in attended_contests]
    ratings = [contest['rating'] for contest in attended_contests]
    rankings = [contest['ranking'] for contest in attended_contests]

    x = range(len(contest_titles))
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, ratings, marker='o', color='darkgreen', alpha=0.9, linewidth=2, markersize=5, markeredgecolor='black')

    ax.set_xticks(x)
    ax.set_title('Ratings')
    ax.set_facecolor('white')
    for i in range(len(rankings)):
        ax.text(x[i], ratings[i], f'Rank {rankings[i]}', ha='center', va='bottom', fontsize=7)
    
    # Automatically detect rating range
    min_rating = math.floor(min(ratings) / 100) * 100
    max_rating = math.ceil(max(ratings) / 100) * 100
    color_regions = [(i, i+100) for i in range(min_rating, max_rating, 100)]
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange']
    for i, region in enumerate(color_regions):
        color = colors[i % len(colors)]
        ax.fill_between(x, region[0], region[1], color=color, alpha=0.1)

    plt.tight_layout()
    plt.show()

def main():
    username = "0xjsson"
    user_contest_ranking_history = fetch_user_contest_ranking_history(username)
    plot_user_contest_rating_history(user_contest_ranking_history)

if __name__ == "__main__":
    main()