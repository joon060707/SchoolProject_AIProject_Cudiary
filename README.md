# SchoolProject_AIProject_Cudiary
2025년 2학기 고급AI융합프로젝트 수행

## To run this project, do following:
### anaconda environment
- Create a new anaconda environment with python 3.10+, and:
```
conda install pytorch torchvision opencv
```
### frontend server
```
conda install nodejs
npm install bootstrap
npm create vite@latest frontend -- --template svelte
npm install
npm install svelte-spa-router
npm install svelte-file-dropzone
```
Then run
```
cd \web\frontend
npm run dev
```
### file server
```
npm install formidable
```
Then run
```
cd web/fileserver
node server.js
```
### backend server
```
pip install fastapi
conda install pydantic
pip install "uvicorn[standard]”
```
Then run
```
cd web/back
uvicorn main:app --reload
```
### database server
Install MySQL Workbench and Server
```
pip install pymysql
pip install cryptography
```
