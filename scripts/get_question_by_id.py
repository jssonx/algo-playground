# Reference: https://github.com/aylei/leetcode-rust/issues/12
import requests
import json
import argparse
import os
from pprint import pprint

class LeetCodeClient:
    def __init__(self):
        self.url = 'https://leetcode.com/graphql'
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.query_problemset_question_list = """
            query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
                problemsetQuestionList: questionList(
                    categorySlug: $categorySlug
                    limit: $limit
                    skip: $skip
                    filters: $filters
                ) {
                    total: totalNum
                    questions: data {
                        frontendQuestionId: questionFrontendId
                        titleSlug
                    }
                }
            }
        """

        self.query_question_data = """
            query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    boundTopicId
                    title
                    titleSlug
                    content
                    translatedTitle
                    translatedContent
                    isPaidOnly
                    difficulty
                    likes
                    dislikes
                    similarQuestions
                    exampleTestcases
                    categoryTitle
                    topicTags {
                        name
                        slug
                        translatedName
                    }
                    companyTagStats
                    codeSnippets {
                        lang
                        langSlug
                        code
                    }
                    stats
                    hints
                    solution {
                        id
                        canSeeDetail
                        paidOnly
                    }
                    status
                    sampleTestCase
                    metaData
                    judgerAvailable
                    judgeType
                    mysqlSchemas
                    enableRunCode
                    enableTestMode
                    enableDebugger
                    envInfo
                    libraryUrl
                    adminUrl
                }
            }
        """

    def get_question_data(self, question_id):
        # First, get the list of all questions
        variables = {
            "categorySlug": "",
            "skip": 0,
            "limit": 5000,  # Increase this if you have more questions
            "filters": {}
        }

        data = {
            'operationName': 'problemsetQuestionList',
            'query': self.query_problemset_question_list,
            'variables': variables
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        json_response = response.json()

        # Now, find the titleSlug for the questionId we are interested in
        title_slug = None
        for question in json_response['data']['problemsetQuestionList']['questions']:
            if question['frontendQuestionId'] == question_id:
                title_slug = question['titleSlug']
                break

        if title_slug is None:
            print(f"No question found with id: {question_id}")
            return None

        # Now, we can get the question data using the titleSlug
        variables = {
            "titleSlug": title_slug,
        }

        data = {
            'operationName': 'questionData',
            'query': self.query_question_data,
            'variables': variables
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        json_response = response.json()

        return json_response

from bs4 import BeautifulSoup


def main(question_id):
    client = LeetCodeClient()
    response_data = client.get_question_data(question_id)
    if response_data is None:
        print("No data received from LeetCode")
        return
    original_data = response_data["data"]["question"]
    
    # Save to lc-cache
    question_data = {
        "id": original_data.get("questionId"),
        "fid": original_data.get("questionFrontendId"),
        "name": original_data.get("title"),
        "slug": original_data.get("titleSlug"),
        "tags": [tag["slug"] for tag in original_data.get("topicTags")],
        "level": original_data.get("difficulty"),
        "category": original_data.get("categoryTitle"),
        "content": original_data.get("content"),
        "hint": original_data.get("hints"),
    }
    slug = question_data["slug"]
    with open(os.path.join(os.getcwd(), "lc-cache", f"{question_id}.{slug}.json"), "w") as json_file:
        json.dump(question_data, json_file, indent=4)
    
    # Save to algorithms
    soup = BeautifulSoup(question_data["content"], 'html.parser')
    question_content = soup.get_text()
    question_content = '\n'.join('# ' + line for line in question_content.split('\n'))
    with open(os.path.join(os.getcwd(), "algorithms/python", f"{question_id}.{slug}.py"), "w") as python_file:
        python_file.write(question_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("question_id", help="The ID of the question to retrieve data for")
    args = parser.parse_args()
    main(args.question_id)