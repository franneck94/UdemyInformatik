var computeButton = document.getElementById('computeButton');
computeButton.addEventListener('click', square);

function square() {
    var input = document.getElementById('input');
    var result = input.value * input.value;
    alert(result);
    input.value = 0;
}
