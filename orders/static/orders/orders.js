document.addEventListener('DOMContentLoaded', function(){
    alert('hello');
    document.querySelectorAll('.pizza').forEach(link => {
        link.onclick = () => {
            alert('hello');
        }
    }
    ); 
});