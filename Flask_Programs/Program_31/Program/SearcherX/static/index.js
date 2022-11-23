var mybut = document.getElementById("btn1");
const x = document.getElementById("myDIV");
const y = document.getElementById("nss");




mybut.addEventListener("click", function () {
    const Inputval = document.getElementById("pwd");
    console.log("Clicked")
    console.log(x.style.display);
    console.log(y.style.display);

    if (Inputval.value == "") {
        console.log("Empty Input");
    } else {
        if (x.style.display == "none") {
            x.style.display = "block";
        }
        if (y.style.display == "block") {
            y.style.display = "none";
        }
    }
});