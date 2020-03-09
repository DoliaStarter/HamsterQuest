/**
 * Module should contain functions shared by the most of js scripts.
 * Such function could be redirection, element creation, data processing, etc.
 */

/**
 * Redirects to given url
 * @param {string} to - url to redirect 
 */
function redirect(to){
    window.location.replace(to)
}

/**
 * Shostcut to document.getElementById 
 * @param {string} element_id 
 * @returns Same as document.getElementById
 */
function $(element_id){
    return document.getElementById(element_id)
}

export {redirect, $};