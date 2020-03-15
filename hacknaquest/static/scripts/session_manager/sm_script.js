// Cool, but you can make it generic !
// Method, that will switch between tabs.
import {$} from '../common.js'

function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
 
  // for (let tab of tablinks)
  // tab.className = tab.className.replace(" active", "")
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

// More readable form
// openTab("Task")
document.getElementById("defaultOpen").click();


function process_django_dict(quest_data){
  quest_data = quest_data.replace(/&#x27;/g, "\"");
  quest_data = JSON.parse(quest_data);    
  return quest_data
}
function updateTaskInfo(stageInfo, quest_data){
    $("task_name").innerHTML = "<b>" + 'stage1' +"</b>"
    $("task_field").innerHTML = stageInfo['task'] + "<br><i>" + quest_data['author'] + "</i></br>"
    $("status_field").innerHTML = stageInfo['status'] 
}
function createExpandingMenu(forToggle){
  let myLabels = document.querySelectorAll(forToggle);
  Array.from(myLabels).forEach(label => {
  label.addEventListener('keydown', e => {
    if (e.which === 32 || e.which === 13) {
      e.preventDefault();
      label.click();
    };
  });
});
}

export {createExpandingMenu, updateTaskInfo, process_django_dict, openTab}