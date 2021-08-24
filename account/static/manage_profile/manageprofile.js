// Preferences buttons
let allbtns = document.querySelectorAll(".update_info_detail_2 .button");
for(let i=0; i<allbtns.length; i++) {
    allbtns[i].addEventListener("click", function(e) {
        let checkbox  = this.previousElementSibling;
        checkbox.click();
        let leftpart = this.querySelector(".first");
        let lastpart = this.querySelector(".second");
        leftpart.style.transition = "0.3s all";
        lastpart.style.transition = "0.3s all";
        if(checkbox.checked) {
            let status = this.querySelector(".first .status");
            status.innerText = "On";
            leftpart.style.width = "90%";
            lastpart.style.width = "10%";
            
        }
        else  {
            let status = this.querySelector(".first .status");
        status.innerText = "Off";
            leftpart.style.width = "50%";
            lastpart.style.width = "50%";
        }
        
       
    })



}