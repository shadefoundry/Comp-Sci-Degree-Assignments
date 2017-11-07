/* 
Assignment 9_10
Kevin Lopez
 */


function generate(){
    var name = document.getElementById("name").value;
    var color = document.getElementById("favcolor").value;
    var text = document.getElementById("text").value;
    var el = document.getElementById('insertHere');
    //window.alert(name +" "  + color+ " " + font+ " " + text;
    el.innerHTML = '<div id="generatedCard"><p id="sizeOfFont" class="blink_text">'+name+'</p><p>'+text+'</p>\n\
<img src="img/img.png" alt="Card Image"></div>';
    document.getElementById("generatedCard").style.backgroundColor=color;
}