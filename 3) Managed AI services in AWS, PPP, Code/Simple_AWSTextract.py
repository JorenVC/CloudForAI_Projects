import boto3

# Initialize a session using Amazon Textract
client = boto3.client('textract')

# Specify the local image file
document_path = 'TestDocument_Voor_AIText.jpg'  # or .png, .pdf, etc.

# Read the image file
with open(document_path, 'rb') as document:
    image_bytes = document.read()

# Call Amazon Textract
response = client.detect_document_text(
    Document={
        'Bytes': image_bytes
    }
)

# Print the detected text
for item in response['Blocks']:
    if item['BlockType'] == 'LINE':
        print(item['Text'])
