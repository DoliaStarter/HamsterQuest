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

function openTab(){}

export {redirect, openTab};