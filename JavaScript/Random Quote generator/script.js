const button =document.querySelector("button")
const p =document.querySelector("p")
const API="https://api.quotable.io/random"
button.addEventListener("click",()=>{
    fetch(API).then(res=> res.json()).then(data =>{
        p.innerText=data.content
    }).catch(()=> alert("Error fetching quote!"))
})
