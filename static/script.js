// Image
background = document.getElementsByClassName("background")[0];
background.src = "/static/background.bmp";
background.alt = "Background";
background.style.position = "absolute";
background.style.width = "100%";
background.style.height = "100%";
background.style.objectFit = "cover";
document.body.appendChild(background);