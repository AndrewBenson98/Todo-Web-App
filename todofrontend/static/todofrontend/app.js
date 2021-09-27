
var domain = 'http://127.0.0.1:8000/'

//This variable keeps track of the current item the user is editing so 
//we know whether to use POST or PUT methods
var activeItem = null

//CSRF Tokens are required for all POST and PUT requests in Django. 
var csrftoken = null

window.onload = function() {
    
    
    //Token Requiered by Django to post form data
    csrftoken = getCookie('csrftoken');
    buildList()
    addSubmitListenser()

};


/*
This function gets the csrf token. It is from the django documentation
*/
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
		}




/* 
Fetches API Json data.
Generates and sets innerHtml to produce task list
*/
function buildList(){
console.log("Building List")
//API Url
var url = domain +'todo-api/tasks/'

//Get the wrapper that will contain all the list items
const wrapper = document.getElementById('list-wrapper')
wrapper.innerHTML=""
//Fetch the Json data
fetch(url)
.then(response => response.json())
.then(function(data){

    //Use Json data to set inner html
    var tasks = data.results

    //console.log('Data:' , tasks)

    //Loop through each Item in the list and add it to the page
    for (var i in tasks){
    //The Html for each Item

    //If the list item is completed, we want to cross it out
    var title = `<span class="title">${tasks[i].title}</span>`
    if (tasks[i].completed == true){
        title = `<strike class="title">${tasks[i].title}</strike>`
    }



    var item = `
        <div id="data-row-${i}" class="task-wrapper d-flex">
            <div style="flex:7">
                ${title}
            </div>
            <div style="flex:1">
                <button class="btn btn-sm btn-outline-info edit">Edit </button>
            </div>
            <div style="flex:1">
                <button class="btn btn-sm btn-outline-danger delete">X</button>
            </div>
        </div>
    `
    //Append the html to the innerHtml of the wrapper
    //wrapper.innerHTML += item
    wrapper.insertAdjacentHTML('beforeend',item)


    }

    //Add Listeners to the Edit and Delete Buttons 
    for (let i  in tasks){
        var editBtn = document.getElementsByClassName('edit')[i]
        var deleteBtn = document.getElementsByClassName('delete')[i]
        var title = document.getElementsByClassName('title')[i]

        editBtn.addEventListener('click', function(){
            //Sets as the active item
            activeItem = tasks[i]
            document.getElementById('title').value = activeItem.title
        })
        deleteBtn.addEventListener('click', function(){
            var url = domain +'todo-api/tasks/' + tasks[i].id+ '/'
            sendRequest(url,'DELETE')
        })
        
        title.addEventListener('click', function(){
            strikeUnstrike(tasks[i])
        })
    }
})
}



/*
Add Submit button event listener
*/
function addSubmitListenser(){
    var form = document.getElementById('form')
    form.addEventListener('submit', function(e){
        var url = domain +'todo-api/tasks/'

        //If there is an active item (being edited)
        if (activeItem != null){
            //Create NewItem
            var url = domain +'todo-api/tasks/' + activeItem.id+ '/'
            activeItem=null
        sendRequest(url,'PUT')
        }else{
            //If there is no active item, then create
        sendRequest(url,'POST')
        }
    })
}

/*
Create/update Functionality
*/
function sendRequest(url, method, ){

var title = document.getElementById('title').value
    fetch(url, {
        method: method,
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'title':title})
    }
    ).then(function(response){
        
        //Reload the page
        buildList()
        document.getElementById('form').reset()
    })
}


/* 
This function will update an item's "completed" attribute after toggling it
*/
function strikeUnstrike(item){
    var url = domain +'todo-api/tasks/' + item.id+ '/'
    //Toggle Item completed attribute
    item.completed = !item.completed

    //Update the item in the backend
    fetch(url, {
        method: 'PUT',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'title':item.title, 'completed':item.completed})
    }
    ).then(function(response){
        
        //Reload the page
        buildList()
        
    })



}