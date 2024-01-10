
window.onload = function () {
    var userResponse = confirm("Here are your instructions. Click OK to begin the test, or Cancel to return to the previous screen.");
    if (userResponse) {
        // User clicked OK, start the test
        // You can add logic here to start the test
        fetch('/generate-paragraph')
            .then(response => response.json())
            .then(data => {
                document.getElementById('generated-paragraph').value = data.paragraph;
            })
            .catch(error => console.error('Error:', error));
        document.getElementById('user-input').focus();
    } else {
        // User clicked Cancel, redirect to previous screen
        window.history.back();
    }
}