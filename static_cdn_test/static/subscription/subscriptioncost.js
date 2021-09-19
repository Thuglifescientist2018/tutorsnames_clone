let monthlyPlan = document.querySelector(".monthlyPlan");
let yearlyPlan = document.querySelector(".yearlyPlan");

let monthlybtn = document.querySelector(".cards").querySelectorAll(".btn")[0]
let yearlybtn = document.querySelector(".cards").querySelectorAll(".btn")[1]
yearlyPlan.style.display = "flex";
monthlyPlan.style.display = "none";


monthlybtn.addEventListener("click", function() { 
   this.classList.add("selectedPlan");
   this.classList.remove("unselectedPlan");
   yearlybtn.classList.remove("selectedPlan");
   yearlybtn.classList.add("unselectedPlan");
   monthlyPlan.style.display = "flex";
   yearlyPlan.style.display = "none";
})

yearlybtn.addEventListener("click", function() { 
    this.classList.add("selectedPlan");
    this.classList.remove("unselectedPlan");
    monthlybtn.classList.remove("selectedPlan");
    monthlybtn.classList.add("unselectedPlan");
    yearlyPlan.style.display = "flex";
    monthlyPlan.style.display = "none";

})

console.log('subscription cost');