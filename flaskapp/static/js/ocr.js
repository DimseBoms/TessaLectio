const actualBtn = document.getElementById('upload');
const fileChosen = document.getElementById('file-chosen');
const uploadButton = document.getElementById('submitLabel');
const submitBtn = document.getElementById('submit');
const uploadBtn = document.getElementById('upload-label');

// Show the file selected for upload
actualBtn.addEventListener('change', function() {
    fileChosen.textContent = this.files[0].name
    uploadBtn.style.backgroundColor = 'var(--main-color)';
    fileChosen.style.color = 'black';
});

// Enable submit button on file upload

document.getElementById('upload').onchange = function() {
    submitLabel.classList.remove('disabled');
    submitLabel.classList.add('btn-primary')
};