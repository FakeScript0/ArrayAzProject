let password=document.getElementById("inp input")
let icon=document.getElementById("img")

function show(){
    
    if(password.type=="password"){
        password.type="type"
        icon.src ="./assets/icons/close.png"
    }else{
        password.type="password"
        icon.src ="./assets/icons/open.png"
    }


}


