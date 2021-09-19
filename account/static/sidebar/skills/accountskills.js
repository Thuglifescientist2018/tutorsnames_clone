function fetchSkills() {
    fetch('http://127.0.0.1:8000/api/accountskills/').then(response => response.json()).then(data => console.log(data))
}
fetchSkills();