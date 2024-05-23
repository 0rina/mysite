function myFunction(gameName, index) {
    console.log(gameName);
    var input = document.createElement("input");
    input.type = "text";
    input.id = "opinion_id"; // unique ID
    input.name = "opinion"; // unique namę
    var button = document.createElement("button");
    button.innerHTML = "Send";

    button.onclick = function() {
        var text = input.value;
        if (text.trim() === '') {
            alert('Write opinion, it can not be empty');
            return;
        }
        console.log(text);

        // Tworzenie URL dla nowej strony
        var newPageUrl = '/g2/' + gameName ;

        // Przekierowanie do nowej strony
        window.location.href = newPageUrl;
    };

    var element = document.getElementById(gameName + index);
    document.getElementById(gameName + index).innerHTML = "Opinion:";
    document.getElementById(gameName + index).appendChild(input);
    element.appendChild(button);
    return gameName, input;
}
