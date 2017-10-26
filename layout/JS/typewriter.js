var i = 0;
var txt = $TEXT$;
var speed = $SPEED$;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("$ID$").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
