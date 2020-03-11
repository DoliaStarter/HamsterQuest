/**
 * Module should contain functions shared by the most of js scripts.
 * Such function could be redirection, element creation, data processing, etc.
 */

/**
 * Redirects to given url
 * @param {string} to - url to redirect 
 */
function redirect(to) {
    window.location.replace(to)
}

/**
 * Shostcut to document.getElementById 
 * @param {string} element_id 
 * @returns Same as document.getElementById
 */
function $(element_id) {
    return document.getElementById(element_id)
}
/**
 * Converts HTML form to dictionary
 * @param {HTMLFormElement} form - form to convert
 * @returns Dictionary where field names are keys and input values - values
 */
function formToDict(form) {
    let elements = form.elements
    let reducer = (accumulator, field) => {
        if (field.name && field.value)
            accumulator[field.name] = field.value
        return accumulator
    }
    let valid_elements = Object.values(elements).reduce(reducer, {})
    return valid_elements
}


/**
 * Sends request and executes callback when request is received.
 * @param {string} url - endpoint
 * @param {dict} data - data to send. Leave empty if send a POST request
 * @param {string} method - request method
 * @returns new Promise
 */
function sendRequest(url, data, method) {
    return new Promise(function (resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open(method, url, true);
        xhr.timeout = 5000;
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                if (method == "GET") {
                    result = JSON.parse(xhr.responseText)
                    resolve(result)
                } else {
                    resolve();
                }
            }
            else if (xhr.readyState == XMLHttpRequest.DONE) {
                var response = JSON.parse(xhr.responseText)
                alert(response.message)
            }
        };
        xhr.ontimeout = () => {
            reject("That took too long")
        }
        //TODO implement triming 
        xhr.send(JSON.stringify(data))
    }
    )
}



export { $, redirect, formToDict, sendRequest };