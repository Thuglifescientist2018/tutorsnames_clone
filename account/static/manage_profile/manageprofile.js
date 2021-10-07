// Preferences buttons
let allbtns = document.querySelectorAll(".update_info_detail_2 .button");
for(let i=0; i<allbtns.length; i++) {

    allbtns[i].addEventListener("click", function(e) {
       let select = this.previousElementSibling;
    console.log(select.selectedIndex)
    if(select.selectedIndex == 2) {
        select.options[1].selected = true;
        let leftpart = this.querySelector(".first");
        let rightpart = this.querySelector(".second");


        leftpart.style.width = "90%";
        rightpart.style.width = "10%";
        leftpart.style.transition = "0.3s all";
        rightpart.style.transition = "0.3s all";
        let switchtext = this.querySelector("span");
        switchtext.innerText = "On";
    }else if(select.selectedIndex == 1) {
        select.options[2].selected = true;
        let leftpart = this.querySelector(".first");
        let rightpart = this.querySelector(".second");
        leftpart.style.width = "50%";
        rightpart.style.width = "50%";
        leftpart.style.transition = "0.3s all";
        rightpart.style.transition = "0.3s all";
        let switchtext = this.querySelector("span");
        switchtext.innerText = "Off";
        
    }
       
       
    })

let selected = allbtns[i].previousElementSibling;
let firstpart = allbtns[i].querySelector(".first");
let lastpart = allbtns[i].querySelector(".second");
if(selected.selectedIndex === 2) {
    firstpart.style.width = "50%";
    lastpart.style.width = "50";
    firstpart.style.transition = "0.3s all";
    firstpart.querySelector("span").innerText = "Off";

}else if(selected.selectedIndex === 1) {
    firstpart.style.width = "90%";
    lastpart.style.width = "10%";
    firstpart.style.transition = "0.3s all";
    firstpart.querySelector("span").innerText = "On";
}

}

// manage profile button(navbar) show or hide options
let user_profile_name = document.getElementById('profile_name')
let user_profile_options = document.getElementById('user_profile_options');


user_profile_name.addEventListener('click', function(e) {
    e.preventDefault(); 
    if(user_profile_options.classList.contains('dont_display')) {
        user_profile_options.classList.remove('dont_display')
    }
    else {
        user_profile_options.classList.add('dont_display')
    }
  
   console.log(user_profile_options_list)
})