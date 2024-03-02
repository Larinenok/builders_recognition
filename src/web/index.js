document.getElementsByClassName('input_image_button')[0]
    .addEventListener('click', function () {
        eel.get_input_image();
});

document.getElementsByClassName('output_image_button')[0]
    .addEventListener('click', function () {
        eel.save_output_image();
});

eel.expose(set_input_image);
function set_input_image() {
    let img = document.getElementById('input_image');
    img.src = 'images/input_image.png?' + Math.random();
    img.style.visibility = 'visible';
}

document.getElementById("find_button").onclick = function () {
    document.getElementById('idle').style.visibility = 'visible';
    eel.find_human();
};

eel.expose(find_human_success);
function find_human_success() {
    let img = document.getElementById('output_image');
    img.src = 'images/output_image.png?' + Math.random();
    img.style.visibility = 'visible';
    document.getElementById('idle').style.visibility = 'hidden';
}