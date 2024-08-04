from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Google Drive API의 OAuth 2.0 범위 정의

class Google_Drive_Api:
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    def authenticate_gdrive():
        """Google Drive API 인증 및 서비스 객체 생성"""
        creds = None
        token_path = 'token.json'
        credentials_path = 'client_secret_41374105812-j8h10rickv0mv71orsmij3kni4hvpq3l.apps.googleusercontent.com.json'  # 다운로드한 OAuth 2.0 클라이언트의 JSON 파일 경로
    
        # 이전에 인증된 토큰이 있으면 로드
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, Google_Drive_Api.SCOPES)
    
        # 유효한 자격 증명이 없으면 로그인 흐름 시작
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, Google_Drive_Api.SCOPES)
                creds = flow.run_local_server(port=0)
        
            # 인증 후 토큰 저장
            with open(token_path, 'w') as token_file:
                token_file.write(creds.to_json())
    
        # Google Drive API 서비스 객체 생성
        service = build('drive', 'v3', credentials=creds)
        return service

    def upload_to_gdrive(service, file_path, file_name):
        """Google Drive에 파일 업로드 및 공유 가능한 링크 생성"""
        file_metadata = {
            'name': file_name,
            'mimeType': 'application/pdf'  # 이미지 파일 형식에 맞게 변경 가능
        }
        media = MediaFileUpload(file_path, mimetype='application/pdf')
    
        # 파일 업로드
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = uploaded_file.get('id')
    
        # 파일 공유 설정 변경 (공유 가능하도록)
        service.permissions().create(
            fileId=file_id,
            body={'type': 'anyone', 'role': 'reader'}
        ).execute()
    
        # 공유 가능한 링크 생성
        sharable_link = f"https://drive.google.com/uc?id={file_id}&export=download"
    
        return sharable_link

    def main(pdf_path):
        service = Google_Drive_Api.authenticate_gdrive()
        file_path = pdf_path  # 업로드할 이미지 파일 경로
        file_name = pdf_path  # Google Drive에 저장할 파일 이름

        link = Google_Drive_Api.upload_to_gdrive(service, file_path, file_name)
        return link


