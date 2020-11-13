var button = document.getElementById("submit-button")
button.onclick = function(){
    var username = document.getElementById("username-entry").value
    console.log(username)
    fetch(`http://localhost:5000/data/${username}`).then(response=>response.text()).then((data)=>{
        console.log(data)
        var dataOutput = document.getElementById("text-output")
        dataOutput.innerHTML = data
    })
}