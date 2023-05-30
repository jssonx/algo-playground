import requests
import json

# 定义一个introspection查询来获取schema
introspection_query = '''
query {
  __schema {
    types {
      name
      kind
      fields {
        name
        args {
          name
          type {
            name
            ofType {
              name
            }
          }
        }
        type {
          name
          ofType {
            name
          }
        }
      }
    }
  }
}
'''

# LeetCode GraphQL API的URL
url = 'https://leetcode.com/graphql'

# 发送请求
response = requests.post(
    url,
    json={'query': introspection_query},
    headers={'Content-Type': 'application/json'}
)

# 检查响应是否有效
if response.status_code == 200:
    # 解析响应并打印结果
    result = json.loads(response.text)
    print(json.dumps(result, indent=2))
else:
    print(f'Error: {response.status_code} - {response.text}')