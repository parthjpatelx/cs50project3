document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.pizza').forEach(link => {
        link.onclick = () => {
            alert('link has been clicked')
            pizza_id = link.dataset.pizza

            const request = new XMLHttpRequest();
            request.open('POST', '/cart');

            // Add a csrf-token to the request headers so that Django accepts the request
            var csrftoken = Cookies.get("csrftoken");
            request.setRequestHeader("X-CSRFToken", csrftoken);
            

            request.onload = () => {

                // Extract JSON data from request
                const data = JSON.parse(request.responseText);
  
                // Update the result div
                if (data.success) {
                    alert('success');
                }
                else {
                    alert('error');
                }
            }

            const data = new FormData();
            pizza_id = true;
            data.append('pizza_id', pizza_id);


  
            // Send request
            request.send(data);
            return false;            
    
        }
    }
    ); 
});