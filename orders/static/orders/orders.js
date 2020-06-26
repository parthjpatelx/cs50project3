document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.pizza').forEach(link => {
        link.onclick = () => {
            alert('hello');
            const request = new XMLHttpRequest();
            request.open('POST', '/cart');
            
            request.onload = () => {
                alert('request sent to server');
                // Extract JSON data from request
                const data = JSON.parse(request.responseText);
  
                // Update the result div
                if (data.success) {
                    alert('succesful response from server');
                }
                else {
                    alert('error');
                }
            }

            const data = new FormData();
            var pizza_id = link.dataset.pizza;
            data.append('pizza_id', pizza_id);

            var csrftoken = Cookies.get("csrftoken");
            request.setRequestHeader("X-CSRFToken", csrftoken);

            request.send(data);
            return false; 
        }
    }
    ); 
});