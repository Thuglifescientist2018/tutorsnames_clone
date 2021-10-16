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
                        <i id="${skill.id}" class="fa fa-pencil-alt"></i>
                        <i id="${skill.id}" class="fa fa-trash"></i>
                        ${skill.skill_status ? `<i id="${skill.id}" class='fas fa-window-close'></i>`: `<i id="${skill.id}" class='fas fa-check-circle'></i>`}
                    </td>
                  

            </tr>
      `
  })

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
      
                <i class="fa fa-pencil-alt"></i>

          
           
                <i class="fa fa-trash"></i>
                ${sub_skill.sub_skill_status ? "<i class='fas fa-window-close'></i>": "<i class='fas fa-check-circle'></i>"}
    
             </td>
   
    
           
           
           
          
        </td>
        </tr>
        `
    })

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
                console.log(page)
            }
                )
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
                    console.log("subskills page after previous: ", subskills_page)
                }
                    )
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
                    console.log("subskills page after next: " , subskills_page)
                }
                    )
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
                    <i class="fa fa-pencil-alt"></i>
                    <i class="fa fa-trash"></i>
                    ${search.skill_status ? "<i class='fas fa-window-close'></i>": "<i class='fas fa-check-circle'></i>"}
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
      
                <i class="fa fa-pencil-alt"></i>

          
           
                <i class="fa fa-trash"></i>
                ${search.sub_skill_status ? "<i class='fas fa-window-close'></i>": "<i class='fas fa-check-circle'></i>"}
    
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
searchskills.addEventListener('keyup', searchSkills)


search_sub_skills.addEventListener('keyup', function() {

    if(this.value  !== "")  {
        
        fetch('/api/subskills_all/').then(response => response.json()).then(datas => {
           
           const filtered_skills = datas.filter(data => data.sub_skill_name.toLowerCase().includes(this.value.toLowerCase()))
           console.log('subskills:', filtered_skills)
           searchSubSkillsUI(filtered_skills)
        });
       
    }else {
        fetchSubSkillsData();
    }
  
    
    
})

// CRUD = Create, Read, Update, Delete functionality
//Skill CRUD

skills_data_ui.addEventListener("click", updateSkill)

//create popup UI for CRUD Icon Clicks
function updateSkill(event) {
    if(event.target.classList.contains('fa-pencil-alt')) {
        let targetParent = event.target.parentElement.parentElement;
        let skill_id = event.target.id;
        fetch('/api/update_skill/' + skill_id).then(response => response.json()).then(data => updateSkillViewUI(data));
          
        
    }
    
    
} 
function updateSkillViewUI(skill) {
    let skills_and_subskills = document.getElementById("skills_and_subskills");
    let manage_profile = document.getElementById("manage_profile");
    manage_profile.style.gridTemplateColumns = "20% 80%";
    skills_and_subskills.innerHTML = "";

    skills_and_subskills.innerHTML += `
    <div id="updateView">
     <h1>Update this item</h1>
     <form method='POST'>
       <label for="skill_name">Skill Name:</label>
       <input type="text" id="skill_name" value='${skill.skill_name}'>
       <label for="order">Order:</label>
       <input type="text" id="order" value='${skill.order}'>
       <button type="submit" id="skill_update_btn" class='btn btn-update'>Update</button>
     </form>
   </div>
    `
}
// skill update_btn 

