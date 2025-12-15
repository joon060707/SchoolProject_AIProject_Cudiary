/**
 * Example: fastapi('get', '/items/', {item_id:123}, success_callback, failure_callback)
 * @param {*} operation is 'get', 'post', 'put', 'delete'
 * @param {*} url is the API endpoint URL
 * @param {*} params is the request payload
 * @param {*} success_callback is the callback function for successful responses
 * @param {*} failure_callback is the callback function for failed responses
 */
const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    // generate URL and options
    let _url = 'http://127.0.0.1:8000'+url
    // if(method === 'get') {
    //     _url += "?" + new URLSearchParams(params)
    // }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if (method !== 'get') {
        options['body'] = body
    }

    // make the fetch call
    fetch(_url, options)
        .then(response => {
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) {  // 200 ~ 299
                        if(success_callback) {
                            // console.log("API Success:", json)
                            success_callback(json)
                        }
                    }else {
                        if (failure_callback) {
                            console.log("API Failure:", json)
                            failure_callback(json)
                        }else {
                            console.log("API Unknown:", json)
                            failure_callback(json)                                                        
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    console.log("API Response Parse Error:", error)
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi // export the fastapi function