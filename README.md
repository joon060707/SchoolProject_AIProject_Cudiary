# SchoolProject_AIProject_Cudiary
2025년 2학기 고급AI융합프로젝트 수행
<img width="1448" height="868" alt="스크린샷 2025-12-06 203625" src="https://github.com/user-attachments/assets/5da5f73f-6828-46c5-b4a8-3b70c9af542f" />
## To run this project, do following:
### anaconda environment
- Create a new anaconda environment with python 3.10+, and:
```
conda install pytorch torchvision opencv
```
### frontend server
- In the project:
```
conda install nodejs
npm install bootstrap
npm create vite@latest frontend -- --template svelte
npm install
npm install svelte-spa-router
npm install svelte-file-dropzone
```
- Add Pretendard or other woff2 font files to "web\frontend\src\assets\css\Pretendard\woff2" from the source
- Modify the bootstrap file to apply the font
- Then run
```
cd \web\frontend
npm run dev
```
### file server
- In the project:
```
npm install formidable
```
- Then run
```
cd web/fileserver
node server.js
```
### backend server
- In the project:
```
pip install fastapi
conda install pydantic
pip install "uvicorn[standard]”
```
- Then run
```
cd web/back
uvicorn main:app --reload
```
### database server
- Install MySQL Workbench and Server
- Create database aip;
- Execute **aip_diary.sql** and **aip_plant.sql** to create tables
- And in the project:
```
pip install pymysql
pip install cryptography
```
