function fetchSkills() {
    fetch('http://127.0.0.1:8000/api/accountskills/').then(response => response.json()).then(infos => {
        addSkillsUIData(infos);
    

    });

}

fetchSkills();
function addSkillsUIData(infos) {
    let skills_data = document.getElementById('skills_data');
    infos.forEach(function (info) {
        skills_data.innerHTML += `
        <tr>
        <td>${info.id}</td>
        <td>${info.skill_name}</td>
        <td><button class="status btn ${info.skill_status ? 'btn-active' : 'btn-inactive'}">${info.skill_status ? 'Active' : 'Inactive'}</button></td>
        <td>${info.order}</td>
        <td>
            <i class="fa fa-pencil-alt"></i>
            <i class="fa fa-trash"></i>
            <i class="fa fa-window-close"></i>
        </td>
     </tr>
        `
    })


}
function fetchSubSkills() {
    fetch('http://127.0.0.1:8000/api/accountsubskills/').then(response => response.json()).then(infos => {
        addSubSkillsUIData(infos)
    

    });

}
fetchSubSkills()
function addSubSkillsUIData(infos) {
    let sub_skills_data = document.getElementById('sub_skills_data');
    infos.forEach(function (info) {
        sub_skills_data.innerHTML += `
       <tr>
       <td>${info.id}</td>
       <td>${info.sub_skill_name}</td>
       <td><button class="status btn ${info.sub_skill_status ? 'btn-active' : 'btn-inactive'}">${info.sub_skill_status ? 'Active' : 'Inactive'}</button></td>
       <td>${info.sub_order}</td>
       <td>
           <i class="fa fa-pencil-alt"></i>
           <i class="fa fa-trash"></i>
           <i class="fa fa-window-close"></i>
       </td>
    </tr>
       `
    })

}


