# Reference: https://github.com/aylei/leetcode-rust/issues/12
import requests
import json

class LeetCodeClient:
    def __init__(self):
        self.url = 'https://leetcode.com/graphql'
        self.headers = {
            'Content-Type': 'application/json',
        }

    def get_question_data(self, question_id):
        # First, get the list of all questions
        query = """
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

        variables = {
            "categorySlug": "", 
            "skip": 0, 
            "limit": 1000,  # Increase this if you have more questions
            "filters": {}
        }

        data = {
            'operationName': 'problemsetQuestionList',
            'query': query,
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
        query = """
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

        variables = {
            "titleSlug": title_slug, 
        }

        data = {
            'operationName': 'questionData',
            'query': query,
            'variables': variables
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        json_response = response.json()

        return json_response

# 使用示例
client = LeetCodeClient()
question_data = client.get_question_data("1")  # Replace "1" with your questionId

# 打印问题数据
print(json.dumps(question_data, indent=4))
