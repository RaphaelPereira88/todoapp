<html>
  <head>
    <link rel="shortcut icon" href="#">
    <title>Todo App</title>
    <style>
      .hidden {                                        
        display: none;
      }
      ul {
        list-style: none;
        padding: 0;
        margin: 0;
        width: 200px;
      }
      li {
        clear: both;
      }
      li button {
        -webkit-appearance: none;
        border: none;
        outline: none;
        color: red;
        float: right;
        cursor: pointer;
        font-size: 20px;
      }
      .lists-wrapper, .todos-wrapper {
        display: inline-block;
        vertical-align: top;
      }
    </style>
  </head>


  <body>
    <div class="lists-wrapper">
      <ul id="lists">
        {% for list in lists %}
        <li>
          <a href="/lists/{{ list.id }}">
            {{ list.name }}
          </a>
        </li>
        {% endfor %}
      </ul>
    </div>
    
    <div class="todos-wrapper">

      <form id="form">
        <input type="text" id="description" name="description" />
        <input type="submit" value="Create" />
      </form>

      <div id="error" class="hidden">Something went wrong!</div>     <!--in case of error, this message, not show show by default-->
      
      <ul id="todos">
                                 <!-- Jinja for loop-->
        {% for todo in todos %}
                                 <!-- says for every item inside li item, we can repeat li item-->
                                 <!-- description includes successful json response from server-->
        <li>                     <!-- we bound data_id to "{{todo.id}}" to define data attribute as ID -->
          <input class="check-completed" data-id="{{ todo.id }}" 
          type="checkbox" {% if todo.completed %}checked {% endif %} />{{ todo.description }}
          <button class= "delete-button" data-id="{{ todo.id}}">&cross;</button>
        </li>
        {% endfor %}
      </ul>

    </div>
                                  <!-- implementing async fetch logic-->
    <script>
      const checkboxes = document.querySelectorAll('.check-completed');
      for (let i = 0; i < checkboxes.length; i++) {
        const checkbox = checkboxes[i];
        checkbox.onchange = function(e) {
          //console.log('event', e);            just use to retrieve that data below :e.target.dataset['id']          
          const newCompleted = e.target.checked;
          const todoId = e.target.dataset['id'];   //fetch: to make a request to the server ,todoID from app.py added
                                                            
          fetch('/todos/' + todoId + '/set-completed', {
            method: 'POST',
            body: JSON.stringify({
              'completed': newCompleted
            }),
            headers: {
              'Content-Type': 'application/json'              //since it's Json that we re sending over we need to specify content type
            }
          })
          .then(function() {
            document.getElementById('error').className = 'hidden'; 
          })
          .catch(function() {
            document.getElementById('error').className = '';
          })
        }
      }  
                                                               //to send automatically information to the server
      document.getElementById('form').onsubmit = function(e) {
        e.preventDefault();   
                                                            //default behaviour 
                                                            //send post request asynchronously using fetch      
                                                            //we want to send a body of information that iclude the input when we hit Submit                      
        fetch('/todos/create', {                            
          method: 'POST',
          body: JSON.stringify({                            
            'description': document.getElementById('description').value
          }),
                                                            //since it's Json that we re sending over we need to specify content type
          headers: {                                         
            'Content-Type': 'application/json'
          }
        })                                                  // to analyse the json response and return it 
        .then(function(response) {                           
          return response.json();
        })                                                  //to manipulate the json response, to create the new object , we need to append it
        .then(function(jsonResponse) {                        
          console.log(jsonResponse);
          const liItem = document.createElement('LI');     //to append the new object
          liItem.innerHTML = jsonResponse['description'];
          document.getElementById('todos').appendChild(liItem);
          document.getElementById('error').className = 'hidden'; 
          window.location.reload(true);
        })
        .catch(function() {                                   // iand just in case there's an error, the catch function will get it and will activate the hidden class
          document.getElementById('error').className = '';
        })
      }
      const deleteBtns = document.querySelectorAll('.delete-button');
        for (let i =0; i< deleteBtns.length; i++) { 
          const btn= deleteBtns[i];
          btn.onclick = function(e){
            const todoId = e.target.dataset['id'];
            fetch('/todos/' + todoId, {
              method:'DELETE'
            })
            .then (function(jsonResponse) {
              window.location.reload(true);
            })
          }
        }
    </script>
  </body>
</html>
