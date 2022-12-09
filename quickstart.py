from __future__ import print_function

import os
from apiclient import errors

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
# SCOPES = ['https://www.googleapis.com/auth/documents']
# SCOPES = ['https://www.googleapis.com/auth/drive']

# The ID of a sample document.
DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'


def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        # print('The title of the document is: {}'.format(document.get('title')))
        return service
    except HttpError as err:
        print(err)

def create_doc(title, scopes):
    creds = get_creds(scopes)
    service = build("docs", 'v1', credentials=creds)
    title = 'Test Doc'
    body = {
        'title': title
    }
    doc = service.documents() \
        .create(body=body).execute()
    print('Created document with title: {0}'.format(doc.get('title')))    

# def delete_file(service, file_id):
#   """Permanently delete a file, skipping the trash.

#   Args:
#     service: Drive API service instance.
#     file_id: ID of the file to delete.
#   """
#   try:
#     service.files().delete(fileId=file_id).execute()
#   except HttpError as err:
#     print(err)

def get_creds(scopes):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def resume_stuff(services):
    """Creates resume based on user input"""
    # Deletes token to generate the appropriate service (from new token)
    # os.remove("token.json")
    question = input("Please enter 1 if creating new resume, or 2 if editing existing resume: ")
    title = input("Please enter the title of your resume: ")
    # title = input("Please enter title for resume: ")
    if question == "1":
        file_id = create_copy(title, services['drive'])
        return file_id
    else:
        edit_resume()

def edit_resume():
    """TODO"""
    return
def create_copy(title, service):
    '''Creates a resume using the resume template's structure'''
    # Creates Google Drive service that allows to use Google Drive API
    try:
        copy_title = '%s' % title
        body = {
        'name': copy_title
        }
        # Doc ID for the resume template 
        document_id = '1-JSL1i-WtjIkqhYjc0YtVeI09SicUM_CSQclooQouY4'
        drive_response = service.files().copy(
        fileId=document_id, body=body).execute()
        document_copy_id = drive_response.get('id')
        return document_copy_id
    except HttpError as err:
        print(err)

def remove_fields(file_id, service):
    """Removes content of a document given its document ID and the Google Docs service"""
    requests = [
        {
            'deleteContentRange': {
                'range': {
                    'startIndex': 1,
                    'endIndex': 5,
                }

            }

        },
    ]
    result = service.documents().batchUpdate(
        documentId=file_id, body={'requests': requests}).execute()

def delete_doc(file_id, scopes):
    """TODO"""
    try: 
        creds = get_creds(scopes)
        drive_service = build("drive", "v3", credentials=creds)
        drive_service.files().delete(fileId=file_id).execute()
    except HttpError as err:
        print(err)

def get_contents(metadata):
    """Grab the contents of a given document's metadata
    """
    return

if __name__ == '__main__':
    scopes_dict = {"Drive": ['https://www.googleapis.com/auth/drive'], 
    "Docs": ['https://www.googleapis.com/auth/documents']}
    scopes = scopes_dict["Drive"] + scopes_dict["Docs"]
    creds = get_creds(scopes)
    # Testing out how to print out the document's metadata
    docs_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)
    services = {"docs": docs_service, "drive": drive_service}
    file_id = resume_stuff(services)
    doc_metadata = docs_service.documents().get(documentId=file_id).execute()
    # print(doc_metadata)