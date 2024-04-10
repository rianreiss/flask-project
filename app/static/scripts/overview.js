function addD() {
    var x = document.getElementById("add-form-d");
    var y = document.getElementById("add-D");
    if (x.style.display == "none") {
        x.style.display = "table-row";
        document.getElementById('descD').focus();
        y.style.display = "none"
    } else {
        x.style.display = "none";
        y.style.display = "table-row"
    }
}

function addR() {
    var x = document.getElementById("add-form-r");
    var y = document.getElementById("add-R");
    if (x.style.display == "none") {
        x.style.display = "table-row";
        document.getElementById('descR').focus();
        y.style.display = "none"
    } else {
        x.style.display = "none";
        y.style.display = "table-row"
    }
}
