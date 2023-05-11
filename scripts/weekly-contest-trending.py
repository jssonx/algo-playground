import requests
import matplotlib.pyplot as plt

def fetch_user_contest_ranking_history(username):
    query = '''
    {
        userContestRankingHistory(username: "%s") {
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
    ''' % username

    url = 'https://leetcode.com/graphql'
    response = requests.post(url, json={'query': query})
    data = response.json()
    return data['data']['userContestRankingHistory']

def plot_user_contest_rating_history(user_contest_ranking_history):
    attended_contests = [ranking_history for ranking_history in user_contest_ranking_history if ranking_history['attended']]
    contest_titles = [contest['contest']['title'] for contest in attended_contests]
    ratings = [contest['rating'] for contest in attended_contests]
    rankings = [contest['ranking'] for contest in attended_contests]

    x = range(len(contest_titles))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, ratings, marker='o', color='blue', alpha=0.7, linewidth=2, markersize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(contest_titles, rotation=45, fontsize=8)
    ax.set_xlabel('Contest', fontsize=10)
    ax.set_ylabel('Rating', fontsize=10)
    ax.set_title('Contest Rating History')
    [ax.spines[i].set_color('black') for i in ax.spines]
    [ax.spines[i].set_linewidth(1) for i in ax.spines]
    ax.set_facecolor('white')
    for i in range(len(rankings)):
        ax.text(x[i], ratings[i], f'Rank {rankings[i]}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()

def main():
    username = "0xjsson"
    user_contest_ranking_history = fetch_user_contest_ranking_history(username)
    plot_user_contest_rating_history(user_contest_ranking_history)

if __name__ == "__main__":
    main()