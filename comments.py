'''
https://github.com/googleapis/google-api-python-client/blob/main/docs/README.md
https://stackoverflow.com/questions/34743774/understanding-how-to-use-the-google-apis-client-library-with-python 
'''
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

API_KEY = "AIzaSyBdxCc01DcVGiMboltSgInuhQYBMxJjLTs"

service = build('drive', 'v3', developerKey=API_KEY)

my_file_id = "1Wkil6zufjdq5ZkRGYPwqST3r7liOXNjyTxsq-OQc10I"
anchor =  {
      'r': 'myRevisionId',
      'a': [
      {
        'line':
        {
          'n': 12,
          'l': 3,
        }
      },
      {
        'line':
        {
          'n': 18,
          'l': 1,
        }
      }]
    }
anchor_json = json.dumps(anchor)
comment_body = {
  "content": "THIS COMMENT WAS LEFT USING THE GOOGLE DOCS PYTHON CLIENT",
  "anchor": anchor_json
}

try:
  request = service.comments().create(
    fileId=my_file_id, 
    body=comment_body,
    fields="id,content"
  )
  request.execute()
  print('Comment added successfully')
except HttpError as e:
  print(f'An error occurred: {e}')
