const validateName = () => {
    const name_input = document.getElementById("name");
    const name_span = name_input.nextElementSibling;
    if(!name_input.value || name_input.value === ""){
        name_span.innerText = "Name required.";
        return false;
    }
    name_span.innerText = "";
    return true;
};

const validateTypes = (event) => {
    const type_input = document.getElementById("type").innerText;
    const type_split = type_input.split(/\r?\n/);
    console.log(type_split)

}


document.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("name").addEventListener("change", validateName);
    // document.getElementById("type").addEventListener("change", validateTypes);
    // document.getElementById("ability").addEventListener("change", validateAbility);
    // document.getElementById("generation").addEventListener("change", validateGeneration);
    const form = document.querySelector('form');
    let valid = false
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
