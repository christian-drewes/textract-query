import boto3
import trp.trp2 as t2
from tabulate import tabulate

s3BucketName = 'ai-demo-fast'
plaintextimage = 'balance_sheet.png'
file_name = './balance_sheet.png'

textract = boto3.client('textract')

start_response = textract.start_document_analysis(
    DocumentLocation={
       'S3Object': {
            'Bucket': s3BucketName,
            'Name': plaintextimage
         }
   },
    FeatureTypes=['QUERIES'],
    QueriesConfig={
        "Queries": [
            {"Text": "What are the total assets?", 'Alias': 'TOTAL_ASSETS'},
            {"Text": "What is the total current liabilities?", 'Alias': 'TOTAL_CURRENT_LIABILITIES'},
            {"Text": "What is the total liabilties and equity?", 'Alias': 'TOTAL_LIABILITY_EQUITY'}
        ]
    }
)
# print(start_response)


response = textract.get_document_analysis(
    JobId='1f16f324c1e33ec9fbe2e2c56e8eea828d9e9f244af3ad649ba5ed3e39436373'
)

# print(response)
print(response['JobStatus'])
# for item in response["Blocks"]:
#     if item["BlockType"] == "QUERY_RESULT":
#            print(item)

d = t2.TDocumentSchema().load(response)
page = d.pages[0]

query_answers = d.get_query_answers(page=page)

print(tabulate(query_answers, tablefmt="github"))