// Skills search functionality
const skills_data = document.querySelector("#skills_data");
let titles = skills_data.querySelectorAll(".skill_name");
const search_bar = document.querySelector("#searchskillscell #searchskills");
search_bar.addEventListener("keyup", function() {
    let names = [];
    let search_query = this.value;
    titles.forEach(function(title){
        names.push(title.innerHTML)
    })
    
   let filtered_names = names.filter(name => name.toLowerCase().includes(search_query.toLowerCase()))
   titles.forEach(function(title){
       filtered_names.forEach(function(filtered_name) {
           if(title.innerHTML.toLowerCase() === filtered_name.toLowerCase()){
               title.parentElement.style.display = "table-row";
           }
           else if (title.innerHTML.toLowerCase() !== filtered_name.toLowerCase()){
               title.parentElement.style.display = "none";    
           }
           
           
       })
   })

   if(search_query === "") {
        titles.forEach(function(title) {
            title.parentElement.style.display = "table-row";
        })
        displayPaginatedItems();
   }
   

})

// Pagination of skills
let pagination = 10;
const rows = skills_data.querySelectorAll("tr");
function displayPaginatedItems() {
    for(let i=rows.length-1; i>=pagination; i--) {
    
        rows[i].style.display = "none"
    }

}
displayPaginatedItems();

// pagination of skills (bottom) buttons and info
const entries_and_page = document.getElementById("entries_and_page");
const skills_pagination_info = entries_and_page.querySelector("#s_p_info");
const from = skills_pagination_info.querySelector("#from");
const to = skills_pagination_info.querySelector("#to");
const sn = document.querySelectorAll('.s_sn'); // .s_sn meaning skills serial number
const nofse = document.querySelector("#nofse") // number of skills entry span display
let displayed_items = 0;
for(let i=0; i<rows.length; i++) {
    if(rows[i].style.display !== "none") {
        displayed_items++;
    }
}
if(sn.length > 0) {
    from.innerText = "1";
}
to.innerText = displayed_items;
nofse.innerText = sn.length;

// Sub Skill Search functionality
const sub_skills_data = document.querySelector("#sub_skills_data");
let sub_titles = sub_skills_data.querySelectorAll(".sub_skill_name");
const search_bar2 = document.querySelector("#search_sub_skills");
search_bar2.addEventListener("keyup", function() {
    let names = [];
    let search_query = this.value;
    sub_titles.forEach(function(title) {
        names.push(title.innerHTML)
    })
    let filtered_names = names.filter(name => name.toLowerCase().includes(search_query.toLowerCase()))
    sub_titles.forEach(function(title){
        filtered_names.forEach(function(filtered_name) {
            if(title.innerHTML.toLowerCase() === filtered_name.toLowerCase()){
                title.parentElement.style.display = "table-row";
            }
            else if (title.innerHTML.toLowerCase() !== filtered_name.toLowerCase()){
                title.parentElement.style.display = "none";    
            }
            
            
        })
    })
    if(search_query === "") {
        sub_titles.forEach(function(title) {
            title.parentElement.style.display = "table-row";
        })
   }


})


