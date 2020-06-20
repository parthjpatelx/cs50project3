document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.pizza').forEach(link => {
        link.onclick = () => {
            var quantity = prompt('please enter quantity')
            quantity = parseInt(quantity)
            pizza_id = link.dataset.pizza

            // send quantity and id of pizza object to server so that server can add to cart
        }
    }
    ); 
});