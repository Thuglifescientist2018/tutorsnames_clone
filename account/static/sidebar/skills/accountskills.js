const skills_data_ui = document.getElementById("skills_data");
const sub_skills_data_ui = document.getElementById("sub_skills_data");
// function that fetches skills data from api

function fetchSkillsData(size) {
    let url =  '/api/skills/';
    if(size !== 'undefined' && size !== '' && size !== null) {
        url = '/api/skills/?size=' + size;
    }
  
        fetch(url).then(
            response => response.json()
        ).then(data => {
            putIntoSkillsUI(data);
          
           
        })
        
}
let s_current_page = document.getElementById("s_current_page");
let s_total_pages = document.getElementById('s_total_pages')

// fetchSkillsData() call to pass fetched data to putIntoSkillsUI

fetchSkillsData();
// function that puts data received from the function fetchSkillsDatas argument pass
function putIntoSkillsUI(skills) {
    clearSkillsUI();
  skills.results.forEach(function(skill) {
     
      skills_data_ui.innerHTML += `
            <tr>
                    <td> ${skill.id} </td>
                    <td>${skill.skill_name} </td>
                    <td>${skill.skill_status} </td>
                    <td>${skill.order} </td>
                    <td> 
                    <a href="/accounts/skill-edit/${skill.id}">
                        <i id="${skill.id}" class="fa fa-pencil-alt"></i>
                    </a>
                    <a href="/accounts/skill-delete/${skill.id}">
                        <i id="${skill.id}" class="fa fa-trash"></i>
                    </a>
                        ${skill.skill_status ? `<a href="/accounts/skill-deactivate/${skill.id}"><i id="${skill.id}" class='fas fa-window-close'></i></a>`: `<a href="/accounts/skill-activate/${skill.id}"><i id="${skill.id}" class='fas fa-check-circle'></i></a>`}
                    </td>
                  

            </tr>
      `
  })
  s_current_page.innerText = 1;
  s_total_pages.innerText = skills.total_pages;


  
}

// function that fetches the sub skills from the api url
function fetchSubSkillsData(size)  {
    let url = '/api/subskills/'
    if(size !== 'undefined' && size !== '' && size !== null) {
        url = '/api/subskills/?size=' + size;
        
    }
  
    fetch(url).then(response => response.json()).then(data => { 
        putIntoSubSkillsUI(data);
       
    })
}

fetchSubSkillsData();
let sub_current_page = document.getElementById("sub_current_page");
let sub_total_pages = document.getElementById("sub_total_pages")

function putIntoSubSkillsUI(sub_skills)  {
    clearSubSkillsUI();
    sub_skills.results.forEach(function(sub_skill) {
        sub_skills_data_ui.innerHTML += `
        <tr>
            <td> ${sub_skill.id} </td>
            <td> ${sub_skill.sub_skill_name} </td>
            <td> ${sub_skill.skills} </td>
            <td> ${sub_skill.sub_skill_level} </td>
            <td> ${sub_skill.sub_skill_status} </td>  
            <td> ${sub_skill.sub_order} </td>  
            <td>
                <a href="/accounts/subskill-edit/${sub_skill.id}">
                <i class="fa fa-pencil-alt"></i>
                </a>

          
                <a href="/accounts/subskill-delete/${sub_skill.id}">
                <i class="fa fa-trash"></i>
                </a>
                ${sub_skill.sub_skill_status ? `<a href="/accounts/subskill-deactivate/${sub_skill.id}"><i class='fas fa-window-close'></i></a>`: 
                `
                <a href="/accounts/subskill-activate/${sub_skill.id}">
                <i class='fas fa-check-circle'></i>
                </a>


                `
            }
    
             </td>
   
    
           
           
           
          
        </td>
        </tr>
        `
    })
    sub_current_page.innerText = 1;
    sub_total_pages.innerText = sub_skills.total_pages;



}
// usage: skill_page_size and subskill_page_size event listener
// reason: putintoskillsui() += innerhtml so to clear old data before new one
function clearSkillsUI() {
skills_data_ui.innerHTML = "";
}
function clearSubSkillsUI() {
    sub_skills_data_ui.innerHTML = "";

}

const s_prevBtn = document.getElementById('s_prevBtn');
const s_nextBtn = document.getElementById('s_nextBtn');


let  page = 1;

function skillPrevious() {
    fetch('/api/skills/?page=' + page).then(response => response.json()).then(
        data =>  {
            
            if(data.previous) {
                fetch(data.previous).then(response => response.json()).then(data => {
                    clearSkillsUI();
                    putIntoSkillsUI(data);
                    page--;
                    console.log(page)
                })
                s_current_page.innerText = page;
            }
           
        }
    )

}
function skillNext() {
fetch('/api/skills/?page=' + page).then(response => response.json()).then(
    data =>  {
       
        if(data.next) {
            fetch(data.next).then(response => response.json()).then(data => {
                clearSkillsUI();
                putIntoSkillsUI(data);
                
                page++;
                s_current_page.innerText = page;  
                console.log(page)
            })
            
        }
       
    }
)


}
let subskills_page = 1;
function subSkillPrevious() {
    fetch('/api/subskills/?page=' + subskills_page).then(response => response.json()).then(
        data =>  {
           
            if(data.previous) {
                fetch(data.previous).then(response => response.json()).then(data => {
                    clearSubSkillsUI()
                    putIntoSubSkillsUI(data);
                    
                    subskills_page--;
                    sub_current_page.innerText = page;
                })
                
            }
           
        }
    )
}
function subSkillNext() {
    fetch('/api/subskills/?page=' + subskills_page).then(response => response.json()).then(
        data =>  {
           
            if(data.next) {
                fetch(data.next).then(response => response.json()).then(data => {
                    clearSubSkillsUI()
                    putIntoSubSkillsUI(data);       
                    
                    subskills_page++;
                    sub_current_page.innerText = subskills_page;
                })
            }
           
        }
    )
}

// change how many items to show per page using select dropdown
const skill_page_size = document.getElementById("skill_page_size"); // HTML select dropdown
const subskill_page_size = document.getElementById("subskill_page_size"); //HTML Select Dropdown



skill_page_size.addEventListener("change", function() {
    clearSkillsUI();
    fetchSkillsData(this.value);
})
subskill_page_size.addEventListener("change", function() {
    clearSubSkillsUI();
    fetchSubSkillsData(this.value)
})
    
// search

let search_sub_skills = document.getElementById('search_sub_skills');   
let searchskills = document.getElementById('searchskills');

function searchSkillsUI(searches) {
    clearSkillsUI();
    searches.forEach(function(search) {
        
        skills_data_ui.innerHTML += `
        <tr>
                <td> ${search.id} </td>
                <td>${search.skill_name} </td>
                <td>${search.skill_status} </td>
                <td>${search.order} </td>
                <td> 
                <a href="/accounts/skill-edit/${search.id}">
                    <i class="fa fa-pencil-alt"></i>
                </a>
                <a href="/accounts/skill-delete/${search.id}">
                    <i class="fa fa-trash"></i>
                    ${search.skill_status ? `<a href="/accounts/skill-deactivate/${search.id}"><i class='fas fa-window-close'></i></a>`: `<a href="/accounts/skill-activate/${search.id}"><i class='fas fa-check-circle'></i></a>`}
                </td>
              

        </tr>
  `
        
    })
}

//sub skills search results and put it into the UI
function searchSubSkillsUI(searches) {
    clearSubSkillsUI()
    searches.forEach(function(search) {
        
        sub_skills_data_ui.innerHTML += `
        <tr>
            <td> ${search.id} </td>
            <td> ${search.sub_skill_name} </td>
            <td> ${search.skills} </td>
            <td> ${search.sub_skill_level} </td>
            <td> ${search.sub_skill_status} </td>  
            <td> ${search.sub_order} </td>  
            <td>
                <a href="/accounts/subskill-edit/${search.id}">
                <i class="fa fa-pencil-alt"></i>
                </a>

          
                <a href="/accounts/subskill-delete/${search.id}">
                <i class="fa fa-trash"></i>
                </a>
                
                ${search.sub_skill_status ? `
                <a href="/accounts/subskill-deactivate/${search.id}">
                <i class='fas fa-window-close'></i>
                </a>
                
                `: `
                <a href="/accounts/subskill-activate/${search.id}">
                <i class='fas fa-check-circle'></i>
                </a>
                `}
    
             </td>
   
    
           
           
           
          
        </td>
        </tr>
        `
        
    })
}
let search_skills_page = 1;
function searchSkills() {
    if(this.value  !== "") {
   
        fetch('/api/skills/?page='+ search_skills_page).then(response => response.json()).then(datas => {
            
            const filtered_skills = datas.results.filter(data => data.skill_name.toLowerCase().includes(this.value.toLowerCase()))
            console.log("this value ", this.value)
           
            if(filtered_skills.length === 0 && datas.next) {
                search_skills_page++; 
            }
           

           searchSkillsUI(filtered_skills)
            return filtered_skills;
           
            
        } )
        

    
    } else {
        fetchSkillsData()
        search_skills_page = 1;
       
    }
    
}
let search_subskills_page = 1;
searchskills.addEventListener('keyup', searchSkills)
function searchSubSkills() {
    if(this.value  !== "") {
   
        fetch('/api/subskills/?page='+ search_subskills_page).then(response => response.json()).then(datas => {
            
            const filtered_skills = datas.results.filter(data => data.sub_skill_name.toLowerCase().includes(this.value.toLowerCase()))
            console.log("this value ", this.value)
           
            if(filtered_skills.length === 0 && datas.next) {
                search_subskills_page++; 
            }
           

           searchSubSkillsUI(filtered_skills)
            return filtered_skills;
           
            
        } )
        

    
    } else {
        fetchSubSkillsData()
        search_subskills_page = 1;
       
    }
    
}

search_sub_skills.addEventListener('keyup', searchSubSkills)



