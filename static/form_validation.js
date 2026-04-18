document.addEventListener("DOMContentLoaded", (event) => {
    let valid = false
    const form = document.querySelector('form');
    form.addEventListener('submit', (event) => {    
        if (!valid){
            const formData = new FormData(form);  
            if (formData.getAll('type').length <= 2){
                valid = true
            }
            else if (formData.getAll('type').length > 2 || !valid){
                event.preventDefault();
                alert("Too many types selected")
            }
        }
    });   
})
