function upDate(element){
  document.getElementById('image').innerHTML= element.alt;
  image.style.backgroundImage = "url("+element.src+")";
  //document.getElementById('image').innerHTML = "<img src='"+element.src+"'>";
 //'url(http://localhost/background.png)'
}

function unDo(element){
  document.getElementById('image').innerHTML = "Hover over an image below to display here."
  image.style.backgroundImage = "url()";
}
