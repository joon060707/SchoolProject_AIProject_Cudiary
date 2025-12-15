// Simple HTTP server in Node.js
import { createServer } from 'http';
import { copyFileSync, readFile, unlinkSync } from 'fs';
import {formidable} from 'formidable';

var baseURL = 'http://localhost:3000/';
var baseLocalPath = "D:\\AIP1\\web\\fileserver\\";

// 파일 서버 만들기
createServer(function (req, res) {

    // ADD cors headers
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:5173');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'content-type,multipart/form-data'); 
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Handle file uploads
    if (req.method === 'OPTIONS' || req.method === 'POST') {

        const form = formidable({ multiples: false });
        form.parse(req, function (err, fields, files) {

            if (err) {
                console.error(err);
                console.log(`Request failed. Parsing error.`);
                res.writeHead('400', { 'Content-Type': 'text/html; charset=utf8'});
                res.write("{status: 'failed'}");
                res.end();
                return;
            }
            if(files.file[0] == undefined){
                console.log(`Request failed. No file uploaded.`);
                res.writeHead('400', { 'Content-Type': 'text/html; charset=utf8'});
                res.write("{status: 'failed'}");
                res.end();
                return;
            }

            // no problem
            var f = files.file[0]; // 업로드된 파일 정보
            var oldpath = f.filepath;
            var newpath = 'upload/' + Date.now() + '-' + f.originalFilename; // no f.newFilename; // no Date.now() 

            copyFileSync(oldpath, newpath); // temp -> upload 폴더로 이동
            unlinkSync(oldpath); // 임시파일 삭제

            console.log(`Request successful.`);

            ///////////////////////////////
            // return the file path
            var path = 'http://localhost:3000/' + newpath;
            console.log(path);
            res.writeHead('200', { 'Content-Type': 'text/html; charset=utf8'});
            res.write(path);
            // res.write("{status: 'success', filepath: '" + path + "'}");
            res.end();
        });

/*
// for reference only, not used currently
        // console.log(req.headers['someheader']);

        // // Check for Content-Length header
        // let contentLength = parseInt(req.headers['content-length'])
        // if (isNaN(contentLength) || contentLength <= 0 ) {
        //     res.statusCode = 411;
        //     res.end(JSON.stringify({status: "error", description: "No File"}))
        //     return
        // }

        // // Try to use the original filename
        // let filename = req.headers['filename']
        // if (filename == null) {
        // filename = Date.now() + ".jpg";
        // }
        
        // const filestream = fs.createWriteStream(`${__dirname}/${filename}`)
        // filestream.on("error", (error) => {
        //     console.error(error)
        //     res.statusCode = 400;
        //     res.write(JSON.stringify({status: "error", description: error}))
        //     res.end();
        // })

        // // Write data as it comes
        // req.pipe(filestream)

        // req.on('end', () => {
        //     filestream.close(() => {
        //         res.end(JSON.stringify({status: "success"}))
        //     })
        // })

        // res.writeHead('200', { 'Content-Type': 'text/html;' });
        // res.write(fs.readFileSync('./upload/test.txt'));
        // res.statusCode = 200;
*/

    // preview image
    }else if (req.method === 'GET') {

        // show image
        console.log(req.url);
        req.url = decodeURIComponent(req.url); // in case of spaces or special characters
        var path = baseLocalPath + req.url // expected: "D:\AIP1\web\fileserver\upload\1762233695367-1762233695352captured_image.png"
        readFile(path, (err, data) => { // expected: "upload/1762233695367-1762233695352captured_image.png"
            if (err) {
                console.log("Error: ", err);
                res.writeHead('404', { 'Content-Type': 'text/html; charset=utf8'});
                res.write("File not found");
                res.end();
                return;
            }
            res.writeHead('200', { 'Content-Type': 'image/*'});
            res.write(data);
            res.end();
        });

    }else {
        console.log(`Request failed. ${req.method} method not supported.`);
        res.writeHead('400', { 'Content-Type': 'text/html; charset=utf8'}); // 잘못된 요청
        res.write("{status: 'failed'}");
        res.end();
    }

    console.log(`Request for ${req.url} received.`);
}).listen(3000, () => {
  console.log(`Server running at http://localhost:3000/`);
})
