
var picture_index = 0;

function prev() {
    picture_index = ((picture_index + 5) - 1) % 5
    var picture_uri = `pictures/${picture_index}.jpeg`
    document.getElementById("picture").src = picture_uri
}

function next() {
    picture_index = (picture_index + 1) % 5
    var picture_uri = `pictures/${picture_index}.jpeg`
    document.getElementById("picture").src = picture_uri
}


function changeColor() {
    var borderRed = document.getElementById('border-red').value || 0;
    var borderGreen = document.getElementById('border-green').value || 0;
    var borderBlue = document.getElementById('border-blue').value || 0;
    
    var borderWidth = document.getElementById('border-width').value || 0;
    
    var backgroundRed = document.getElementById('background-red').value || 0;
    var backgroundGreen = document.getElementById('background-green').value || 0;
    var backgroundBlue = document.getElementById('background-blue').value || 0;
    
    var paragraph = document.getElementById('paragraph');
    paragraph.style.borderColor = `rgb(${borderRed}, ${borderGreen}, ${borderBlue})`;
    paragraph.style.borderWidth = `${borderWidth}px`;
    paragraph.style.backgroundColor = `rgb(${backgroundRed}, ${backgroundGreen}, ${backgroundBlue})`;
}

function validate() {
    var pw1 = document.getElementById("pw1").value;
    var pw2 = document.getElementById("pw2").value;


    if (pw1.length < 8) {
        alert("The length of the first password is less than 8 letters!")
    } else if (pw1 != pw2) {
        alert("Two passwords don't match!")
    } else {
        alert("Everything is good!")
    }
}
